/// <reference lib="webworker" />

/**
 * StudyFeed service worker.
 *
 * Precaching and the offline navigation fallback come from Workbox. On top of that this file owns
 * the daily reminder when the app is closed:
 *
 *  - `periodicsync` — the browser wakes the worker on its own schedule (Chrome, Android, installed
 *    app). The worker cannot read localStorage, so it reads today's status from IndexedDB, where
 *    $lib/reminders.ts keeps it, and posts the nudge itself if the goal is unmet.
 *  - `push` — real server push, used when VAPID keys are configured (see $lib/push.ts).
 *  - `notificationclick` — tapping a nudge opens the app on the home screen, which is where the
 *    daily-goal banner lives.
 */
import { cleanupOutdatedCaches, createHandlerBoundToURL, precacheAndRoute } from 'workbox-precaching';
import { NavigationRoute, registerRoute } from 'workbox-routing';
import { readMirror, type ReminderMirror } from '$lib/reminder-db';

declare let self: ServiceWorkerGlobalScope & {
	__WB_MANIFEST: Array<{ url: string; revision: string | null }>;
};

precacheAndRoute(self.__WB_MANIFEST);
cleanupOutdatedCaches();

self.addEventListener('install', () => {
	self.skipWaiting();
});

self.addEventListener('activate', (event) => {
	event.waitUntil(self.clients.claim());
});

// Any navigation that is not already cached falls back to the prerendered home page, so a page the
// student has never opened offline still arrives on something real instead of a blank screen.
registerRoute(new NavigationRoute(createHandlerBoundToURL('/')));

const NUDGE_TAG = 'studyfeed-daily';

function nudgeText(remaining: number): { title: string; body: string } {
	return {
		title: remaining === 1 ? 'StudyFeed — 1 card to go today' : `StudyFeed — ${remaining} cards to go today`,
		body:
			remaining === 1
				? 'One card left. Two minutes and you are done for the day.'
				: `${remaining} cards left. Two minutes and you are done for the day.`
	};
}

async function postNudge(remaining: number): Promise<void> {
	const { title, body } = nudgeText(Math.max(1, remaining));
	await self.registration.showNotification(title, {
		body,
		tag: NUDGE_TAG,
		renotify: true,
		icon: '/icon-192.png',
		badge: '/favicon.svg',
		data: { url: '/' }
	});
}

/**
 * True when a nudge is owed right now: reminders are on, today's goal is unmet, and the local time
 * has reached the reminder hour.
 */
function nudgeOwed(mirror: ReminderMirror | null, now: Date): boolean {
	if (!mirror || !mirror.enabled) return false;
	if (mirror.day !== localDay(now)) return false; // record is from another day: nothing to say
	if (mirror.done >= mirror.goal) return false;
	const minutes = now.getHours() * 60 + now.getMinutes();
	return minutes >= mirror.hour * 60 + mirror.minute;
}

function localDay(d: Date): string {
	const y = d.getFullYear();
	const m = String(d.getMonth() + 1).padStart(2, '0');
	const day = String(d.getDate()).padStart(2, '0');
	return `${y}-${m}-${day}`;
}

/* ---------------- closed-app nudge: periodic background sync ---------------- */

self.addEventListener('periodicsync', (event) => {
	const typed = event as ExtendableEvent & { tag?: string };
	if (typed.tag && typed.tag !== 'studyfeed-daily') return;
	typed.waitUntil(
		(async () => {
			const mirror = await readMirror();
			if (!nudgeOwed(mirror, new Date())) return;
			await postNudge(mirror ? mirror.goal - mirror.done : 2);
		})()
	);
});

/* ---------------- closed-app nudge: real push ---------------- */

self.addEventListener('push', (event) => {
	const typed = event as PushEvent;
	let payload: { title?: string; body?: string; remaining?: number } = {};
	try {
		payload = (typed.data?.json() as typeof payload) ?? {};
	} catch {
		payload = {};
	}

	typed.waitUntil(
		(async () => {
			// A push that arrives with no payload still has to decide something, so fall back to the
			// mirrored status rather than posting an empty notification.
			const remaining = payload.remaining ?? 0;
			if (payload.title) {
				await self.registration.showNotification(payload.title, {
					body: payload.body ?? '',
					tag: NUDGE_TAG,
					renotify: true,
					icon: '/icon-192.png',
					badge: '/favicon.svg',
					data: { url: '/' }
				});
				return;
			}
			const mirror = await readMirror();
			const owed = nudgeOwed(mirror, new Date());
			if (!owed && remaining <= 0) return;
			await postNudge(remaining || (mirror ? mirror.goal - mirror.done : 2));
		})()
	);
});

/* ---------------- tapping a nudge ---------------- */

self.addEventListener('notificationclick', (event) => {
	const typed = event as NotificationEvent;
	typed.notification.close();
	const target = (typed.notification.data as { url?: string } | null)?.url ?? '/';

	typed.waitUntil(
		(async () => {
			const all = await self.clients.matchAll({ type: 'window', includeUncontrolled: true });
			for (const client of all) {
				if ('focus' in client) {
					await client.focus();
					if ('navigate' in client) await (client as WindowClient).navigate(target);
					return;
				}
			}
			if (self.clients.openWindow) await self.clients.openWindow(target);
		})()
	);
});
