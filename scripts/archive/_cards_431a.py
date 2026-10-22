# CSCA 431 Mathematics for Computer Science - Modules I and II
# Logic, proofs, sets, functions, sequences, matrices and relations.

CODE = "CSCA431"

CARDS = {
    "CSCA431-MI-T01": {
        "explanation": "A proposition is a statement that is definitely true or definitely false, such as two plus two equals four. Connectives join propositions into larger ones: negation, conjunction, disjunction, exclusive or, implication and biconditional. A truth table lists the value of the whole statement for every combination of the variables. A statement that is always true is a tautology, one that is always false is a contradiction, and the rest are contingencies. Two statements are logically equivalent when their truth table columns match. The laws of De Morgan, distribution and absorption are used to rewrite one into the other.",
        "example": "The statement it is raining or it is not raining is a tautology, because one half must hold. The statement it is raining and it is not raining is a contradiction.",
        "quiz": [
            {
                "q": "Which connective gives a true result only when both inputs are true?",
                "options": ["Disjunction", "Conjunction", "Exclusive or", "Implication"],
                "answer": 1,
                "why": "Conjunction, the and operator, is true only when both of its operands are true.",
            },
            {
                "q": "A statement that is true for every combination of its variables is called:",
                "options": ["A contradiction", "A contingency", "A tautology", "A fallacy"],
                "answer": 2,
                "why": "A tautology is always true, a contradiction is always false, and a contingency is sometimes each.",
            },
            {
                "q": "Which statement about propositional logic is NOT correct?",
                "options": ["A proposition has a definite truth value", "A truth table lists every combination of the variables", "De Morgan laws relate conjunction, disjunction and negation", "An implication is true only when both of its parts are true"],
                "answer": 3,
                "why": "An implication is false only when the premise is true and the conclusion is false.",
            },
            {
                "q": "How many rows does a truth table for three variables have?",
                "options": ["3", "6", "8", "9"],
                "answer": 2,
                "why": "Each variable doubles the count, so three variables give 2 to the power 3, which is 8 rows.",
            },
            {
                "q": "An argument whose conclusion must be true whenever all its premises are true is called:",
                "options": ["Valid", "Sound", "Tautological", "Equivalent"],
                "answer": 0,
                "why": "Validity is about the link from premises to conclusion; soundness also needs the premises to be true.",
            },
        ],
        "examTip": "Write the six connectives with their symbols, then draw one truth table and label the tautology and the contradiction.",
    },

    "CSCA431-MI-T02": {
        "explanation": "A predicate is a statement with a variable in it, such as P of x meaning x is greater than three. It becomes a proposition only once the variable is given a value or bound by a quantifier. The universal quantifier says that P holds for every element of the domain, and the existential quantifier says it holds for at least one. Negation flips them: not for all becomes there exists a counterexample, and not there exists becomes for all not. With nested quantifiers the order matters, because for all x there exists y says something different from there exists y for all x.",
        "example": "For every student there is a subject they like is not the same as there is a subject that every student likes. Swapping the two quantifiers changes what is being claimed.",
        "quiz": [
            {
                "q": "Which quantifier says that a predicate holds for every element of the domain?",
                "options": ["Existential quantifier", "Universal quantifier", "Nested quantifier", "Bound quantifier"],
                "answer": 1,
                "why": "The universal quantifier, written as an upside down A, claims the predicate for all elements.",
            },
            {
                "q": "What is the negation of the statement every student passed?",
                "options": ["Every student failed", "At least one student did not pass", "No student passed", "Some student passed"],
                "answer": 1,
                "why": "Negating a universal gives an existential, because one counterexample is enough to break the claim.",
            },
            {
                "q": "Which statement about quantifiers is NOT correct?",
                "options": ["A predicate becomes a proposition once its variable is bound", "The order of nested quantifiers can change the meaning", "The negation of there exists is for all not", "For all x there exists y means the same as there exists y for all x"],
                "answer": 3,
                "why": "The first says each x has its own y, while the second says one single y works for every x.",
            },
            {
                "q": "Which of these is a valid rule of inference?",
                "options": ["Affirming the consequent", "Denying the antecedent", "Modus ponens", "The converse of an implication"],
                "answer": 2,
                "why": "Modus ponens takes p and p implies q and concludes q; the other three are known fallacies.",
            },
            {
                "q": "Which argument form is a fallacy?",
                "options": ["Modus tollens", "Hypothetical syllogism", "Disjunctive syllogism", "Affirming the consequent"],
                "answer": 3,
                "why": "From p implies q and q you cannot conclude p, because q may hold for another reason.",
            },
        ],
        "examTip": "Write the two quantifiers with their symbols, give the two negation rules, then show why swapping nested quantifiers changes the meaning.",
    },

    "CSCA431-MI-T03": {
        "explanation": "A proof is a valid argument that leaves no doubt about a statement. A direct proof assumes the hypothesis and works forward with known facts until the conclusion appears. Proof by contraposition proves not q implies not p instead, which is logically the same claim. Proof by contradiction assumes the statement is false and derives something impossible, the classic example being that the square root of two is irrational. A proof by cases splits the statement into cases that cover everything, and an existence proof shows that at least one object exists.",
        "example": "To prove that if n squared is odd then n is odd, prove the contrapositive instead. If n is even then n squared is even, which follows at once.",
        "quiz": [
            {
                "q": "Which method proves not q implies not p instead of p implies q?",
                "options": ["Direct proof", "Proof by contraposition", "Proof by contradiction", "Proof by cases"],
                "answer": 1,
                "why": "A conditional and its contrapositive are logically equivalent, so proving one proves the other.",
            },
            {
                "q": "Which classical result is proved by contradiction in most textbooks?",
                "options": ["The sum of the first n integers", "The irrationality of the square root of two", "The binomial theorem", "The division algorithm"],
                "answer": 1,
                "why": "Assuming the square root of two is rational forces a common factor, which contradicts the fraction being in lowest terms.",
            },
            {
                "q": "Which statement about proofs is NOT correct?",
                "options": ["A vacuous proof relies on the hypothesis being false", "A trivial proof relies on the conclusion being already known", "A direct proof assumes the hypothesis and derives the conclusion", "A proof by cases only needs to cover the largest case"],
                "answer": 3,
                "why": "The cases must exhaust every possibility, or a gap remains where the statement is unproved.",
            },
            {
                "q": "Which proof shows an object exists without producing it?",
                "options": ["Constructive proof", "Non constructive proof", "Direct proof", "Proof by contraposition"],
                "answer": 1,
                "why": "A constructive proof hands you the object, while a non constructive one only shows that it must exist.",
            },
            {
                "q": "How many cases must a proof by cases cover?",
                "options": ["One representative case", "Every case that the statement allows", "Exactly two cases", "As many as there are words in the theorem"],
                "answer": 1,
                "why": "The cases have to be exhaustive, otherwise the statement stays unproved in the gap.",
            },
        ],
        "examTip": "Name each method in one line with the shape of its argument, and keep the square root of two ready for the contradiction method.",
    },

    "CSCA431-MI-T04": {
        "explanation": "Strategy is about choosing a method before writing a line. Work forward from the hypothesis, or work backward from the goal until it meets a known fact. Try small cases first, because a counterexample found early saves a long attempt at a proof. Induction proves a statement for every natural number in two steps. The base case is proved first, then the step showing that P of k implies P of k plus one. Strong induction assumes all the smaller cases instead of only the previous one. The well ordering property is why induction works at all.",
        "example": "To prove the sum of the first n odd numbers is n squared, check n equals 1. Then show that adding the next odd number takes k squared to k plus one squared.",
        "quiz": [
            {
                "q": "What are the two steps of a proof by mathematical induction?",
                "options": ["Hypothesis and conclusion", "Base case and inductive step", "Converse and contrapositive", "Existence and uniqueness"],
                "answer": 1,
                "why": "The base case starts the chain and the inductive step keeps it going for every natural number.",
            },
            {
                "q": "How does strong induction differ from ordinary induction?",
                "options": ["It skips the base case", "It assumes the statement for all smaller values", "It proves the statement for real numbers", "It needs two base cases"],
                "answer": 1,
                "why": "Strong induction may use any earlier case, which helps when the step depends on more than one predecessor.",
            },
            {
                "q": "Which statement about induction is NOT correct?",
                "options": ["The base case must be proved separately", "The inductive step proves P of k implies P of k plus one", "The well ordering property underlies induction", "Assuming the conclusion and reaching a known fact is a valid inductive step"],
                "answer": 3,
                "why": "Assuming what you are proving is circular, and it is the most common induction mistake.",
            },
            {
                "q": "Which mistake breaks an induction proof?",
                "options": ["Stating the base case explicitly", "Proving the inductive step in detail", "Omitting the base case", "Using the variable n"],
                "answer": 2,
                "why": "Without a base case the chain has nothing to start from, so nothing at all is proved.",
            },
            {
                "q": "What does the well ordering property say?",
                "options": ["Every set has a largest element", "Every non-empty set of positive integers has a least element", "Every group has a generator", "Every relation is transitive"],
                "answer": 1,
                "why": "That least element is what makes the descent argument behind induction and strong induction work.",
            },
        ],
        "examTip": "Write the two induction steps as labelled lines, then add one sentence on the two usual mistakes: no base case and assuming the conclusion.",
    },

    "CSCA431-MII-T01": {
        "explanation": "A set is an unordered collection of distinct objects, listed or given by a rule such as x such that x is even. A is a subset of B when every element of A also lies in B, and the power set holds all the subsets. The operations are union, intersection, difference, complement and symmetric difference, and the identities they obey mirror the laws of logic. The size of a set is its cardinality, and the inclusion exclusion rule stops the overlap being counted twice. The Cartesian product collects every ordered pair from two sets, which is what relations and functions are built on.",
        "example": "A set of three students has 2 to the power 3, which is 8 subsets in its power set. That already takes a line to list, which is why the power set grows too fast to write out for large sets.",
        "quiz": [
            {
                "q": "How many subsets does a set with 4 elements have?",
                "options": ["4", "8", "16", "24"],
                "answer": 2,
                "why": "The power set has 2 to the power n elements, so 2 to the power 4 gives 16.",
            },
            {
                "q": "Which rule gives the size of the union of two overlapping sets?",
                "options": ["|A| + |B|", "|A| + |B| - |A intersection B|", "|A| x |B|", "|A| - |B|"],
                "answer": 1,
                "why": "Inclusion exclusion subtracts the intersection once, because those elements were counted twice.",
            },
            {
                "q": "Which statement about sets is NOT correct?",
                "options": ["A set lists each element only once", "The order of elements in a set does not matter", "The empty set is a subset of every set", "The power set of A has the same number of elements as A"],
                "answer": 3,
                "why": "The power set has 2 to the power n elements, which is larger than n for every non-empty set.",
            },
            {
                "q": "If A has 10 elements, B has 7 and their intersection has 3, what is the size of the union?",
                "options": ["14", "17", "20", "10"],
                "answer": 0,
                "why": "Inclusion exclusion gives 10 + 7 - 3, which is 14.",
            },
            {
                "q": "What does the Cartesian product of A and B contain?",
                "options": ["Every element of A plus every element of B", "Every ordered pair with the first from A and the second from B", "Only the elements common to A and B", "The subsets shared by A and B"],
                "answer": 1,
                "why": "Ordered pairs are what make relations and functions possible, and the order inside each pair matters.",
            },
        ],
        "examTip": "Write the set operations with their symbols, then give the inclusion exclusion formula and one worked example with numbers.",
    },

    "CSCA431-MII-T02": {
        "explanation": "A function takes each element of its domain and gives back exactly one element of its codomain. The domain is the set of allowed inputs, the codomain is the declared output set and the range is what actually comes out. A function is injective when different inputs always give different outputs, and surjective when every element of the codomain is reached. A function that is both is bijective, and only then does an inverse exist. Composition applies one function after another, and the graph of a function is the set of its ordered pairs.",
        "example": "The function that squares an integer is not injective, because 2 and minus 2 both give 4. Restricting the domain to non-negative integers makes it injective, and then an inverse exists.",
        "quiz": [
            {
                "q": "What is a function that is both injective and surjective called?",
                "options": ["A constant function", "A bijective function", "An identity function", "A floor function"],
                "answer": 1,
                "why": "Bijective means one to one and onto, which is exactly when an inverse function exists.",
            },
            {
                "q": "Which statement about functions is NOT correct?",
                "options": ["Every input maps to exactly one output", "An injective function never sends two inputs to the same output", "A surjective function reaches every element of the codomain", "Every function has an inverse"],
                "answer": 3,
                "why": "An inverse needs the function to be bijective, and most functions are not.",
            },
            {
                "q": "The range of a function is:",
                "options": ["The set of allowed inputs", "The set of outputs actually produced", "The declared output set", "The graph of the function"],
                "answer": 1,
                "why": "The codomain is what is declared up front; the range is the part of it that is really hit.",
            },
            {
                "q": "A function from a set of 3 elements to a set of 5 elements cannot be:",
                "options": ["Injective", "Surjective", "Well defined", "Any of these"],
                "answer": 1,
                "why": "Three inputs produce at most three outputs, so two elements of the codomain are missed.",
            },
            {
                "q": "What does the composition of two functions do?",
                "options": ["Adds their outputs together", "Applies one function and then the other", "Swaps their domains", "Inverts both of them"],
                "answer": 1,
                "why": "Composition feeds the output of one function straight into the input of the next.",
            },
        ],
        "examTip": "Draw two small arrow diagrams, one injective and one surjective, and write the one line condition for each.",
    },

    "CSCA431-MII-T03": {
        "explanation": "A sequence is an ordered list of numbers following a rule, and a series adds its terms. In an arithmetic progression each term differs from the previous one by a constant. Its sum is n over 2 times the first term plus the last. In a geometric progression each term is a fixed multiple of the previous one, and the sum formula divides by r minus 1. A recurrence relation defines a term from earlier terms, as the Fibonacci rule does. Sigma notation writes a sum compactly, and the formulas for the first n integers, squares and cubes save pages of arithmetic.",
        "example": "Saving 100 rupees more each month than the last gives an arithmetic progression. The total after a year is 12 over 2 times the first month plus the last month's amount.",
        "quiz": [
            {
                "q": "What is the sum of the first 100 positive integers?",
                "options": ["5,000", "5,050", "10,000", "100"],
                "answer": 1,
                "why": "The formula n times n plus 1 over 2 gives 100 times 101 over 2, which is 5,050.",
            },
            {
                "q": "In a geometric progression, each term is:",
                "options": ["Increased by a constant amount", "Multiplied by a constant factor", "The sum of the two previous terms", "Reversed in order"],
                "answer": 1,
                "why": "A fixed multiplier defines a geometric progression, while a fixed difference defines an arithmetic one.",
            },
            {
                "q": "Which statement about sequences is NOT correct?",
                "options": ["An arithmetic progression has a constant difference", "The Fibonacci sequence is defined by a recurrence", "A geometric progression has a constant ratio", "Every recurrence relation has a closed form that is easy to find"],
                "answer": 3,
                "why": "Many recurrences have no simple closed form, which is why they are studied in their own right.",
            },
            {
                "q": "Which sequence is defined by adding the two previous terms?",
                "options": ["An arithmetic progression", "A geometric progression", "The Fibonacci sequence", "The triangular numbers"],
                "answer": 2,
                "why": "The Fibonacci rule takes each term as the sum of the two before it, once the first two are fixed.",
            },
            {
                "q": "What is the sum of the arithmetic progression 2, 5, 8, 11, 14?",
                "options": ["30", "35", "40", "45"],
                "answer": 2,
                "why": "There are 5 terms, so the sum is 5 over 2 times 2 plus 14, which is 40.",
            },
        ],
        "examTip": "Write the two progression formulas side by side, then add the sigma formulas for the first n integers, squares and cubes.",
    },

    "CSCA431-MII-T04": {
        "explanation": "A matrix is a rectangular array of numbers arranged in rows and columns. It may be square, diagonal, symmetric, an identity matrix or a zero matrix, depending on its shape and its entries. Matrices of the same size add and subtract entry by entry, and multiplication follows the row by column rule. The transpose swaps rows with columns, and the trace adds the entries on the main diagonal. A square matrix has an inverse only when its determinant is not zero. A Boolean matrix uses only 0 and 1, with join and meet as its operations.",
        "example": "Multiplying a 2 by 3 matrix by a 3 by 4 matrix gives a 2 by 4 result. The inner dimensions must match, or the product is not defined.",
        "quiz": [
            {
                "q": "When can two matrices be multiplied?",
                "options": ["When they have the same number of rows", "When the columns of the first equal the rows of the second", "When both matrices are square", "When both have the same determinant"],
                "answer": 1,
                "why": "The inner dimensions must match, and the result takes the two outer dimensions.",
            },
            {
                "q": "What is the trace of a matrix?",
                "options": ["The sum of the entries on the main diagonal", "The product of all its entries", "The number of rows", "The determinant"],
                "answer": 0,
                "why": "The trace is defined only for a square matrix, and it adds the diagonal entries.",
            },
            {
                "q": "Which statement about matrices is NOT correct?",
                "options": ["The transpose swaps rows and columns", "Matrix multiplication is commutative", "An inverse exists only when the determinant is non-zero", "An identity matrix has ones on the diagonal and zeros elsewhere"],
                "answer": 1,
                "why": "Order matters in matrix multiplication, so A times B usually differs from B times A.",
            },
            {
                "q": "A 2 by 3 matrix is multiplied by a 3 by 5 matrix. What is the size of the result?",
                "options": ["2 by 5", "3 by 3", "5 by 2", "Not defined"],
                "answer": 0,
                "why": "The inner dimensions 3 and 3 match, and the result takes the outer dimensions 2 and 5.",
            },
            {
                "q": "What values does a Boolean matrix hold?",
                "options": ["Any real numbers", "Only 0 and 1", "Only prime numbers", "Only negative numbers"],
                "answer": 1,
                "why": "Boolean matrices use 0 and 1 with join and meet, which is how relations are stored.",
            },
        ],
        "examTip": "Give the row by column rule in one line, then state the condition for an inverse and the shape rule for a product.",
    },

    "CSCA431-MII-T05": {
        "explanation": "A relation from A to B is any subset of the Cartesian product A cross B, so it is a set of ordered pairs. It can be written as a list of pairs, as a zero one matrix or as a directed graph. On a single set a relation may be reflexive, symmetric, antisymmetric or transitive, and which of these hold decides what the relation is called. A relation that is reflexive, symmetric and transitive is an equivalence relation, and it cuts the set into equivalence classes. One that is reflexive, antisymmetric and transitive is a partial order, drawn as a Hasse diagram.",
        "example": "Equality is reflexive, symmetric and transitive, so it is an equivalence relation. The divides relation on the positive integers is reflexive, antisymmetric and transitive, so it is a partial order.",
        "quiz": [
            {
                "q": "Which three properties make a relation an equivalence relation?",
                "options": ["Reflexive, antisymmetric and transitive", "Reflexive, symmetric and transitive", "Symmetric, antisymmetric and irreflexive", "Reflexive, irreflexive and transitive"],
                "answer": 1,
                "why": "Those three together are what partitions the set into equivalence classes.",
            },
            {
                "q": "Which properties define a partial order?",
                "options": ["Reflexive, symmetric and transitive", "Reflexive, antisymmetric and transitive", "Irreflexive, symmetric and transitive", "Symmetric and transitive only"],
                "answer": 1,
                "why": "Antisymmetry replaces symmetry, which lets a partial order compare elements rather than group them.",
            },
            {
                "q": "Which statement about relations is NOT correct?",
                "options": ["A relation can be drawn as a directed graph", "A relation can be stored as a zero one matrix", "The transitive closure is computed by Warshall algorithm", "Every reflexive relation is also symmetric"],
                "answer": 3,
                "why": "Reflexive and symmetric are independent properties, and neither one follows from the other.",
            },
            {
                "q": "What does the reflexive closure of a relation add?",
                "options": ["Every missing pair a to a", "The reverse of every pair", "Every pair reachable by a path", "Nothing, because closures only remove pairs"],
                "answer": 0,
                "why": "The reflexive closure adds self loops, the symmetric one adds reverses and the transitive one adds path shortcuts.",
            },
            {
                "q": "Which algorithm computes the transitive closure of a relation?",
                "options": ["Dijkstra algorithm", "Warshall algorithm", "Euclidean algorithm", "Sieve of Eratosthenes"],
                "answer": 1,
                "why": "Warshall works on the relation matrix and fills in every pair reachable by a path.",
            },
        ],
        "examTip": "List the five properties with a one line test for each, then give the property sets for equivalence and for partial order.",
    },
}
