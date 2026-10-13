"""Module I of CSCA 411 - two or three questions added per card.

Type mix: one "which is NOT" (three true statements from the card, one false),
one short scenario, and for the numeric cards a third complexity or numeric
question. The two questions already on each card stay exactly as they are.
"""

CODE = "CSCA411"

ADD = {
	# ---- 01. Basic terminologies (conceptual) ----
	"CSCA411-M1-01": [
		{
			"q": "Which statement about data structure terms is NOT correct?",
			"options": [
				"A data item is one single value kept on its own",
				"A record is a group of related values kept together",
				"A structure is only for storing data, never for finding it",
				"Efficiency means the operations you use most are fast",
			],
			"answer": 2,
			"why": "A data structure is the arrangement plus the rules for adding, finding and removing items, so finding data is part of its job.",
		},
		{
			"q": "A team keeps student marks in a plain list and finds one student by checking from the top every time. According to the card, what is the real problem?",
			"options": [
				"The arrangement makes their most used operation slow",
				"The marks are grouped as records instead of data items",
				"The list holds more data items than memory allows",
				"The language they use has no built-in array type",
			],
			"answer": 0,
			"why": "The same data arranged differently would make the operation they repeat most take less time, and that choice is the data structure.",
		},
	],
	# ---- 02. Algorithms: definition (conceptual) ----
	"CSCA411-M1-02": [
		{
			"q": "Which of these is NOT a property that an algorithm must have?",
			"options": [
				"Finiteness, so it stops after a limited number of steps",
				"Definiteness, so every step is clear and unambiguous",
				"Effectiveness, so each step is simple enough to carry out",
				"Brevity, so it is written in the fewest possible lines",
			],
			"answer": 3,
			"why": "There is no brevity property; an algorithm may be long as long as it is finite, definite, effective and produces output.",
		},
		{
			"q": "A friend writes steps to find the largest of three numbers, but one step says only 'compare them properly'. Which property does that step break?",
			"options": [
				"Definiteness, because the step is not unambiguous",
				"Finiteness, because the steps must come to an end",
				"Input, because the numbers are already given",
				"Effectiveness, because the answer must be printed",
			],
			"answer": 0,
			"why": "Every step has to be clear enough to follow without guessing, and 'compare them properly' leaves the reader guessing.",
		},
	],
	# ---- 03. Pseudocode (conceptual) ----
	"CSCA411-M1-03": [
		{
			"q": "Which of these is NOT something pseudocode does?",
			"options": [
				"Keeps the algorithm's logic in plain readable words",
				"Uses simple keywords such as READ, WHILE and PRINT",
				"Runs on the computer without being translated first",
				"Shortens the coding stage because the thinking is done",
			],
			"answer": 2,
			"why": "Pseudocode cannot be executed directly; it is a plan that you translate into a language such as C++ or Java later.",
		},
		{
			"q": "You must show the logic of a payroll program to a teacher who does not know Java. What should you hand over?",
			"options": [
				"Pseudocode using plain steps and simple keywords",
				"The complete Java source with comments added",
				"Only the final printed output of the program",
				"A list of the input files the program reads",
			],
			"answer": 0,
			"why": "Pseudocode keeps the logic and drops the strict grammar, so a reader who does not know Java can still check the steps.",
		},
	],
	# ---- 04. Time complexity (numeric) ----
	"CSCA411-M1-04": [
		{
			"q": "Which statement about time complexity is NOT correct?",
			"options": [
				"It counts basic operations as a function of input size",
				"It is the stopwatch time measured on the lab computer",
				"It shows how the work grows as the data becomes large",
				"A smaller growth rate survives a large input better",
			],
			"answer": 1,
			"why": "Stopwatch time changes with every machine; time complexity counts operations against n so the comparison is portable.",
		},
		{
			"q": "Your teacher raises the test data from 1,000 to 10,000 records and the running time grows about a hundred times. What does that show?",
			"options": [
				"The work grows with the square of the input size",
				"The work grows in a straight line with the input",
				"The work stays the same for every input size",
				"The work grows more slowly than the input",
			],
			"answer": 0,
			"why": "Ten times the input producing a hundred times the work is the n squared pattern, not a linear one.",
		},
		{
			"q": "An algorithm always performs 4n + 20 basic operations. About how many operations does it perform for n = 100?",
			"options": ["About 420", "About 120", "About 4,020", "About 10,400"],
			"answer": 0,
			"why": "4 x 100 + 20 = 420; the growth is written O(n), but the actual count still uses the real expression.",
		},
	],
	# ---- 05. Space complexity (numeric) ----
	"CSCA411-M1-05": [
		{
			"q": "Which of these is NOT counted as auxiliary space?",
			"options": [
				"A temporary array created while sorting the input",
				"A second list built while merging two sorted lists",
				"One small variable used to swap two values",
				"The memory holding the input array itself",
			],
			"answer": 3,
			"why": "Auxiliary space is the extra working memory beyond the input, so the input array is not part of it.",
		},
		{
			"q": "You must merge two sorted lists of 500 names each into a new list without touching the originals. What is the extra memory cost?",
			"options": [
				"A second list of about 1,000 names, O(n) auxiliary",
				"One temporary variable only, so O(1) auxiliary",
				"No extra memory, because both lists are sorted",
				"About half a list, so O(n/2) auxiliary space",
			],
			"answer": 0,
			"why": "Building a new merged list needs a second list as large as the total input, which is O(n) auxiliary space.",
		},
		{
			"q": "An algorithm uses exactly three extra variables whatever the input size. How is its auxiliary space written?",
			"options": [
				"O(1), a constant amount of extra memory",
				"O(n), because extra memory grows with input",
				"O(3n), because it keeps three variables",
				"O(log n), because the variables are small",
			],
			"answer": 0,
			"why": "A fixed three variables never grow with n, so the auxiliary space is constant, O(1), which makes the algorithm in-place.",
		},
	],
	# ---- 06. Efficiency: best, average, worst (numeric) ----
	"CSCA411-M1-06": [
		{
			"q": "Which statement about the three cases is NOT correct?",
			"options": [
				"Best case is the luckiest input and worst the unluckiest",
				"Worst case is reported because it is a guarantee",
				"Average case is the typical input seen in practice",
				"Comparing algorithms means comparing code length",
			],
			"answer": 3,
			"why": "Algorithms are compared by growth rate, not by how short the code is; a shorter program can easily be the slower one.",
		},
		{
			"q": "Two programs solve the same problem. One is 40 lines and the other is 200 lines. How should you compare them?",
			"options": [
				"By their growth rates, not by their line counts",
				"By line count, because shorter code is always faster",
				"By the best case only, because that is the target",
				"By which language they happen to be written in",
			],
			"answer": 0,
			"why": "The card states that comparing algorithms means comparing growth rates, and code length says nothing about how the work grows.",
		},
		{
			"q": "A search on 1,000 items takes 1 comparison in the best case, about 500 on average and 1,000 in the worst case. What growth does the average case show?",
			"options": [
				"Linear growth, because the work rises with the input",
				"Constant growth, because the average never changes",
				"Quadratic growth, because the input is squared",
				"Logarithmic growth, because it halves each step",
			],
			"answer": 0,
			"why": "About n/2 comparisons is still a straight-line rise with n, so the average case of linear search is O(n).",
		},
	],
	# ---- 07. Big-O (numeric) ----
	"CSCA411-M1-07": [
		{
			"q": "Which statement about Big-O notation is NOT correct?",
			"options": [
				"It gives the upper limit of growth for a large input",
				"It drops constants, so 3n + 5 becomes O(n)",
				"It keeps the smaller terms, so n squared + 100n stays as it is",
				"O(1) is better than O(n), which is better than O(n squared)",
			],
			"answer": 2,
			"why": "Smaller terms are dropped as well, so n squared + 100n simplifies to O(n squared) because the squared term dominates.",
		},
		{
			"q": "Your program does 3n + 5 operations and your friend writes it as O(3n + 5). What should you write instead?",
			"options": [
				"O(n), because constants and lower terms are dropped",
				"O(3n), because the constant 3 has to stay",
				"O(5), because 5 is the smallest part of it",
				"O(n squared), because terms are multiplied",
			],
			"answer": 0,
			"why": "Big-O keeps only the fastest growing term with its constant removed, so 3n + 5 simplifies to O(n).",
		},
		{
			"q": "For a very large input, which of these orders needs the fewest operations?",
			"options": ["O(1)", "O(log n)", "O(n squared)", "O(n)"],
			"answer": 0,
			"why": "Constant time does not grow at all, so O(1) beats O(log n), which beats O(n), which beats O(n squared).",
		},
	],
	# ---- 08. Omega and Theta (numeric) ----
	"CSCA411-M1-08": [
		{
			"q": "Which statement about the three notations is NOT correct?",
			"options": [
				"Omega gives the least work an algorithm can do",
				"Theta is used when the two bounds have the same order",
				"Big-O is the floor and Omega is the roof of growth",
				"A function can have many upper bounds but one tight Theta",
			],
			"answer": 2,
			"why": "It is the other way round: Big-O is the roof (upper bound) and Omega is the floor (lower bound).",
		},
		{
			"q": "An algorithm performs exactly n comparisons for every input of size n. Which statement can you write?",
			"options": [
				"Theta(n), because the floor and the roof are both n",
				"Only O(1), because the work per item is fixed",
				"Only Omega(1), because the work never grows",
				"O(n squared), because that is the safest bound",
			],
			"answer": 0,
			"why": "When the lower and upper bounds have the same order, Theta pins the function from both sides: Theta(n).",
		},
		{
			"q": "An algorithm's work always lies between 2n and 5n. Which notation describes it exactly?",
			"options": [
				"Theta(n), because both bounds have the same order",
				"Theta(2n), because 2n is the lower bound",
				"Theta(5n), because 5n is the upper bound",
				"Theta(n squared), because 5n is more than n",
			],
			"answer": 0,
			"why": "Theta ignores the constants on both sides and keeps the order that both bounds share, which is n.",
		},
	],
	# ---- 09. Arrays (numeric) ----
	"CSCA411-M1-09": [
		{
			"q": "Which of these is NOT a property of an array as described on the card?",
			"options": [
				"Items of the same type sit next to each other in memory",
				"Any item is reached directly by its index number",
				"The size grows and shrinks freely while the program runs",
				"Inserting in the middle means shifting the later items",
			],
			"answer": 2,
			"why": "An array is a fixed-size block, so its size is decided in advance and the shifting cost is the price of inserting in the middle.",
		},
		{
			"q": "You keep 30 students' marks in an array and read marks[17] instantly. What makes that instant read possible?",
			"options": [
				"The address is computed from the index and element size",
				"The array keeps a sorted copy of every element",
				"The array searches itself in logarithmic steps",
				"The compiler keeps a table of every index",
			],
			"answer": 0,
			"why": "Because the elements sit next to each other, the address of arr[i] is calculated directly, so the read is constant time.",
		},
		{
			"q": "In a 2D array a[4][5] stored in row-major order, which element comes immediately after a[2][4]?",
			"options": ["a[3][0]", "a[2][5]", "a[3][4]", "a[1][4]"],
			"answer": 0,
			"why": "Row 2 ends at column 4 (5 columns means 0 to 4), so the next element is the first column of the next row, a[3][0].",
		},
	],
	# ---- 10. Searching (numeric) ----
	"CSCA411-M1-10": [
		{
			"q": "Which statement about the two searches is NOT correct?",
			"options": [
				"Linear search works on sorted and unsorted arrays",
				"Binary search throws away half the list each step",
				"Binary search needs about 17 steps for a lakh of records",
				"Linear search beats binary search on large sorted data",
			],
			"answer": 3,
			"why": "On large sorted data binary search finishes in about 17 steps while linear search may need a lakh, so linear search is slower.",
		},
		{
			"q": "You have a sorted list of 1,000 student names and must find one name quickly. What does the card recommend, and why?",
			"options": [
				"Binary search, because it needs about 10 steps",
				"Linear search, because the list is already sorted",
				"Binary search, because it also works on unsorted data",
				"Linear search, because it compares fewer items",
			],
			"answer": 0,
			"why": "Halving 1,000 items takes about 10 comparisons, which is why binary search is the choice for a large sorted list.",
		},
		{
			"q": "About how many comparisons does binary search need in the worst case for 1,024 sorted items?",
			"options": [
				"About 10, since 2 raised to 10 gives 1,024",
				"About 1,024, one comparison per item",
				"About 512, half of the list",
				"About 32, since 1,024 divided by 32 is 32",
			],
			"answer": 0,
			"why": "Binary search halves the list each step, so the worst case is log base 2 of 1,024, which is 10.",
		},
	],
}
