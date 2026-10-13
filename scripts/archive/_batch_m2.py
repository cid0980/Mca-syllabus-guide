"""Module II of CSCA 411 - two or three questions added per card.

Same mix as Module I: a "which is NOT", a short scenario, and a third
complexity or numeric question for the cards that carry a real count,
capacity or cost. Existing questions are untouched.
"""

CODE = "CSCA411"

ADD = {
	# ---- 01. Stack: definition and operations ----
	"CSCA411-M2-01": [
		{
			"q": "Which statement about a stack is NOT correct?",
			"options": [
				"Insertion and deletion both happen at the top end",
				"The last element added is the first one removed",
				"peek returns the top element and also removes it",
				"isFull and isEmpty are tested before push and pop",
			],
			"answer": 2,
			"why": "peek only reads the top element; removing it is the job of pop, which is why it is used to look without changing the stack.",
		},
		{
			"q": "A text editor must undo the most recent change first, every time. Which structure fits, and why?",
			"options": [
				"A stack, because the newest change is removed first",
				"A queue, because changes are removed in order",
				"An array, because changes are stored in place",
				"A linked list, because changes are searched by value",
			],
			"answer": 0,
			"why": "Undo needs last in first out, which is exactly what a stack gives when every edit is pushed and every undo pops.",
		},
		{
			"q": "A stack is kept in an array of size 10 and top is currently 9. What happens on the next push?",
			"options": [
				"Overflow, because top has already reached MAX - 1",
				"Underflow, because the stack is completely full",
				"The element at index 9 is overwritten quietly",
				"A second array is created automatically",
			],
			"answer": 0,
			"why": "The array holds indexes 0 to 9, so top == MAX - 1 means the stack is full and the next push is an overflow.",
		},
	],
	# ---- 02. Stack representation: array and linked list ----
	"CSCA411-M2-02": [
		{
			"q": "Which statement about the two stack representations is NOT correct?",
			"options": [
				"The array version keeps one integer top index",
				"The linked version pushes a node whose next pointer is the old top",
				"The array version can never overflow once the size is chosen",
				"The linked version spends one pointer for every node",
			],
			"answer": 2,
			"why": "A fixed array overflows as soon as top reaches MAX - 1, so the size must be chosen with the worst case in mind.",
		},
		{
			"q": "A canteen serves at most 50 plates in one sitting. Which representation suits the plate stack, and why?",
			"options": [
				"An array, because the maximum size is known in advance",
				"A linked list, because the count changes every sitting",
				"A linked list, because it pays no cost for pointers",
				"An array, because it grows itself once the pile is full",
			],
			"answer": 0,
			"why": "When the maximum is known, the array version is simpler and faster per operation, and it never wastes pointer memory.",
		},
		{
			"q": "For a stack stored in an array, the underflow test before pop is:",
			"options": [
				"top == -1, meaning there is nothing to remove",
				"top == 0, meaning the first cell is still free",
				"top == MAX - 1, meaning the array is full",
				"top == MAX, meaning the top left the array",
			],
			"answer": 0,
			"why": "With top starting at -1 for an empty stack, top == -1 is the signal that a pop would be an underflow.",
		},
	],
	# ---- 03. Expression conversion ----
	"CSCA411-M2-03": [
		{
			"q": "Which statement about postfix notation is NOT correct?",
			"options": [
				"The operator is written after its two operands",
				"Evaluation order is fixed by position, so brackets are not needed",
				"Every operand has to sit inside brackets to be evaluated",
				"An operator is pushed only after popping higher or equal precedence",
			],
			"answer": 2,
			"why": "Postfix works precisely because position settles the order, so brackets are unnecessary and carrying them is meaningless.",
		},
		{
			"q": "While converting the infix expression (A + B) * C, what does the closing bracket make the stack do?",
			"options": [
				"Pop the + because its opening bracket has been matched",
				"Push the * before the + can be popped",
				"Pop every operator that is still on the stack",
				"Push the bracket itself onto the output",
			],
			"answer": 0,
			"why": "A closing bracket pops operators until it meets its opening bracket, so the + goes to the output and the bracket pair is discarded.",
		},
	],
	# ---- 04. Postfix evaluation, recursion and more ----
	"CSCA411-M2-04": [
		{
			"q": "Which statement about postfix evaluation is NOT correct?",
			"options": [
				"Each operand is pushed onto the stack as it is read",
				"An operator pops two values, applies itself and pushes the result",
				"A well formed expression leaves exactly one value behind",
				"Each operator is pushed onto the stack as it is read",
			],
			"answer": 3,
			"why": "Operators are applied, not stored; only operands are pushed, and each operator consumes two values from the stack.",
		},
		{
			"q": "Ctrl+Z in a word processor restores the state before the most recent edit. Which structure is the editor using?",
			"options": [
				"A stack, because the newest edit is undone first",
				"A queue, because edits are undone as they were made",
				"A deque, because edits are undone from both ends",
				"A linked list, because edits are searched by text",
			],
			"answer": 0,
			"why": "The card's undo example is last in first out: every edit is pushed and every Ctrl+Z pops the most recent one.",
		},
		{
			"q": "Evaluate the postfix expression 8 2 / 3 + .",
			"options": ["7", "13", "3", "5"],
			"answer": 0,
			"why": "8 divided by 2 gives 4, then 4 plus 3 gives 7; both operations happen in the order the operators appear.",
		},
	],
	# ---- 05. Queue: definition and operations ----
	"CSCA411-M2-05": [
		{
			"q": "Which statement about a simple queue is NOT correct?",
			"options": [
				"Insertion happens at the rear and deletion at the front",
				"It gives first in first out service order",
				"Items can be removed from the middle when needed",
				"Nothing is removed from the middle, so it models a line",
			],
			"answer": 2,
			"why": "A queue only ever touches its two ends, which is what keeps the service order strictly first come, first served.",
		},
		{
			"q": "A system serves requests in arrival order, but its array queue is full after a few days even though requests keep finishing. What is the cause?",
			"options": [
				"The array queue wastes the space freed at the front",
				"The queue has been used as a stack by mistake",
				"The queue keeps no front pointer at all",
				"FIFO order cannot be kept in an array",
			],
			"answer": 0,
			"why": "Deletions move the front forward and leave empty cells behind it, so the rear hits the end while free space still exists in front.",
		},
		{
			"q": "An array queue of size 5 has front = 2 and rear = 4. How many items does it hold?",
			"options": [
				"3 items, at indexes 2, 3 and 4",
				"2 items, at indexes 3 and 4 only",
				"5 items, because the array is of size 5",
				"4 items, because the rear counts from the start",
			],
			"answer": 0,
			"why": "The queue runs from the front to the rear inclusive, so indexes 2, 3 and 4 hold three items.",
		},
	],
	# ---- 06. Circular queue ----
	"CSCA411-M2-06": [
		{
			"q": "Which statement about a circular queue is NOT correct?",
			"options": [
				"The rear wraps to the beginning using modulo arithmetic",
				"It reuses the cells that deletions freed at the front",
				"It removes the need to keep one slot empty",
				"It keeps the same first in first out order as a plain queue",
			],
			"answer": 2,
			"why": "Full and empty would otherwise look identical, so one slot is deliberately left empty to tell the two states apart.",
		},
		{
			"q": "In a circular queue the rear sits at the last index. Where does the very next enqueue write?",
			"options": [
				"At index 0, because the rear wraps around",
				"At the last index again, overwriting it",
				"At the index after the front, then stop",
				"Nowhere, because the rear has left the array",
			],
			"answer": 0,
			"why": "The modulo step sends the rear back to index 0 once it passes the end, which is what makes the array behave like a ring.",
		},
		{
			"q": "A circular queue of size 5 has front = 3 and rear = 0 after wrapping. Where does the next enqueue write?",
			"options": [
				"Index 1, because the rear moves on by one modulo 5",
				"Index 0, overwriting the element at the rear",
				"Index 3, because that cell is empty now",
				"Index 4, because the array ends there",
			],
			"answer": 0,
			"why": "The rear advances with (rear + 1) % n, so 0 becomes 1, and the cell at index 3 is not touched because only the rear moves.",
		},
	],
	# ---- 07. Priority queue and deque ----
	"CSCA411-M2-07": [
		{
			"q": "Which statement about a priority queue is NOT correct?",
			"options": [
				"It removes the element with the highest priority",
				"Every element is stored with a priority value",
				"It always removes the oldest element, exactly like a queue",
				"A heap is the standard efficient implementation",
			],
			"answer": 2,
			"why": "Priority decides the order, so an urgent job can overtake older ones, which is why a priority queue is not FIFO at all.",
		},
		{
			"q": "In an emergency room, a critical patient arrives after several minor cases. Who is treated first, and what does that show?",
			"options": [
				"The critical patient, because removal is by priority",
				"The minor cases, because they arrived earlier",
				"The critical patient, because a queue removes the last arrival",
				"No one, because a queue cannot hold priority values",
			],
			"answer": 0,
			"why": "This is the card's own example: a priority queue serves the element with the highest priority rather than the oldest one.",
		},
		{
			"q": "A heap-backed priority queue holds 1,000 items. About how many steps do insert and remove take?",
			"options": [
				"About 10, because a heap works in logarithmic steps",
				"About 1,000, because every item is compared",
				"About 500, because half the items are kept",
				"About 1, because the root is always known",
			],
			"answer": 0,
			"why": "Keeping the extreme value at the root gives O(log n) work, and log base 2 of 1,000 is about 10.",
		},
	],
	# ---- 08. Applications of queues ----
	"CSCA411-M2-08": [
		{
			"q": "Which of these is NOT a queue application?",
			"options": [
				"CPU scheduling of runnable processes",
				"Printer spooling of pending documents",
				"Breadth first search of a graph",
				"Undo history inside a text editor",
			],
			"answer": 3,
			"why": "Undo history is last in first out, so it belongs to a stack; the other three all handle jobs in arrival order.",
		},
		{
			"q": "A graph must be explored level by level, finishing all neighbours of the start node before going deeper. Which structure does that, and why?",
			"options": [
				"A queue, because nodes are processed in arrival order",
				"A stack, because the newest node is processed first",
				"A priority queue, because nodes carry weights",
				"An array, because the graph is stored by index",
			],
			"answer": 0,
			"why": "Processing in arrival order keeps each level complete before the next one starts, which is why breadth first search is built on a queue.",
		},
	],
	# ---- 09. Linked list: definition and node structure ----
	"CSCA411-M2-09": [
		{
			"q": "Which statement about a linked list is NOT correct?",
			"options": [
				"Nodes are scattered in memory and joined by pointers",
				"Each node stores a value and a pointer to the next node",
				"Any element can be read in one step, exactly as in an array",
				"Reaching the k-th node means walking k links from the head",
			],
			"answer": 2,
			"why": "Only the head is known, so there is no direct address arithmetic and a position must be reached by walking the links.",
		},
		{
			"q": "After weeks of use, free memory is scattered in small pieces. Why can a linked list still hold 10,000 records without moving any of them?",
			"options": [
				"Each node goes wherever space is free and pointers join them",
				"The list reserves one large block of memory in advance",
				"The list sorts the nodes back into order after each change",
				"The list stores only the head and rebuilds the rest on demand",
			],
			"answer": 0,
			"why": "Nodes do not have to sit next to each other, so scattered free space is fine and only the pointers need rewriting.",
		},
		{
			"q": "How many links must be followed to reach the 5th node from the head?",
			"options": ["4 links", "5 links", "3 links", "1 link"],
			"answer": 0,
			"why": "The head is the 1st node, so four hops over four links land on the 5th node.",
		},
	],
	# ---- 10. Singly, doubly and circular linked lists ----
	"CSCA411-M2-10": [
		{
			"q": "Which statement about the forms of linked list is NOT correct?",
			"options": [
				"A singly linked list can only be traversed forward",
				"A doubly linked list stores a previous pointer as well",
				"A circular linked list ends with NULL in its last node",
				"Round robin scheduling suits a circular linked list",
			],
			"answer": 2,
			"why": "The last node of a circular list points back to the first node instead of holding NULL, which is what closes the ring.",
		},
		{
			"q": "A music player must support next and previous, and deleting the current song should not mean walking from the start. Which form fits?",
			"options": [
				"A doubly linked list, because the previous pointer is there",
				"A singly linked list, because it saves a pointer per song",
				"A circular list, because it never reaches an end",
				"An array, because songs are reached by position",
			],
			"answer": 0,
			"why": "Carrying a previous pointer gives backward movement and constant-time deletion once the node is known, which is the two things asked for.",
		},
		{
			"q": "How many pointer fields does a node of a doubly linked list carry?",
			"options": [
				"Two, one to the next node and one to the previous",
				"One, pointing to the next node only",
				"Three, one for each direction and one to the head",
				"None, because the list keeps an index array",
			],
			"answer": 0,
			"why": "The extra previous pointer is exactly the memory cost that buys backward traversal and O(1) deletion.",
		},
	],
	# ---- 11. Linked list operations and their complexity ----
	"CSCA411-M2-11": [
		{
			"q": "Which statement about the cost of linked list operations is NOT correct?",
			"options": [
				"Inserting at the front of the list is constant time",
				"Deleting a known node is constant time in a doubly linked list",
				"Searching for a value by comparison is constant time",
				"Finding the predecessor is the costly part in a singly linked list",
			],
			"answer": 2,
			"why": "A search has to walk the links until the value appears, so it costs O(n) even though the deletion that follows may be O(1).",
		},
		{
			"q": "Your program deletes a given roll number from a long singly linked list. What is the dominant cost?",
			"options": [
				"Walking from the head to find its predecessor",
				"Shifting all later records one place left",
				"Copying the whole list into a new array",
				"Recounting the length of the list every time",
			],
			"answer": 0,
			"why": "Pointer surgery itself is cheap; the expensive part is the traversal that locates the node before it, which is why a doubly linked list helps.",
		},
		{
			"q": "A singly linked list holds 1,000 nodes. About how many nodes must be visited to insert a new node after node 900?",
			"options": [
				"About 900, walking from the head to that node",
				"About 100, counting backwards from the end",
				"About 10, using binary halving steps",
				"1, because insertion is always constant time",
			],
			"answer": 0,
			"why": "Insertion is only constant time at the front; reaching a particular position needs the walk from the head, about 900 nodes here.",
		},
	],
	# ---- 12. Applications, arrays versus linked lists ----
	"CSCA411-M2-12": [
		{
			"q": "Which statement about choosing between arrays and linked lists is NOT correct?",
			"options": [
				"A linked list never has to move its elements",
				"An array gives direct access to any index",
				"A linked list uses less memory per element than an array",
				"Linked lists suit collections whose size changes often",
			],
			"answer": 2,
			"why": "Every node pays for a pointer field, so a linked list uses more memory per element than an array of the same values.",
		},
		{
			"q": "A polynomial has 12 non-zero terms out of 500 possible powers. Why is a linked list the better store?",
			"options": [
				"Only the non-zero terms are stored, saving memory",
				"Linked lists always answer lookups faster than arrays",
				"Arrays cannot store more than ten terms in a row",
				"Linked lists sort the terms automatically as they arrive",
			],
			"answer": 0,
			"why": "Storing only the terms that exist avoids 488 empty slots, which is exactly the sparse-data case the card names.",
		},
		{
			"q": "An array of 1,000 integers and a linked list of 1,000 nodes hold the same values. Which one needs more memory?",
			"options": [
				"The linked list, because every node stores a pointer",
				"The array, because it keeps its values side by side",
				"Both need exactly the same amount of memory",
				"Neither, because both hold plain numbers only",
			],
			"answer": 0,
			"why": "The linked list carries one extra pointer per element, which is the memory trade-off accepted for not moving data.",
		},
	],
}
