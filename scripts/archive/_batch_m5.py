"""Module V of CSCA 411 - three questions added per card."""

CODE = "CSCA411"

ADD = {
	# ---- 01. Dynamic programming: general method ----
	"CSCA411-M5-01": [
		{
			"q": "Which statement about dynamic programming is NOT correct?",
			"options": [
				"It stores answers to overlapping subproblems",
				"Memoization is top-down and tabulation bottom-up",
				"It recomputes every state each time it is needed",
				"It spends memory on the table to avoid repeated work",
			],
			"answer": 2,
			"why": "Each state is computed once and looked up afterwards, which is what turns exponential recursion into polynomial time.",
		},
		{
			"q": "You must count the ways to climb 10 steps taking 1 or 2 steps at a time. What does dynamic programming do differently from plain recursion?",
			"options": [
				"It stores the counts for smaller steps and reuses them",
				"It tries every order of steps again from the beginning",
				"It guesses a pattern and multiplies it out",
				"It converts the count into a greedy choice",
			],
			"answer": 0,
			"why": "The counts for step 8 and step 9 are needed repeatedly, so caching them removes the exponential repetition of plain recursion.",
		},
		{
			"q": "A dynamic programming table has one state for each item and each capacity. For 5 items and capacity 10, how many states are there?",
			"options": [
				"50 states, because every item is paired with every capacity",
				"15 states, because items and capacities are added",
				"32 states, one for every subset of items",
				"100 states, because the items are squared",
			],
			"answer": 0,
			"why": "The table is the product of the two dimensions, so 5 items across 10 capacities gives 50 states, written O(nW).",
		},
	],
	# ---- 02. 0/1 knapsack using dynamic programming ----
	"CSCA411-M5-02": [
		{
			"q": "Which statement about the 0/1 knapsack problem is NOT correct?",
			"options": [
				"Each item is taken whole or left behind",
				"The state records the best profit for the first i items and capacity w",
				"Greedy order by profit-to-weight ratio is always optimal here",
				"The table is filled row by row and the last cell holds the answer",
			],
			"answer": 2,
			"why": "Ratio greedy is optimal only in the fractional version; with indivisible items a good ratio can block a better combination.",
		},
		{
			"q": "Items weigh 2, 2 and 3 kg with values 4, 5 and 6, and the bag holds 4 kg. Why can the bag not be filled to exactly 4 kg?",
			"options": [
				"Because an item may not be cut into a fraction",
				"Because the three values are all different",
				"Because the table needs a fifth column",
				"Because the capacity must be an even number",
			],
			"answer": 0,
			"why": "The 0/1 rule allows only whole items, so 2 + 2 = 4 kg is used and the 3 kg item cannot be split to top up the last kilogram.",
		},
		{
			"q": "A knapsack table is built with one row per item and one column per capacity, for 4 items and capacity 8. How many cells does that give?",
			"options": [
				"32 cells, four rows of eight",
				"12 cells, four plus eight",
				"64 cells, because the size is squared",
				"16 cells, one for every subset",
			],
			"answer": 0,
			"why": "Rows times columns gives 4 times 8, which is 32 cells, and that count is exactly why the algorithm is O(nW).",
		},
	],
	# ---- 03. Travelling salesman problem ----
	"CSCA411-M5-03": [
		{
			"q": "Which statement about the travelling salesman problem is NOT correct?",
			"options": [
				"The tour visits every city once and returns to the start",
				"Brute force checks about (n - 1) factorial tours",
				"Dynamic programming solves it in polynomial time",
				"No polynomial time algorithm is known for it",
			],
			"answer": 2,
			"why": "Dynamic programming shrinks the search to states of current city plus visited set, but that is still exponential, so TSP stays NP-hard.",
		},
		{
			"q": "A delivery van must visit twelve shops and return to the depot. Why is comparing every possible order useless in practice?",
			"options": [
				"Twelve cities mean billions of tours to compare",
				"Twelve cities cannot fit in the computer's memory",
				"The depot cannot be visited again at the end",
				"Routes must be arranged alphabetically, not cheapest",
			],
			"answer": 0,
			"why": "The number of tours grows factorially, so eleven factorial orders is in the billions even for a small map.",
		},
		{
			"q": "For 5 cities, about how many distinct tours does brute force have to check?",
			"options": [
				"24, because it is 4 factorial",
				"5, one tour starting from each city",
				"120, because it is 5 factorial",
				"10, because each pair of cities is counted once",
			],
			"answer": 0,
			"why": "The starting city is fixed, so the remaining 4 cities can be ordered in 4 factorial ways, which is 24 tours.",
		},
	],
	# ---- 04. Backtracking: general method ----
	"CSCA411-M5-04": [
		{
			"q": "Which statement about backtracking is NOT correct?",
			"options": [
				"It builds a solution one component at a time",
				"A partial solution is abandoned as soon as it cannot work",
				"It explores the state space tree breadth first",
				"Its worst case is still exponential without pruning",
			],
			"answer": 2,
			"why": "Backtracking is depth first search over partial solutions; going breadth first would lose the undo-the-last-choice behaviour it relies on.",
		},
		{
			"q": "While filling a sudoku you place a digit that breaks a box rule. What does backtracking do next?",
			"options": [
				"Erases that digit and tries the next one",
				"Fills the whole grid and fixes mistakes at the end",
				"Starts the grid again from the first cell",
				"Leaves the cell empty and moves on for good",
			],
			"answer": 0,
			"why": "The violated constraint prunes that branch immediately, so the choice is undone and the next value is tried - the backtrack.",
		},
		{
			"q": "A state space tree has two choices at every step and a depth of 10. About how many nodes exist if nothing is pruned?",
			"options": [
				"About 1,000, since 2 raised to 10 is 1,024",
				"About 20, two choices per level",
				"About 100, ten levels of ten branches",
				"About 10, one node per level",
			],
			"answer": 0,
			"why": "Unpruned branching doubles at every level, so ten levels give roughly a thousand nodes, which is why pruning matters.",
		},
	],
	# ---- 05. n-Queen problem ----
	"CSCA411-M5-05": [
		{
			"q": "Which statement about the n-Queen problem is NOT correct?",
			"options": [
				"No two queens may share a row, a column or a diagonal",
				"Queens are placed one row at a time during backtracking",
				"A solution is written by listing the row of each queen",
				"When a row has no safe column, the previous row is undone",
			],
			"answer": 2,
			"why": "A solution is written as a tuple of column numbers, one per row, which makes the row constraint free.",
		},
		{
			"q": "While placing queens you reach row 4 and find every column attacked. What does the algorithm do?",
			"options": [
				"Undoes the placement in row 3 and tries another column there",
				"Places the queen in an attacked column anyway",
				"Restarts the board from row 1 in a new order",
				"Stops, because it has proved that no solution exists",
			],
			"answer": 0,
			"why": "A dead end in one row means the previous choice was wrong, so it is undone and the next alternative is tried.",
		},
		{
			"q": "In the 4-Queens problem, one queen is placed in each row. How many ways are there to assign the columns before any diagonal check?",
			"options": [
				"24, because the four columns can be ordered in 4 factorial ways",
				"4, because there are four rows to fill",
				"16, because it is four rows of four squares",
				"256, because every square is chosen independently",
			],
			"answer": 0,
			"why": "One queen per row means the four distinct columns can be permuted in 4 factorial = 24 ways, and the diagonal rules cut that down to 2.",
		},
	],
	# ---- 06. Graph colouring problem ----
	"CSCA411-M5-06": [
		{
			"q": "Which statement about graph colouring is NOT correct?",
			"options": [
				"No two adjacent vertices may share a colour",
				"The chromatic number is the minimum number of colours needed",
				"Adjacent vertices may share a colour if they are far apart",
				"Deciding whether three colours are enough is NP-complete",
			],
			"answer": 2,
			"why": "Sharing a colour is forbidden exactly when two vertices are adjacent, and distance on the page has nothing to do with it.",
		},
		{
			"q": "Courses that share students must not be held in the same slot. What does each time slot represent?",
			"options": [
				"A colour, with clashing courses as adjacent vertices",
				"A vertex, with lecture halls as the edges",
				"An edge weight, counting the shared students",
				"The chromatic number of the timetable",
			],
			"answer": 0,
			"why": "This is the card's own example: slots behave like colours and two courses that cannot clash are joined by an edge.",
		},
		{
			"q": "A graph joins every pair of its 5 vertices, so every pair is adjacent. How many colours does a proper colouring need?",
			"options": [
				"5, because no two vertices may share a colour",
				"1, because one colour covers all five vertices",
				"2, because every complete graph is bipartite",
				"10, because there are ten edges to colour",
			],
			"answer": 0,
			"why": "In a complete graph every vertex touches every other, so each one needs its own colour and the chromatic number equals the vertex count.",
		},
	],
	# ---- 07. Complexity classes: P and NP ----
	"CSCA411-M5-07": [
		{
			"q": "Which statement about the classes P and NP is NOT correct?",
			"options": [
				"P contains the problems solvable in polynomial time",
				"NP allows easy verification even when solving is hard",
				"P is known to be a strictly smaller class than NP",
				"Verifying a solution is never harder than finding one",
			],
			"answer": 2,
			"why": "Whether P equals NP is still open; all we know for certain is that P is contained in NP.",
		},
		{
			"q": "A classmate hands you a finished jigsaw and you can see at once that it fits together. What does that show about NP?",
			"options": [
				"Checking an answer can be easy even if finding it was hard",
				"Solving must be just as easy as checking",
				"The problem cannot be solved by any algorithm",
				"The problem is in P but not in NP",
			],
			"answer": 0,
			"why": "This is the card's own picture of NP: verification is cheap even when the search that produced the answer was expensive.",
		},
		{
			"q": "Sorting n numbers with a good algorithm costs n log n comparisons. Which class does that place sorting in?",
			"options": [
				"P, because n log n is polynomial time",
				"NP-hard, because sorting uses comparisons",
				"Neither P nor NP, because it is a sorting task",
				"NP-complete, because everything reduces to it",
			],
			"answer": 0,
			"why": "Polynomial time solvability is the definition of P, and n log n grows more slowly than n squared.",
		},
	],
	# ---- 08. NP-hard and NP-complete problems ----
	"CSCA411-M5-08": [
		{
			"q": "Which statement about NP-hard and NP-complete problems is NOT correct?",
			"options": [
				"Every NP problem reduces to an NP-hard problem",
				"A problem in NP that is NP-hard is NP-complete",
				"An NP-hard problem must itself belong to NP",
				"Reduction is the tool used to prove other problems hard",
			],
			"answer": 2,
			"why": "NP-hard problems need not be in NP at all; only when they are also in NP do they earn the name NP-complete.",
		},
		{
			"q": "A college must build a clash-free timetable. Why do colleges use heuristics instead of an exact answer?",
			"options": [
				"The problem is NP-complete, so a good schedule is used",
				"The problem is in P, so heuristics are merely faster",
				"Timetables have no constraints left to check",
				"Heuristics always return the optimal timetable",
			],
			"answer": 0,
			"why": "Timetabling is NP-complete, so colleges settle for schedules that are good rather than provably optimal.",
		},
		{
			"q": "An NP-complete problem is reduced to a new problem in polynomial time. What does that prove about the new problem?",
			"options": [
				"It is NP-hard, because every NP problem reduces to it",
				"It is in P, because the reduction itself runs quickly",
				"It has no solution under any circumstances",
				"It is easier than the problem it came from",
			],
			"answer": 0,
			"why": "A reduction from a known hard problem carries the hardness across, so the new problem is NP-hard and NP-complete if it is also in NP.",
		},
	],
}
