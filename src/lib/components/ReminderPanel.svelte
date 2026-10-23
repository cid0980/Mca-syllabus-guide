<script lang="ts">
	/**
	 * Daily reminder settings.
	 *
	 * Everything here is local: the reminder time, the goal and the repeat all live in this
	 * browser's settings. Nothing is uploaded and nothing needs an account.
	 */
	import { onMount } from 'svelte';
	import { Bell, BellRing, Send, TriangleAlert, CircleCheck } from 'lucide-svelte';
	import { settings, setReminder } from '$lib/stores/settings';
	import { hydrated } from '$lib/stores/hydrate';
	import {
		today,
		permissionState,
		notificationsSupported,
		enableReminders,
		disableReminders,
		sendTestNudge,
		registerPeriodicSync,
		slotsForDay
	} from '$lib/reminders';

	/** Called with a short message to show in the page toast. */
	export let notify: (message: string) => void;

	const GOALS = [1, 2, 3, 5];

	const REPEATS = [
		{ value: 0, label: 'Once' },
		{ value: 1, label: 'Every hour' },
		{ value: 2, label: 'Every 2 hours' },
		{ value: 3, label: 'Every 3 hours' },
		{ value: 4, label: 'Every 4 hours' }
	];

	let permission: NotificationPermission | 'unsupported' = 'default';
	let busy = false;
	/** True when the browser accepted the closed-app wake-up registration. */
	let background = false;

	onMount(() => {
		permission = permissionState();
	});

	$: cfg = $settings.reminder;
	$: supported = notificationsSupported();
	$: blocked = permission === 'denied';

	$: timeValue = `${String(cfg.hour).padStart(2, '0')}:${String(cfg.minute).padStart(2, '0')}`;

	$: slotTimes = slotsForDay(cfg, new Date()).map(
		(d) =>
			d.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' })
	);

	function onTime(event: Event) {
		const value = (event.currentTarget as HTMLInputElement).value;
		const match = /^(\d{1,2}):(\d{2})$/.exec(value);
		if (!match) return;
		const hour = Math.min(23, Math.max(0, Number(match[1])));
		const minute = Math.min(59, Math.max(0, Number(match[2])));
		setReminder({ hour, minute });
	}

	async function turnOn() {
		busy = true;
		const result = await enableReminders();
		permission = result;
		background = result === 'granted' ? await registerPeriodicSync() : false;
		busy = false;

		if (result === 'granted') notify('Daily reminder on');
		else if (result === 'denied')
			notify('Notifications are blocked. Allow them in your browser site settings, then try again.');
		else notify('This browser will not let the site notify you. The home banner still tracks your goal.');
	}

	async function onToggle(event: Event) {
		const on = (event.currentTarget as HTMLInputElement).checked;
		if (!on) {
			await disableReminders();
			background = false;
			notify('Daily reminder off');
			return;
		}
		if (permission !== 'granted') {
			await turnOn();
			return;
		}
		setReminder({ enabled: true });
		background = await registerPeriodicSync();
		notify('Daily reminder on');
	}

	async function onTest() {
		busy = true;
		const sent = await sendTestNudge();
		busy = false;
		notify(sent ? 'Test nudge sent' : 'Could not send — check notification permission');
	}
</script>

{#if !$hydrated}
	<div class="group">
		<div class="row muted">Loading your reminder settings…</div>
	</div>
{:else}
	<div class="group">
		<div class="row">
			<span class="icon"><Bell size={18} /></span>
			<span class="grow">
				<span class="row-title">Daily reminder</span>
				<span class="row-sub">
					{#if cfg.enabled}
						{cfg.goal === 1 ? '1 card a day' : `${cfg.goal} cards a day`}, nudging at {slotTimes.join(' and ')}
					{:else}
						Off. A nudge at your set time until the daily goal is met.
					{/if}
				</span>
			</span>
			<!-- the switch only reflects the stored setting; asking for permission happens on the
			     way in, so a browser prompt never appears from a passive page load -->
			<label class="switch">
				<input
					type="checkbox"
					checked={cfg.enabled}
					disabled={busy || !supported}
					on:change={onToggle}
					aria-label="Daily reminder"
				/>
				<span class="track" aria-hidden="true"><span class="knob"></span></span>
			</label>
		</div>
	</div>

	{#if !supported}
		<div class="gutter">
			<p class="note">
				<TriangleAlert size={14} />
				<span>
					This browser cannot show notifications from a website. On iPhone, add StudyFeed to your
					home screen first (Share → Add to Home Screen), then open it from there.
				</span>
			</p>
		</div>
	{:else if blocked}
		<div class="gutter">
			<p class="note warn">
				<TriangleAlert size={14} />
				<span>
					Notifications are blocked for this site. Open your browser's site settings (the padlock
					or ⓘ next to the address) and set Notifications to Allow. The reminder switch below stays
					off until then.
				</span>
			</p>
		</div>
	{:else if cfg.enabled}
		<div class="gutter panel">
			<label class="field">
				<span class="field-label">Remind me at</span>
				<input
					class="time"
					type="time"
					value={timeValue}
					on:input={onTime}
					aria-label="Reminder time"
				/>
			</label>

			<p class="field-label">Daily goal</p>
			<div class="chips">
				{#each GOALS as g}
					<button
						class="chip"
						class:on={cfg.goal === g}
						on:click={() => setReminder({ goal: g })}
						aria-pressed={cfg.goal === g}
					>
						{g} {g === 1 ? 'card' : 'cards'}
					</button>
				{/each}
			</div>

			<p class="field-label">Keep reminding</p>
			<div class="chips">
				{#each REPEATS as r}
					<button
						class="chip"
						class:on={cfg.repeatHours === r.value}
						on:click={() => setReminder({ repeatHours: r.value })}
						aria-pressed={cfg.repeatHours === r.value}
					>
						{r.label}
					</button>
				{/each}
			</div>

			<p class="status" class:done={$today.met}>
				{#if $today.met}
					<CircleCheck size={14} />
					<span>Goal met for today. No more nudges until tomorrow.</span>
				{:else}
					<BellRing size={14} />
					<span>
						{$today.done} of {cfg.goal} cards read today. Next nudge at {slotTimes[0]}{#if slotTimes.length > 1}, then again until the goal is met.{/if}
					</span>
				{/if}
			</p>

			<div class="row-actions">
				<button class="btn btn--secondary btn--sm" on:click={onTest} disabled={busy}>
					<Send size={14} /> Send a test nudge
				</button>
			</div>

			<p class="hint">
				While StudyFeed is open the nudge arrives on time. With it closed, your browser decides
				whether to wake the app, so treat that as a bonus rather than a promise — Chrome on Android
				does it for installed apps. Either way the banner on Home shows where you stand.
				{#if background}
					Background check-ins are registered on this device.
				{/if}
			</p>
		</div>
	{:else}
		<div class="gutter">
			<p class="hint">
				Turn this on and StudyFeed will ask for notification permission, then nudge you at your set
				time until you have read {cfg.goal === 1 ? 'a card' : `${cfg.goal} cards`} that day. Nothing
				leaves your device.
			</p>
		</div>
	{/if}
{/if}

<style>
	.row {
		display: flex;
		align-items: center;
		gap: var(--sp-3);
		width: 100%;
		min-height: 56px;
		padding: var(--sp-3) var(--sp-4);
		text-align: left;
	}

	.row.muted {
		color: var(--fg-subtle);
		font-size: var(--fs-small);
	}

	.icon {
		display: inline-flex;
		color: var(--fg-muted);
		flex: 0 0 auto;
	}

	.grow {
		flex: 1 1 auto;
		min-width: 0;
	}

	.row-title {
		display: block;
		font-size: var(--fs-body);
		font-weight: 600;
	}

	.row-sub {
		display: block;
		font-size: var(--fs-caption);
		line-height: 1.5;
		color: var(--fg-subtle);
		margin-top: 2px;
	}

	/* switch — sized for a thumb, and it never overlaps the label text */
	.switch {
		flex: 0 0 auto;
		display: inline-flex;
		align-items: center;
	}

	.switch input {
		position: absolute;
		opacity: 0;
		width: 1px;
		height: 1px;
		margin: 0;
	}

	.track {
		display: block;
		width: 46px;
		height: 28px;
		padding: 2px;
		border-radius: var(--radius-full);
		background: var(--fill-strong);
		transition: background var(--dur-quick) var(--ease-standard);
	}

	.knob {
		display: block;
		width: 24px;
		height: 24px;
		border-radius: var(--radius-full);
		background: #fff;
		box-shadow: 0 1px 3px rgba(0, 0, 0, 0.25);
		transition: transform var(--dur-quick) var(--ease-standard);
	}

	.switch input:checked + .track {
		background: var(--accent);
	}

	.switch input:checked + .track .knob {
		transform: translateX(18px);
	}

	.switch input:focus-visible + .track {
		outline: 2px solid var(--accent);
		outline-offset: 2px;
	}

	.switch input:disabled + .track {
		opacity: 0.4;
	}

	.panel {
		padding-top: var(--sp-4);
	}

	.field {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: var(--sp-3);
		margin-bottom: var(--sp-4);
	}

	.field-label {
		display: block;
		font-size: var(--fs-caption);
		font-weight: 700;
		letter-spacing: 0.06em;
		text-transform: uppercase;
		color: var(--fg-subtle);
		margin-bottom: var(--sp-2);
	}

	.field .field-label {
		margin-bottom: 0;
	}

	.time {
		background: var(--fill);
		border: 1px solid var(--border);
		border-radius: var(--radius);
		padding: var(--sp-2) var(--sp-3);
		font: inherit;
		font-size: var(--fs-body);
		color: var(--fg);
	}

	.chips {
		display: flex;
		flex-wrap: wrap;
		gap: var(--sp-2);
		margin-bottom: var(--sp-4);
	}

	.chip {
		padding: var(--sp-2) var(--sp-3);
		background: var(--fill);
		border: 1px solid transparent;
		border-radius: var(--radius-full);
		font-size: var(--fs-small);
		color: var(--fg-muted);
	}

	.chip.on {
		background: var(--accent);
		border-color: var(--accent);
		color: var(--accent-fg);
		font-weight: 600;
	}

	.status {
		display: flex;
		align-items: flex-start;
		gap: var(--sp-2);
		font-size: var(--fs-small);
		line-height: 1.5;
		color: var(--fg-muted);
		margin-top: var(--sp-2);
	}

	.status :global(svg) {
		flex: 0 0 auto;
		margin-top: 2px;
	}

	.status.done {
		color: var(--success);
	}

	.row-actions {
		display: flex;
		flex-wrap: wrap;
		gap: var(--sp-2);
		margin-top: var(--sp-3);
	}

	.note {
		display: flex;
		align-items: flex-start;
		gap: var(--sp-2);
		font-size: var(--fs-small);
		line-height: 1.6;
		color: var(--fg-muted);
		margin-top: var(--sp-3);
	}

	.note :global(svg) {
		flex: 0 0 auto;
		margin-top: 2px;
	}

	.note.warn {
		color: var(--warning);
	}

	.hint {
		font-size: var(--fs-caption);
		line-height: 1.6;
		color: var(--fg-subtle);
		margin-top: var(--sp-3);
	}
</style>
