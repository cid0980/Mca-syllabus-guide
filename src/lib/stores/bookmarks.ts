/** Saved cards. key `sf:bookmarks` -> string[] of node ids, newest first. */
import { browser } from '$app/environment';
import { get, writable } from 'svelte/store';
import { KEYS, readJSON, writeJSON } from '$lib/storage';

export const bookmarks = writable<string[]>([]);

let ready = false;

export function initBookmarks(): void {
	if (!browser || ready) return;
	ready = true;
	bookmarks.set(readJSON<string[]>(KEYS.bookmarks, []));
	let saveTimer: ReturnType<typeof setTimeout> | undefined;
	bookmarks.subscribe((v) => {
		clearTimeout(saveTimer);
		saveTimer = setTimeout(() => writeJSON(KEYS.bookmarks, v), 200);
	});
}

export function isBookmarked(id: string, list: string[] = get(bookmarks)): boolean {
	return list.includes(id);
}

export function toggleBookmark(id: string): boolean {
	let added = false;
	bookmarks.update((list) => {
		if (list.includes(id)) return list.filter((x) => x !== id);
		added = true;
		return [id, ...list];
	});
	return added;
}

export function clearBookmarks(): void {
	bookmarks.set([]);
}
