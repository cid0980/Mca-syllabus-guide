/**
 * Short labels for the course circles.
 *
 * The subject code stays next to these circles everywhere it matters, so the circle itself says
 * what the subject actually is: DSA instead of 411. One map, used by every screen that draws a
 * course circle, so the labels can never drift apart.
 *
 * Keep these to five characters or fewer - the circle is 36px wide with an 11px label.
 */
const SHORT: Record<string, string> = {
	'CSCA 411': 'DSA', // Data Structures and Algorithms
	'CSCA 412': 'OOP', // Object Oriented Programming
	'CSCA 413': 'DBMS', // Database Management Systems
	'CSCA 431': 'Maths', // Mathematics for Computer Science
	'CSCA 421': 'CN', // Computer Networks
	'CSCA 422': 'OS', // Operating Systems
	'CSCA 423': 'Comm', // Communication Skills
	'CSCA 432': 'Mgmt', // Management Concepts and Strategies
	'CSCA 511': 'SE', // Software Engineering
	'CSCA 512': 'IWT' // Internet and Web Technologies
};

/** Short circle label for a subject code. Unknown codes fall back to the digits ("411"). */
export function shortName(code: string): string {
	return SHORT[code] ?? code.replace(/^[A-Z]{4}\s*/, '');
}
