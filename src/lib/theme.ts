/** Subject accents are UI chrome, kept to a small fixed set so the palette stays quiet. */
const SEMESTER_TINT: Record<number, string> = {
	1: 'var(--accent)',
	2: 'var(--accent)',
	3: 'var(--accent)'
};

/** Course number badge text, e.g. "CSCA 411" -> "411". */
export function courseNumber(code: string): string {
	return code.replace(/[^0-9]/g, '');
}

export function tintFor(semester: number): string {
	return SEMESTER_TINT[semester] ?? 'var(--accent)';
}
