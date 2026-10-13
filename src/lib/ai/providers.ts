/**
 * AI providers. Endpoints verified against current docs (Oct 2026):
 *  - Gemini  : POST generativelanguage.googleapis.com/v1beta/models/{model}:generateContent  (x-goog-api-key)
 *  - OpenRouter / NVIDIA / any OpenAI-compatible host: POST {baseUrl}/chat/completions (Bearer)
 *
 * Model ids move fast, so every provider keeps its model EDITABLE in Settings and can list its own
 * models through /api/ai/models — the app never hardcodes a model the user cannot change.
 */
export type ProviderId = 'server' | 'gemini' | 'openrouter' | 'nvidia';

export interface Provider {
	id: ProviderId;
	label: string;
	/** 'gemini' uses its own body shape; 'openai' is the chat/completions shape. */
	kind: 'gemini' | 'openai';
	keyLabel: string;
	keyHint: string;
	/** where to get a key, shown in Settings */
	console: string;
	baseUrl?: string;
	defaultModel?: string;
	needsKey: boolean;
}

export const PROVIDERS: Provider[] = [
	{
		id: 'gemini',
		label: 'Google Gemini',
		kind: 'gemini',
		keyLabel: 'API key',
		keyHint: 'starts with AIza',
		console: 'aistudio.google.com/apikey',
		defaultModel: 'gemini-3.5-flash',
		needsKey: true
	},
	{
		id: 'openrouter',
		label: 'OpenRouter',
		kind: 'openai',
		keyLabel: 'API key',
		keyHint: 'starts with sk-or-',
		console: 'openrouter.ai/settings/keys',
		baseUrl: 'https://openrouter.ai/api/v1',
		defaultModel: 'google/gemini-3.5-flash',
		needsKey: true
	},
	{
		id: 'nvidia',
		label: 'NVIDIA NIM',
		kind: 'openai',
		keyLabel: 'API key',
		keyHint: 'starts with nvapi-',
		console: 'build.nvidia.com/settings/api-keys',
		baseUrl: 'https://integrate.api.nvidia.com/v1',
		defaultModel: 'meta/llama-3.3-70b-instruct',
		needsKey: true
	},
	{
		id: 'server',
		label: 'This app\'s server',
		kind: 'openai',
		keyLabel: 'No key needed',
		keyHint: 'uses the key set in the hosting environment',
		console: '',
		needsKey: false
	}
];

export function providerById(id: ProviderId): Provider {
	return PROVIDERS.find((p) => p.id === id) ?? PROVIDERS[0];
}
