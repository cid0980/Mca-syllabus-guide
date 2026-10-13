"""Module IV of CSCA 411 - three questions added per card."""

CODE = "CSCA411"

ADD = {
	# ---- 01. Divide and conquer: general method ----
	"CSCA411-M4-01": [
		{
			"q": "Which statement about the divide and conquer method is NOT correct?",
			"options": [
				"A problem is split into smaller instances of the same problem",
				"Recursion expresses the method naturally",
				"The cost is written as a recurrence relation",
				"Splitting into halves makes the recursion depth n",
			],
			"answer": 3,
			"why": "Halving the problem at every step reaches the base case after about log n steps, not n, and that is why the method is cheap.",
		},
		{
			"q": "You must find the heaviest student in a class of 100. How does divide and conquer approach it?",
			"options": [
				"Split into halves, find each half's heaviest, compare the two",
				"Compare every student's weight with every other student's",
				"Sort the class by weight and then read the last entry",
				"Ask each student once and stop after the first answer",
			],
			"answer": 0,
			"why": "Each half is a smaller copy of the same job, and combining the two answers costs just one comparison.",
		},
		{
			"q": "An algorithm has the recurrence T(n) = 2T(n/2) + n. How many levels deep does the recursion go?",
			"options": [
				"About log base 2 of n levels, halving each time",
				"About n levels, one level for each element",
				"About n/2 levels, one level for each pair",
				"Two levels only, the left half and the right half",
			],
			"answer": 0,
			"why": "The problem size halves at every level, so the base case is reached after about log base 2 of n levels.",
		},
	],
	# ---- 02. Binary search as divide and conquer ----
	"CSCA411-M4-02": [
		{
			"q": "Which statement about binary search is NOT correct?",
			"options": [
				"It compares the key with the middle element",
				"It discards the half that cannot hold the key",
				"It works on an unsorted array if it is scanned twice",
				"The recursive version pays extra function call overhead",
			],
			"answer": 2,
			"why": "Halving only makes sense on sorted data; on an unsorted array binary search returns wrong answers instead of reporting a problem.",
		},
		{
			"q": "Binary search is run by mistake on an array that was never sorted. What happens?",
			"options": [
				"It may return a wrong position without any error",
				"It reports that the array is not sorted",
				"It sorts the array first and then searches",
				"It becomes slower but stays perfectly correct",
			],
			"answer": 0,
			"why": "The comparison only knows which half to drop, so unsorted data gives false guidance and a silently wrong answer.",
		},
		{
			"q": "Starting from 1,000 items, how many items remain after three comparisons of binary search?",
			"options": [
				"About 125, because each step halves what is left",
				"About 500, because only the first half is dropped",
				"About 1,000, because nothing is ever removed",
				"About 250, because only two halvings have happened",
			],
			"answer": 0,
			"why": "1,000 halves to 500, then to 250, then to 125, which is why the search needs about log base 2 of n comparisons in total.",
		},
	],
	# ---- 03. Merge sort ----
	"CSCA411-M4-03": [
		{
			"q": "Which statement about merge sort is NOT correct?",
			"options": [
				"It splits the array in half and sorts each half recursively",
				"Merging two sorted lists takes linear time",
				"Its worst case is much worse than its average case",
				"It needs an extra array while merging",
			],
			"answer": 2,
			"why": "Merge sort splits exactly at the middle every time, so every case costs O(n log n) and there is no bad input.",
		},
		{
			"q": "Two teachers sort half of the answer sheets each. What does the merge step do, and what does it cost?",
			"options": [
				"It compares the two front sheets repeatedly, in linear time",
				"It compares every pair of sheets, in quadratic time",
				"It re-sorts the combined pile from the beginning",
				"It leaves the two sorted piles separate at the end",
			],
			"answer": 0,
			"why": "Each comparison removes one sheet from the front of a pile, so merging n sheets together takes about n comparisons.",
		},
		{
			"q": "How many levels of splitting does merge sort need for an array of 64 items?",
			"options": ["6 levels", "64 levels", "32 levels", "8 levels"],
			"answer": 0,
			"why": "64 halves to 1 in six steps, since 2 raised to 6 is 64, and that is why merge sort has log n levels.",
		},
	],
	# ---- 04. Quick sort ----
	"CSCA411-M4-04": [
		{
			"q": "Which statement about quick sort is NOT correct?",
			"options": [
				"Partitioning leaves the pivot in its final sorted position",
				"A bad pivot can make the recursion depth as large as n",
				"Its worst case is better than the worst case of merge sort",
				"A random pivot makes the bad case unlikely in practice",
			],
			"answer": 2,
			"why": "Quick sort's worst case is O(n squared) while merge sort stays O(n log n) in every case, so quick sort's worst case is worse.",
		},
		{
			"q": "The array is already sorted and the code always picks the last element as pivot. What is the result?",
			"options": [
				"Partitions of size 0 and n - 1, degrading to O(n squared)",
				"Perfectly even partitions, giving O(n log n) work",
				"The array is sorted with almost no comparisons at all",
				"Quick sort notices this and switches to merge sort",
			],
			"answer": 0,
			"why": "The last element of a sorted array is its largest, so every partition is empty on one side and the depth becomes n.",
		},
		{
			"q": "Partitioning 100 elements costs about 100 comparisons. About how much do the two halves then cost together?",
			"options": [
				"About 100 more, because every level costs n",
				"About 10,000, because the halves are squared",
				"About 50, because the two halves are smaller",
				"Nothing more, because the pivot is already placed",
			],
			"answer": 0,
			"why": "Each level of recursion partitions the whole set once, so the work per level stays about n and the total becomes n times the depth.",
		},
	],
	# ---- 05. Analysis of recursive algorithms and recurrences ----
	"CSCA411-M4-05": [
		{
			"q": "Which statement about analysing recurrences is NOT correct?",
			"options": [
				"A recurrence states the cost of a recursive algorithm",
				"Back substitution expands the recurrence and sums it",
				"The recursion tree adds up the cost level by level",
				"The master theorem applies only to non-recursive code",
			],
			"answer": 3,
			"why": "The master theorem solves recurrences of the form T(n) = aT(n/b) + f(n), so it is a tool for recursive algorithms.",
		},
		{
			"q": "Merge sort does n work on every level of its recursion tree and there are log n levels. What is the total cost?",
			"options": [
				"n log n, because each of the log n rows costs n",
				"n squared, because the levels multiply together",
				"n, because only one level is counted",
				"log n, because only the number of levels counts",
			],
			"answer": 0,
			"why": "Adding n work over log n rows gives n log n, which is exactly what the recursion tree method is for.",
		},
		{
			"q": "Solving the recurrence T(n) = 2T(n/2) + 1 gives which complexity?",
			"options": ["O(n)", "O(1)", "O(n log n)", "O(log n)"],
			"answer": 0,
			"why": "The subproblems grow to n while the extra work stays constant, so the total follows the number of subproblems, O(n).",
		},
	],
	# ---- 06. Greedy method: general ----
	"CSCA411-M4-06": [
		{
			"q": "Which statement about the greedy method is NOT correct?",
			"options": [
				"It always takes the choice that looks best right now",
				"It never goes back and reverses a decision",
				"It is correct for every problem, including 0/1 knapsack",
				"It is fast because there is no backtracking",
			],
			"answer": 2,
			"why": "0/1 knapsack is the classic counterexample: items are indivisible, so a locally best choice can block the optimal answer.",
		},
		{
			"q": "An ATM must hand out 2,700 rupees using the fewest notes. Which approach does the card describe?",
			"options": [
				"Take the largest note that still fits, then repeat",
				"Try every possible combination of notes and pick the best",
				"Take the smallest notes until the amount runs out",
				"Halve the amount and withdraw it in two attempts",
			],
			"answer": 0,
			"why": "The greedy loop keeps taking the locally largest note that fits, and for Indian note denominations this reaches the fewest notes.",
		},
		{
			"q": "A greedy pass makes one decision for each of n items. Before any sorting, about how many decisions does it make?",
			"options": [
				"n decisions, one for each item",
				"n squared decisions, one for each pair",
				"log n decisions, halving the list each time",
				"2 raised to n decisions, one per subset",
			],
			"answer": 0,
			"why": "The greedy loop walks the items once and commits each time, which is what makes it linear before any sorting cost is added.",
		},
	],
	# ---- 07. Fractional knapsack ----
	"CSCA411-M4-07": [
		{
			"q": "Which statement about the fractional knapsack problem is NOT correct?",
			"options": [
				"Items can be cut, so a fraction of an item may be taken",
				"The greedy rule works with profit divided by weight",
				"The greedy answer is only approximate, never optimal",
				"Sorting the items by ratio is the first step",
			],
			"answer": 2,
			"why": "Because items are divisible, the exchange argument proves the ratio order is optimal, so the greedy answer here is exact.",
		},
		{
			"q": "A 5 kg bag must hold rice, dal and ghee, and ghee has the best value per kilogram. What does the greedy rule do as the bag fills up?",
			"options": [
				"Takes ghee first, and only the quantity that fits",
				"Takes equal quantities of all three items",
				"Skips ghee because only whole items may be packed",
				"Takes the cheapest item first to save money",
			],
			"answer": 0,
			"why": "The ratio order comes first and cutting is allowed, so the item that crosses the capacity line is taken in part.",
		},
		{
			"q": "An item has profit 60 and weight 4. What is its profit-to-weight ratio?",
			"options": [
				"15 per kilogram, which sorts it well",
				"56 per kilogram, the difference of the two",
				"0.067 per kilogram, the weight divided by profit",
				"240 per kilogram, the product of the two",
			],
			"answer": 0,
			"why": "The greedy criterion is profit divided by weight, and 60 divided by 4 is 15 per kilogram.",
		},
	],
	# ---- 08. Greedy algorithms on graphs ----
	"CSCA411-M4-08": [
		{
			"q": "Which statement about these three greedy graph algorithms is NOT correct?",
			"options": [
				"Prim grows one tree outward from a start vertex",
				"Kruskal uses union-find to detect cycles",
				"Dijkstra works correctly with negative edge weights",
				"All three repeatedly take the best remaining candidate",
			],
			"answer": 2,
			"why": "Dijkstra finalises a distance as soon as it is the closest, and a negative edge arriving later can still beat it.",
		},
		{
			"q": "You must find the fastest route from the hostel to the department on a road map carrying travel times. Which algorithm fits?",
			"options": [
				"Dijkstra's, because it finds shortest paths from one source",
				"Prim's, because it grows a tree across the map",
				"Kruskal's, because it sorts the roads by weight",
				"Either Prim's or Kruskal's, since both find routes",
			],
			"answer": 0,
			"why": "A single source with weighted edges and a destination is exactly the shortest path problem Dijkstra's algorithm solves.",
		},
		{
			"q": "Kruskal's algorithm sorts the edges before scanning them. For 300 edges, about how many comparisons does a good sort need?",
			"options": [
				"About 2,400, since a good sort is n log n",
				"About 300, since each edge is read once",
				"About 90,000, since every pair is compared",
				"About 8, since the depth is logarithmic",
			],
			"answer": 0,
			"why": "300 edges need about 300 times log base 2 of 300, which is roughly 2,400 comparisons, and that sorting cost dominates the algorithm.",
		},
	],
	# ---- 09. Job sequencing with deadlines ----
	"CSCA411-M4-09": [
		{
			"q": "Which statement about job sequencing with deadlines is NOT correct?",
			"options": [
				"Jobs are considered in decreasing order of profit",
				"Each job is placed as late as its deadline allows",
				"A job is dropped even when a free slot is available",
				"The result maximises the profit of the jobs finished in time",
			],
			"answer": 2,
			"why": "A job is dropped only when no free slot exists before its deadline; if a slot exists, the job is scheduled there.",
		},
		{
			"q": "Four submissions are due on different days with different credit weights. How does the greedy scan schedule them?",
			"options": [
				"Highest profit first, each as late as its deadline allows",
				"Earliest deadline first, in the order they are due",
				"Shortest job first, ignoring the credit weight",
				"Alphabetical order, filling the first free day each time",
			],
			"answer": 0,
			"why": "Profit decides the order and the latest possible slot keeps earlier slots free, which is what protects feasibility.",
		},
		{
			"q": "Two unit-time jobs both carry profit, with deadlines 1 and 2. How many can be finished in time?",
			"options": [
				"Both, because there are two slots before the deadlines",
				"Only one, because both jobs need day 1",
				"Neither, because the deadlines are too close",
				"Both, but only if they run on the same day",
			],
			"answer": 0,
			"why": "The deadline 1 job goes into slot 1 and the deadline 2 job into slot 2, so both fit before their deadlines.",
		},
	],
	# ---- 10. Huffman coding ----
	"CSCA411-M4-10": [
		{
			"q": "Which statement about Huffman coding is NOT correct?",
			"options": [
				"Frequent characters receive the shorter codes",
				"The two least frequent nodes are merged at each step",
				"Frequent characters end up deeper in the tree",
				"The code is a prefix code, so no separator is needed",
			],
			"answer": 2,
			"why": "Merging the rarest characters first pushes them deep into the tree, so frequent characters stay near the root with short codes.",
		},
		{
			"q": "In an SMS, the letter e appears far more often than q. What does Huffman coding do about that?",
			"options": [
				"It gives e a shorter code and q a longer one",
				"It gives both letters the same eight bit code",
				"It removes the rare letters from the message",
				"It gives q the shorter code because q is rarer",
			],
			"answer": 0,
			"why": "Shorter codes for frequent characters is the whole idea, and it lowers the average number of bits per character.",
		},
		{
			"q": "Five characters have frequencies 5, 7, 10, 15 and 20. Which two are merged first?",
			"options": [
				"The 5 and the 7, the two smallest",
				"The 15 and the 20, the two largest",
				"The 10 and the 15, the middle pair",
				"The 5 and the 20, the extremes",
			],
			"answer": 0,
			"why": "Huffman always merges the two lowest frequencies first, so 5 and 7 combine into a node of weight 12.",
		},
	],
}
