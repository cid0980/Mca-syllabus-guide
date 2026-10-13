"""Module III of CSCA 411 - three questions added per card.

Every topic in this module carries a real count, height or cost, so all eleven
cards get the "which is NOT", the scenario and the numeric question.
"""

CODE = "CSCA411"

ADD = {
	# ---- 01. Tree terminology ----
	"CSCA411-M3-01": [
		{
			"q": "Which statement about tree terminology is NOT correct?",
			"options": [
				"Every node except the root has exactly one parent",
				"A node that has no children at all is called a leaf",
				"A tree with n nodes always contains n edges",
				"The degree of a node counts its children",
			],
			"answer": 2,
			"why": "A tree with n nodes has exactly n - 1 edges, which is the fact numerical questions in this topic are built on.",
		},
		{
			"q": "Your college chart runs Vice Chancellor, then Deans, then Heads of Department, then faculty. Which node is the root, and how do the edges compare with the nodes?",
			"options": [
				"The Vice Chancellor, and edges are one fewer than nodes",
				"The faculty, and edges equal the number of nodes",
				"The Deans, and edges are twice the number of nodes",
				"Any node, because a tree has no fixed root",
			],
			"answer": 0,
			"why": "The top of the hierarchy is the root and it has no parent, and every tree with n nodes carries n - 1 edges.",
		},
		{
			"q": "A tree contains 15 nodes. How many edges does it have?",
			"options": ["14", "15", "16", "30"],
			"answer": 0,
			"why": "One edge leads into every node except the root, so 15 nodes give 14 edges.",
		},
	],
	# ---- 02. Binary tree and its representation ----
	"CSCA411-M3-02": [
		{
			"q": "Which statement about binary tree representation is NOT correct?",
			"options": [
				"Every node has at most two children, left and right",
				"In the array form a node's children sit at fixed indexes",
				"The linked form handles any shape without leaving gaps",
				"In the array form a skewed tree wastes no space at all",
			],
			"answer": 3,
			"why": "A skewed tree fills only one side of each level, so the array form leaves the other half of every position empty.",
		},
		{
			"q": "A tree is a chain in which every node has only a right child. Which representation wastes memory, and why?",
			"options": [
				"The array form, because of the empty left child slots",
				"The linked form, because it stores two pointers",
				"Both forms equally, because the shape is the same",
				"Neither form, because the tree has few nodes",
			],
			"answer": 0,
			"why": "Index arithmetic doubles down the tree, so a chain occupies positions spread far apart and leaves most cells unused.",
		},
		{
			"q": "The most nodes a binary tree can hold on level i is 2 raised to i. How many nodes can level 3 hold at most?",
			"options": ["8", "6", "16", "3"],
			"answer": 0,
			"why": "2 raised to 3 is 8, and counting from level 0 this is the fourth level down the tree.",
		},
	],
	# ---- 03. Binary tree traversals ----
	"CSCA411-M3-03": [
		{
			"q": "Which statement about the traversals is NOT correct?",
			"options": [
				"Inorder places the root between its two subtrees",
				"Preorder places the root before both subtrees",
				"Postorder visits the root before its children",
				"Level order sweeps the tree breadth first using a queue",
			],
			"answer": 2,
			"why": "Postorder finishes both subtrees and visits the root last, which is why it suits deletion.",
		},
		{
			"q": "You are deleting a folder that contains files. Which order removes the contents before the folder itself?",
			"options": [
				"Postorder, because children are handled before the parent",
				"Preorder, because the parent is handled first",
				"Inorder, because the parent sits in the middle",
				"Level order, because folder levels come first",
			],
			"answer": 0,
			"why": "This is the card's own example: postorder reaches the root last, so the contents are gone before the folder is removed.",
		},
		{
			"q": "Level order traversal of a tree with n nodes works with a queue. How many times is each node put into that queue?",
			"options": [
				"Exactly once, when it is discovered",
				"Twice, once on discovery and once on finishing",
				"Once per level of the tree",
				"It depends only on the height of the tree",
			],
			"answer": 0,
			"why": "A node is enqueued when its parent is expanded and never again, which keeps the traversal linear in the number of nodes.",
		},
	],
	# ---- 04. Types of binary trees ----
	"CSCA411-M3-04": [
		{
			"q": "Which statement about the types of binary tree is NOT correct?",
			"options": [
				"Full means every internal node has two children",
				"Complete means the last level fills from the left",
				"Skewed means the tree stays balanced as it grows",
				"Perfect means every leaf lies on the bottom level",
			],
			"answer": 2,
			"why": "A skewed tree is the opposite of balanced: it collapses to one side, so its height becomes n and it behaves like a list.",
		},
		{
			"q": "One player gets a bye and the tournament sheet collapses into a chain of single matches. What has the tree become, and why does it matter?",
			"options": [
				"Skewed, so its height is n and search behaves like a list",
				"Complete, so every level is filled from the left",
				"Perfect, because every leaf is on the bottom level",
				"Balanced, because the height stays logarithmic",
			],
			"answer": 0,
			"why": "A chain is the skewed shape, and losing the balance turns a logarithmic search into a linear scan.",
		},
		{
			"q": "A perfect binary tree has all its leaves on the bottom level. How many nodes does a perfect tree of height 3 hold?",
			"options": ["15", "7", "8", "16"],
			"answer": 0,
			"why": "A perfect tree of height h holds 2 raised to h plus 1, minus 1, so height 3 gives 16 - 1 = 15 nodes.",
		},
	],
	# ---- 05. Applications of trees ----
	"CSCA411-M3-05": [
		{
			"q": "Which of these is NOT an application of trees?",
			"options": [
				"Database indexing with B+ trees",
				"Data compression with Huffman trees",
				"Keeping process queues for round robin scheduling",
				"Expression evaluation inside a compiler",
			],
			"answer": 2,
			"why": "Round robin scheduling is a first come first served rotation, so it belongs to a circular queue rather than a tree.",
		},
		{
			"q": "A phone book tree finds one name among a lakh in about 17 comparisons. Why is that possible?",
			"options": [
				"Each comparison discards about half of the names left",
				"The tree keeps the names in ten fixed buckets",
				"The tree checks every name but does it faster",
				"The tree remembers the last name you searched",
			],
			"answer": 0,
			"why": "Searching down a balanced tree halves the remaining candidates at every step, which is what makes 17 comparisons enough for a lakh.",
		},
		{
			"q": "A balanced search tree holds one million names. About how many comparisons does one lookup need?",
			"options": ["About 20", "About 1,000", "About 100,000", "About 5"],
			"answer": 0,
			"why": "Halving a million takes about 20 steps, since 2 raised to 20 is a little more than a million.",
		},
	],
	# ---- 06. Graph terminology and types ----
	"CSCA411-M3-06": [
		{
			"q": "Which statement about graphs is NOT correct?",
			"options": [
				"A graph may contain cycles and has no root vertex",
				"The in-degree of a vertex counts edges entering it",
				"A connected graph with n vertices and no cycles has n edges",
				"An edge weight represents a cost or a distance",
			],
			"answer": 2,
			"why": "No-cycle connectivity is the definition of a tree, and a tree with n vertices has n - 1 edges, not n.",
		},
		{
			"q": "A metro map shows stations and tracks, and one route brings you back to the station you started from. What does that route show?",
			"options": [
				"A cycle, which a tree is not allowed to contain",
				"A root, which every graph must contain",
				"A spanning tree with no other edges present",
				"A directed acyclic structure with no return",
			],
			"answer": 0,
			"why": "Returning to the starting vertex is a cycle, and dropping the no-cycle rule is exactly what separates a graph from a tree.",
		},
		{
			"q": "A connected graph has 12 vertices and no cycles. How many edges does it have?",
			"options": ["11", "12", "13", "24"],
			"answer": 0,
			"why": "A connected graph with no cycle is a tree, and a tree always has one edge fewer than its vertices.",
		},
	],
	# ---- 07. Graph representation ----
	"CSCA411-M3-07": [
		{
			"q": "Which statement about graph representation is NOT correct?",
			"options": [
				"An adjacency matrix answers 'is there an edge' in one lookup",
				"An adjacency list stores only the edges that exist",
				"An adjacency matrix uses memory in proportion to the edges",
				"Both forms work with the same traversal algorithms",
			],
			"answer": 2,
			"why": "A matrix always spends V squared cells whether the graph has many edges or almost none, so its memory does not follow E.",
		},
		{
			"q": "A friendship network has a million users with about 50 friends each. Which representation fits, and why?",
			"options": [
				"An adjacency list, because the graph is sparse",
				"An adjacency matrix, because it saves memory here",
				"An incidence matrix, because it keeps weights",
				"Neither, because a million vertices cannot be held",
			],
			"answer": 0,
			"why": "A million by million matrix would be absurd for 50 friends per person, and a list stores only the edges that exist.",
		},
		{
			"q": "An adjacency matrix is built for a graph with 1,000 vertices. How many cells does it use?",
			"options": [
				"One million, because the matrix is V squared",
				"About 2,000, two cells for each vertex",
				"About 500,000, half of the square",
				"Exactly twice the number of edges",
			],
			"answer": 0,
			"why": "Every vertex gets a row and a column, so 1,000 vertices need 1,000 x 1,000 cells regardless of the edges.",
		},
	],
	# ---- 08. Graph traversals: BFS and DFS ----
	"CSCA411-M3-08": [
		{
			"q": "Which statement about the two traversals is NOT correct?",
			"options": [
				"BFS expands the oldest discovered vertex first",
				"DFS expands the most recently discovered vertex first",
				"BFS needs a visited array while DFS does not",
				"BFS gives shortest paths when every edge costs the same",
			],
			"answer": 2,
			"why": "Both traversals need the visited array; without it a cycle would make them process the same vertex forever.",
		},
		{
			"q": "You must walk from the campus gate to the library with the fewest turns. Which traversal gives that route, and why?",
			"options": [
				"BFS, because it spreads outward level by level",
				"DFS, because it dives to the end first",
				"DFS, because it keeps the turns on a stack",
				"BFS, because it explores the deepest corridor first",
			],
			"answer": 0,
			"why": "Exploring in rings means the first time a place is reached it is reached with the fewest steps, which is the BFS guarantee.",
		},
		{
			"q": "A graph has 50 vertices and 200 edges, stored as an adjacency list. About how many steps does one traversal take?",
			"options": [
				"About 250, because the cost is V + E",
				"About 2,500, because the cost is V times E",
				"About 200, because only the edges are visited",
				"About 50, because only the vertices matter",
			],
			"answer": 0,
			"why": "Each vertex is expanded once and each edge is looked at once, so the total is 50 + 200 steps, written O(V + E).",
		},
	],
	# ---- 09. Dijkstra's algorithm ----
	"CSCA411-M3-09": [
		{
			"q": "Which statement about Dijkstra's algorithm is NOT correct?",
			"options": [
				"It finds shortest paths from one source to every vertex",
				"It locks in the closest unfinalised vertex each round",
				"It works correctly on graphs with negative edge weights",
				"A priority queue version suits large road networks",
			],
			"answer": 2,
			"why": "A negative edge arriving later can beat a distance already locked in, which is why negative weights are excluded.",
		},
		{
			"q": "A road graph has one negative edge because it models a toll refund. What happens if Dijkstra's algorithm is run on it?",
			"options": [
				"The locked distances can be wrong, so it must not be used",
				"It runs faster because some edges cost less",
				"It finds the shortest path exactly as usual",
				"It needs a plain queue instead of a priority queue",
			],
			"answer": 0,
			"why": "Dijkstra's guarantee depends on distances never shrinking later, and one negative edge breaks exactly that promise.",
		},
		{
			"q": "Dijkstra's algorithm using a binary heap on V vertices and E edges runs in about:",
			"options": [
				"O((V + E) log V), because each heap step is logarithmic",
				"O(V squared) only, whatever the number of edges is",
				"O(V + E), the same as a single traversal",
				"O(E squared), because each edge is relaxed twice",
			],
			"answer": 0,
			"why": "A heap keeps the closest vertex available in logarithmic time, which gives O((V + E) log V) overall.",
		},
	],
	# ---- 10. Topological sorting ----
	"CSCA411-M3-10": [
		{
			"q": "Which statement about topological sorting is NOT correct?",
			"options": [
				"It orders the vertices of a directed acyclic graph",
				"Every edge in the result points forward",
				"It can also order a graph that contains a cycle",
				"A single DAG may have more than one valid order",
			],
			"answer": 2,
			"why": "A cycle means A needs B while B needs A, so no order can satisfy both and topological sorting is impossible.",
		},
		{
			"q": "A study plan says Data Structures before Algorithms, and Algorithms before Network Security. How many valid orders exist?",
			"options": [
				"One, because the chain fixes a single order",
				"Six, one for each permutation of the three subjects",
				"Three, one starting from each subject",
				"None, because prerequisites make the plan cyclic",
			],
			"answer": 0,
			"why": "A single chain of prerequisites leaves no freedom, so exactly one order satisfies every edge.",
		},
		{
			"q": "A project has 7 tasks and no prerequisites between them. How many of them have in-degree zero to begin with?",
			"options": [
				"All 7, because nothing has to come before them",
				"Only 1, the first task in the list",
				"None, because every task has a prerequisite",
				"6, because the last task has to wait",
			],
			"answer": 0,
			"why": "In-degree zero means no unfinished prerequisite, and with no prerequisites at all every task starts ready to run.",
		},
	],
	# ---- 11. Minimum spanning tree: Prim and Kruskal ----
	"CSCA411-M3-11": [
		{
			"q": "Which statement about the minimum spanning tree is NOT correct?",
			"options": [
				"It connects every vertex using n - 1 edges",
				"Prim grows one tree outward from a start vertex",
				"Kruskal considers edges in increasing order of weight",
				"It keeps a cycle in the tree to lower the total cost",
			],
			"answer": 3,
			"why": "A spanning tree has no cycle by definition, and both algorithms explicitly reject an edge that would create one.",
		},
		{
			"q": "Ten campus buildings must all be linked by fibre with the least total trench length. What must the result be?",
			"options": [
				"A minimum spanning tree with 9 links and no cycle",
				"A complete graph with every pair of buildings linked",
				"A shortest path tree measured from one building",
				"A set of 10 links that forms one large cycle",
			],
			"answer": 0,
			"why": "Connecting everything at the lowest total cost is the definition of a minimum spanning tree, and it needs n - 1 links.",
		},
		{
			"q": "A network has 8 buildings that must all be connected. How many links does any spanning tree use?",
			"options": ["7", "8", "9", "16"],
			"answer": 0,
			"why": "A spanning tree always uses one link fewer than the number of vertices, so 8 buildings need 7 links.",
		},
	],
}
