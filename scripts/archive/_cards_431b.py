# CSCA 431 Mathematics for Computer Science - Modules III, IV and V
# Number theory, algebraic structures and counting.

CODE = "CSCA431"

CARDS = {
    "CSCA431-MIII-T01": {
        "explanation": "The division algorithm says that a equals d times q plus r, with r between zero and d minus one. Both q and r are unique. When r is zero we say d divides a. Congruence modulo m means that m divides a minus b, which is the same as saying a and b leave the same remainder. Addition and multiplication can be done on the remainders, and the answer is taken modulo m again. That wrapping is what makes clocks, hash tables and check digits work. A linear congruence a x congruent to b modulo m has a solution exactly when the gcd of a and m divides b.",
        "example": "If it is 10 o'clock now, then in 5 hours it is 3 o'clock. The reason is that 15 modulo 12 is 3.",
        "quiz": [
            {
                "q": "What does it mean to say a is congruent to b modulo m?",
                "options": ["a and b are equal", "m divides a minus b", "a is larger than b", "a and b are both prime"],
                "answer": 1,
                "why": "Congruence means the difference is a multiple of m, so both numbers leave the same remainder.",
            },
            {
                "q": "What is 17 modulo 5?",
                "options": ["1", "2", "3", "5"],
                "answer": 1,
                "why": "17 is 3 times 5 plus 2, so the remainder is 2.",
            },
            {
                "q": "Which statement about modular arithmetic is NOT correct?",
                "options": ["Addition works on remainders", "Multiplication works on remainders", "Every non-zero element has an inverse modulo any m", "Clocks are an example of arithmetic modulo 12"],
                "answer": 2,
                "why": "An inverse exists only when a and m are coprime, which is why prime moduli matter in cryptography.",
            },
            {
                "q": "When does the linear congruence a x congruent to b modulo m have a solution?",
                "options": ["Always", "Only when a and m are coprime", "When the gcd of a and m divides b", "Never, unless b is zero"],
                "answer": 2,
                "why": "The gcd condition decides solvability, and the number of solutions equals that gcd.",
            },
            {
                "q": "In the division algorithm a = dq + r, what range does r lie in?",
                "options": ["0 to d", "0 to d minus 1", "1 to d", "Any value at all"],
                "answer": 1,
                "why": "The remainder is non-negative and strictly smaller than the divisor, which is what makes q and r unique.",
            },
        ],
        "examTip": "State the division algorithm with the range of r, define congruence, then give one clock sum and one hash example.",
    },

    "CSCA431-MIII-T02": {
        "explanation": "Computers hold integers in base two, and converting between bases uses expansion on one side and repeated division on the other. The Euclidean algorithm finds the gcd by replacing the pair with the divisor and the remainder until the remainder is zero. The extended version also records the coefficients x and y with a x plus b y equal to the gcd. Those coefficients give the modular inverse of a, which exists whenever the gcd is one. The same condition decides a linear Diophantine equation, which is solvable exactly when the gcd of a and b divides c.",
        "example": "For 48 and 18: 48 is 2 times 18 plus 12, then 18 is 1 times 12 plus 6. Then 12 is 2 times 6 plus 0, so the gcd is 6.",
        "quiz": [
            {
                "q": "What does the Euclidean algorithm compute?",
                "options": ["The least common multiple", "The greatest common divisor", "The prime factorisation", "The modular inverse directly"],
                "answer": 1,
                "why": "It replaces the pair by the divisor and remainder repeatedly, and the last non-zero remainder is the gcd.",
            },
            {
                "q": "What extra output does the extended Euclidean algorithm give?",
                "options": ["The prime factorisation", "The coefficients x and y with a x plus b y equal to the gcd", "The remainder sequence only", "The number of divisors"],
                "answer": 1,
                "why": "Those coefficients are what produce a modular inverse when the gcd is 1.",
            },
            {
                "q": "When does a have an inverse modulo m?",
                "options": ["Always", "Only when a is prime", "When the gcd of a and m is 1", "When m is even"],
                "answer": 2,
                "why": "Being coprime to m is exactly the condition, and the extended Euclidean algorithm finds the inverse.",
            },
            {
                "q": "Which statement about integer algorithms is NOT correct?",
                "options": ["Base conversion uses repeated division", "The Euclidean algorithm ends when the remainder is zero", "A linear Diophantine equation needs the gcd to divide the constant", "The Euclidean algorithm needs the prime factorisation first"],
                "answer": 3,
                "why": "The Euclidean algorithm needs no factorisation, which is why it stays fast on very large numbers.",
            },
            {
                "q": "When is a x + b y = c solvable in integers?",
                "options": ["Always", "Only when a and b are prime", "When the gcd of a and b divides c", "Only when c is odd"],
                "answer": 2,
                "why": "The gcd divides the left side whatever x and y are, so it has to divide c as well.",
            },
        ],
        "examTip": "Show one Euclidean run as three division lines, then state two conditions: gcd 1 for an inverse, and gcd divides c for a Diophantine equation.",
    },

    "CSCA431-MIII-T03": {
        "explanation": "A prime is an integer greater than one whose only positive divisors are one and itself. The fundamental theorem of arithmetic says every integer greater than one factors into primes in exactly one way, up to the order. That uniqueness is what lets the gcd and the lcm be read straight off the two factorisations. Two numbers are relatively prime when their gcd is one, and the lcm can be found from the product divided by the gcd. The sieve of Eratosthenes lists primes by crossing out multiples, and trial division tests one number by trying divisors up to its square root.",
        "example": "12 is 2 squared times 3 and 18 is 2 times 3 squared. The gcd is 6 and the lcm is 36, read off the two factorisations.",
        "quiz": [
            {
                "q": "What does the fundamental theorem of arithmetic state?",
                "options": ["Every integer is prime", "Every integer greater than 1 factors uniquely into primes", "There are infinitely many primes", "Every even number is composite"],
                "answer": 1,
                "why": "Existence and uniqueness of the prime factorisation is the content of the theorem.",
            },
            {
                "q": "How is the lcm found from the product of two numbers?",
                "options": ["Product times the gcd", "Product divided by the gcd", "Product minus the gcd", "Product plus the gcd"],
                "answer": 1,
                "why": "The gcd and lcm satisfy a times b equals gcd times lcm, so dividing gives the lcm.",
            },
            {
                "q": "Up to what value must trial division test divisors?",
                "options": ["Half the number", "The square root of the number", "Twice the number", "The number itself"],
                "answer": 1,
                "why": "If a divisor above the square root existed, its partner below it would have been found first.",
            },
            {
                "q": "Which statement about primes is NOT correct?",
                "options": ["Two numbers with gcd 1 are relatively prime", "The sieve of Eratosthenes lists primes by crossing out multiples", "A prime has exactly two positive divisors", "1 is a prime number"],
                "answer": 3,
                "why": "One is excluded by definition, because including it would break unique factorisation.",
            },
            {
                "q": "What form does a Mersenne prime have?",
                "options": ["2 to the p minus 1", "n squared plus 1", "2 times n plus 1", "n factorial plus 1"],
                "answer": 0,
                "why": "Mersenne primes are one less than a power of two, and the largest known primes are of this form.",
            },
        ],
        "examTip": "Write the prime factorisations of two numbers, read off the gcd and lcm, then add the square root rule for trial division.",
    },

    "CSCA431-MIII-T04": {
        "explanation": "A system of linear congruences can be solved by substitution, or in one step by the Chinese remainder theorem. That theorem says a system whose moduli are pairwise relatively prime has a unique solution modulo their product. Fermat's little theorem says a to the p minus one is congruent to one modulo p. It needs p to be prime and not a divisor of a. Euler's theorem replaces p minus one with the totient phi of n, which counts the numbers up to n that are coprime to n. Both results are what make RSA work, because they let a huge exponent be reduced to a small one.",
        "example": "To find the last digit of 3 to the 100, work modulo 10. The powers of 3 repeat with period four, and 100 is a multiple of 4, so the answer is 1.",
        "quiz": [
            {
                "q": "What does the Chinese remainder theorem require of the moduli?",
                "options": ["They must all be prime", "They must be pairwise relatively prime", "They must all be odd", "They must be equal"],
                "answer": 1,
                "why": "Pairwise coprime moduli give one solution modulo the product of all of them.",
            },
            {
                "q": "What does Fermat's little theorem say when p is prime and does not divide a?",
                "options": ["a to the p is congruent to a mod p", "a to the p minus 1 is congruent to 1 mod p", "a is congruent to p mod a", "a squared is congruent to 1 mod p"],
                "answer": 1,
                "why": "That is the classic form, and it is Euler's theorem with phi of p equal to p minus 1.",
            },
            {
                "q": "What does the totient phi of n count?",
                "options": ["The divisors of n", "The integers up to n that are coprime to n", "The prime factors of n", "The multiples of n"],
                "answer": 1,
                "why": "Phi of n is the size of the multiplicative group modulo n, which is why it appears in Euler's theorem.",
            },
            {
                "q": "Which statement about these theorems is NOT correct?",
                "options": ["Euler's theorem generalises Fermat's little theorem", "The Chinese remainder theorem gives a unique solution modulo the product", "Fermat's little theorem needs p to be prime", "RSA uses the totient because phi is easy to compute for any n"],
                "answer": 3,
                "why": "Computing phi is easy only when the factorisation is known, and that difficulty is what keeps RSA safe.",
            },
            {
                "q": "For a prime p, what is phi of p?",
                "options": ["p", "p minus 1", "p plus 1", "1"],
                "answer": 1,
                "why": "Every number from 1 to p minus 1 is coprime to a prime, so the count is p minus 1.",
            },
        ],
        "examTip": "Write the three theorems with their exact conditions, then add one line on how RSA uses the totient and large primes.",
    },

    "CSCA431-MIV-T01": {
        "explanation": "A group is a set with one operation satisfying four axioms: closure, associativity, an identity element and an inverse for every element. When the operation is also commutative the group is called abelian. The integers under addition form a group, and so do the non-zero rationals under multiplication. The order of a group is the number of elements in it. The order of an element is the smallest power that returns it to the identity. A subgroup is a subset that is a group in its own right under the same operation.",
        "example": "The integers under addition form a group with identity 0 and inverse minus n. The integers under multiplication do not, because 2 has no inverse that is still an integer.",
        "quiz": [
            {
                "q": "Which four axioms define a group?",
                "options": ["Closure, associativity, identity, inverse", "Closure, commutativity, identity, inverse", "Associativity, commutativity, distributivity, identity", "Closure, associativity, distributivity, inverse"],
                "answer": 0,
                "why": "Commutativity is not required, and it is what makes an abelian group a special case.",
            },
            {
                "q": "What is a group whose operation is commutative called?",
                "options": ["A cyclic group", "An abelian group", "A simple group", "A quotient group"],
                "answer": 1,
                "why": "Abelian groups satisfy a times b equals b times a in addition to the four group axioms.",
            },
            {
                "q": "Which statement about groups is NOT correct?",
                "options": ["The integers under addition form a group", "The non-zero rationals under multiplication form a group", "The integers under multiplication form a group", "Permutations of a set form a group under composition"],
                "answer": 2,
                "why": "Most integers have no multiplicative inverse that is an integer, so the inverse axiom fails.",
            },
            {
                "q": "What is the order of an element a in a group?",
                "options": ["The number of elements in the group", "The smallest positive n with a to the n equal to the identity", "The number of subgroups containing a", "The inverse of a"],
                "answer": 1,
                "why": "If no such power exists the element has infinite order, as in the integers under addition.",
            },
            {
                "q": "What must a subgroup satisfy?",
                "options": ["Contain the identity and be closed under the operation and inverses", "Contain every element of the group", "Be commutative", "Have prime order"],
                "answer": 0,
                "why": "Those conditions are exactly what makes the subset a group under the same operation.",
            },
        ],
        "examTip": "State the four axioms, name one abelian and one non-abelian example, then give the subgroup test.",
    },

    "CSCA431-MIV-T02": {
        "explanation": "A cyclic group is one where every element is a power of a single generator g. The integers under addition are cyclic with generator 1, because every integer is a multiple of 1. In a finite cyclic group the order of the group equals the order of its generator, and every subgroup of a cyclic group is cyclic. A homomorphism is a map that respects the operation, so f of a times b equals f of a times f of b. Its kernel is everything that maps to the identity, and its image is everything that is reached; both are subgroups.",
        "example": "The integers modulo 6 under addition are cyclic, generated by 1. The element 2 generates only 0, 2 and 4, so it generates a proper subgroup.",
        "quiz": [
            {
                "q": "What makes a group cyclic?",
                "options": ["It has a finite number of elements", "Every element is a power of one generator", "Every element commutes", "It has no proper subgroups"],
                "answer": 1,
                "why": "One element and its powers produce the whole group, which is what generated means here.",
            },
            {
                "q": "What condition must a homomorphism satisfy?",
                "options": ["f of a times b equals f of a times f of b", "f of a equals a", "f is one to one", "f is onto"],
                "answer": 0,
                "why": "Preserving the operation is the definition; being one to one or onto is an extra property.",
            },
            {
                "q": "What is the kernel of a homomorphism?",
                "options": ["The set of all outputs", "The set of elements mapping to the identity", "The set of generators", "The set of elements of order two"],
                "answer": 1,
                "why": "The kernel measures how much the map collapses, and it is always a subgroup of the domain.",
            },
            {
                "q": "Which statement about cyclic groups is NOT correct?",
                "options": ["Every subgroup of a cyclic group is cyclic", "The integers under addition are cyclic with generator 1", "The order of a finite cyclic group equals the order of its generator", "Every cyclic group is finite"],
                "answer": 3,
                "why": "The integers under addition are an infinite cyclic group, so finiteness is not part of the definition.",
            },
            {
                "q": "What is an isomorphism?",
                "options": ["A homomorphism with a trivial kernel", "A bijective homomorphism", "A homomorphism onto a subgroup", "A map that reverses the operation"],
                "answer": 1,
                "why": "A bijective homomorphism preserves the structure both ways, so the groups differ only in names.",
            },
        ],
        "examTip": "Give the definition of a cyclic group with one example, then state the homomorphism condition and name the kernel and image.",
    },

    "CSCA431-MIV-T03": {
        "explanation": "A coset is one element multiplied by every element of a subgroup H, written aH on the left or Ha on the right. The cosets of H partition the group into blocks, and every block has exactly the size of H. The number of blocks is the index of H, which is the group order divided by the subgroup order. Lagrange's theorem says the order of a subgroup divides the order of the group, so the order of every element divides it too. A subgroup is normal when aH equals Ha for every a, and only then can the cosets be made into a quotient group.",
        "example": "In a group of order 12, a subgroup can only have order 1, 2, 3, 4, 6 or 12. A subgroup of order 5 is impossible, because 5 does not divide 12.",
        "quiz": [
            {
                "q": "What does Lagrange's theorem state?",
                "options": ["Every subgroup is normal", "The order of a subgroup divides the order of the group", "Every group is cyclic", "The index is always prime"],
                "answer": 1,
                "why": "The cosets have equal size and partition the group, so the group order is a multiple of the subgroup order.",
            },
            {
                "q": "A group has order 12. Which of these cannot be the order of a subgroup?",
                "options": ["2", "4", "5", "6"],
                "answer": 2,
                "why": "Lagrange's theorem allows only divisors of 12, and 5 is not one of them.",
            },
            {
                "q": "Which statement about cosets is NOT correct?",
                "options": ["Cosets of a subgroup partition the group", "All cosets of a subgroup have the same size", "The number of cosets is called the index", "Two cosets are either disjoint or they overlap partly"],
                "answer": 3,
                "why": "Two cosets are either identical or completely disjoint, which is what makes them a partition.",
            },
            {
                "q": "When is a subgroup called normal?",
                "options": ["When it has prime order", "When aH equals Ha for every element a", "When it contains the identity", "When it is cyclic"],
                "answer": 1,
                "why": "Equal left and right cosets are what let a well defined quotient group be built from them.",
            },
            {
                "q": "What is a simple group?",
                "options": ["A group of prime order with no operation", "A group with no proper non-trivial normal subgroup", "A group with one element", "A group that is cyclic"],
                "answer": 1,
                "why": "Simple groups are the building blocks, because they cannot be broken into a smaller quotient.",
            },
        ],
        "examTip": "State Lagrange's theorem, give the divisor example, then define a normal subgroup with the aH equals Ha test.",
    },

    "CSCA431-MIV-T04": {
        "explanation": "A ring carries two operations: it is an abelian group under addition, and multiplication is associative and distributes over addition. A commutative ring with unity is one where multiplication commutes and there is a multiplicative identity. An integral domain adds the rule that there are no zero divisors, so a product can only be zero when one factor is. A field goes further and gives every non-zero element an inverse; the rationals, the reals and the integers modulo a prime are all fields. The characteristic is the smallest number of times the identity must be added to itself to reach zero.",
        "example": "The integers form an integral domain but not a field, because 2 has no integer inverse. The integers modulo 7 do form a field, because every non-zero class has an inverse.",
        "quiz": [
            {
                "q": "What extra property makes a ring a field?",
                "options": ["Multiplication commutes", "Every non-zero element has a multiplicative inverse", "There is an additive identity", "Multiplication is associative"],
                "answer": 1,
                "why": "Commutativity and associativity are already assumed; inverses for every non-zero element is the step up.",
            },
            {
                "q": "What is an integral domain?",
                "options": ["A ring where every element has an inverse", "A commutative ring with unity and no zero divisors", "A ring of prime order", "A field of characteristic zero"],
                "answer": 1,
                "why": "No zero divisors means a product of non-zero elements is never zero, so cancellation works.",
            },
            {
                "q": "Which of these is a field?",
                "options": ["The integers", "The integers modulo 6", "The integers modulo 7", "The even integers"],
                "answer": 2,
                "why": "A prime modulus gives a field, because every non-zero class is coprime to 7 and has an inverse.",
            },
            {
                "q": "Which statement about rings is NOT correct?",
                "options": ["A ring is an abelian group under addition", "Multiplication distributes over addition", "Every ring has a multiplicative identity", "A field has no zero divisors"],
                "answer": 2,
                "why": "Unity is an extra condition; rings without it are valid and are called rings without unity.",
            },
            {
                "q": "What is the characteristic of a ring?",
                "options": ["The number of elements in it", "The smallest n with n times the identity equal to zero", "The number of its ideals", "The order of its multiplicative group"],
                "answer": 1,
                "why": "If no such n exists the characteristic is zero, which is the case for the integers and the reals.",
            },
        ],
        "examTip": "Give the definitions in a chain: ring, commutative ring with unity, integral domain, field. Add one example at each step.",
    },

    "CSCA431-MV-T01": {
        "explanation": "Counting finds how many outcomes there are without writing them all down. The product rule says that two independent choices with m and n outcomes give m times n outcomes together. The sum rule says that two cases which cannot happen together with m and n outcomes give m plus n. When the cases overlap, the subtraction rule removes the double count, which is the inclusion exclusion idea. A tree diagram draws the choices as branches, so the count is the number of leaves. The same rules count subsets, functions between finite sets and injective functions.",
        "example": "A meal has 3 starters and 4 main courses, giving 3 times 4 which is 12 combinations. Adding 2 desserts makes it 3 times 4 times 2, which is 24.",
        "quiz": [
            {
                "q": "A code has 2 letters followed by 3 digits. With 26 letters and 10 digits, how many codes are there?",
                "options": ["26 + 10", "26 x 26 x 10 x 10 x 10", "2 x 3 x 26 x 10", "26 x 10"],
                "answer": 1,
                "why": "The product rule multiplies the number of choices at each of the five positions.",
            },
            {
                "q": "A student can take one of 4 maths courses or one of 3 physics courses, but not both. How many choices?",
                "options": ["12", "7", "4", "3"],
                "answer": 1,
                "why": "The cases cannot happen together, so the sum rule applies and the counts are added.",
            },
            {
                "q": "Which statement about counting rules is NOT correct?",
                "options": ["The product rule applies to a sequence of choices", "The sum rule applies to cases that cannot overlap", "The subtraction rule removes outcomes counted twice", "A tree diagram counts by multiplying the number of levels"],
                "answer": 3,
                "why": "A tree diagram counts by the number of leaves, which is the product of the branch counts per level.",
            },
            {
                "q": "How many functions are there from a set of 3 elements to a set of 5 elements?",
                "options": ["15", "3 to the power 5", "5 to the power 3", "3 x 5"],
                "answer": 2,
                "why": "Each of the 3 inputs may go to any of the 5 outputs, so the choices multiply to 5 cubed.",
            },
            {
                "q": "In a class of 30, 18 study maths and 12 study physics, and 5 study both. How many study at least one?",
                "options": ["30", "25", "35", "23"],
                "answer": 1,
                "why": "Inclusion exclusion gives 18 + 12 - 5, which is 25.",
            },
        ],
        "examTip": "State the product and sum rule in one line each, then show the inclusion exclusion count with numbers.",
    },

    "CSCA431-MV-T02": {
        "explanation": "The pigeonhole principle is the simple fact that more objects than boxes forces a box to hold two. In its general form, placing N objects into k boxes forces some box to hold at least the ceiling of N divided by k objects. The point of the method is choosing the boxes well, because the statement you want follows from how you set them up. Among thirteen people two share a birth month, because there are only twelve months. Among n plus 1 integers chosen from 1 to 2n, one divides another, which is proved by stripping powers of two.",
        "example": "In any group of 367 people two share a birthday, because there are only 366 possible dates. No probability is needed to say this.",
        "quiz": [
            {
                "q": "What does the simple pigeonhole principle say?",
                "options": ["n objects in n boxes fill every box", "n + 1 objects in n boxes force a box to hold two", "The objects must be identical", "The boxes must be arranged in order"],
                "answer": 1,
                "why": "One more object than there are boxes makes a shared box unavoidable.",
            },
            {
                "q": "What does the generalised principle guarantee when N objects go into k boxes?",
                "options": ["Every box holds the same number", "Some box holds at least the ceiling of N divided by k", "No box is left empty", "Some box holds exactly N divided by k"],
                "answer": 1,
                "why": "The ceiling is needed because objects are whole, so the average is rounded up.",
            },
            {
                "q": "How many people guarantee that two share a birth month?",
                "options": ["12", "13", "24", "25"],
                "answer": 1,
                "why": "With 12 months, 13 people force a shared month by the pigeonhole principle.",
            },
            {
                "q": "Which statement about the pigeonhole principle is NOT correct?",
                "options": ["It proves existence without identifying which box is shared", "Choosing the boxes well is the main skill", "It proves that some box holds at most the average", "It applies to any sequence of n squared + 1 distinct numbers"],
                "answer": 2,
                "why": "The principle guarantees a box holding at least the average, never at most it.",
            },
            {
                "q": "Any sequence of n squared + 1 distinct numbers must contain:",
                "options": ["Two equal numbers", "An increasing or decreasing subsequence of length n + 1", "A prime number", "A number divisible by n"],
                "answer": 1,
                "why": "That is the classic subsequence application, proved by attaching a pair of lengths to each term.",
            },
        ],
        "examTip": "State both forms of the principle, then give two applications: the shared birth month and the subsequence result.",
    },

    "CSCA431-MV-T03": {
        "explanation": "A permutation counts arrangements where the order matters, and a combination counts selections where it does not. Arranging r items chosen from n gives n factorial divided by n minus r factorial. When items may repeat, the count is n to the power r. Around a circle the count is n minus 1 factorial, because rotating the circle changes nothing. Choosing r items from n without caring about order gives n factorial over r factorial times n minus r factorial, read as n choose r. When repetition is allowed in a selection, the count becomes n plus r minus 1 choose r.",
        "example": "Five books can be arranged on a shelf in 5 factorial, which is 120 ways. Choosing 3 of them to take home gives 5 choose 3, which is 10 ways, because the packing order does not matter.",
        "quiz": [
            {
                "q": "How many ways can 3 books be chosen from 5 when order does not matter?",
                "options": ["60", "10", "15", "120"],
                "answer": 1,
                "why": "It is a combination, 5 choose 3, which is 5 factorial over 3 factorial times 2 factorial, giving 10.",
            },
            {
                "q": "How many ways can 5 people sit around a round table?",
                "options": ["5 factorial", "4 factorial", "5", "25"],
                "answer": 1,
                "why": "Rotations are the same arrangement, so one seat is fixed and the other 4 are arranged.",
            },
            {
                "q": "Which statement is NOT correct?",
                "options": ["Permutations count ordered arrangements", "Combinations count unordered selections", "A circular permutation of n objects is n minus 1 factorial", "The number of arrangements of r from n equals n choose r"],
                "answer": 3,
                "why": "Arrangements use n factorial over n minus r factorial, while n choose r ignores the order.",
            },
            {
                "q": "How many 4 digit PINs can be made from 10 digits if repetition is allowed?",
                "options": ["5,040", "10,000", "210", "40"],
                "answer": 1,
                "why": "Each of the four positions has 10 choices, so the count is 10 to the power 4.",
            },
            {
                "q": "In how many ways can the letters of the word CAT be arranged?",
                "options": ["3", "6", "9", "27"],
                "answer": 1,
                "why": "There are 3 distinct letters, so the count is 3 factorial, which is 6.",
            },
        ],
        "examTip": "Write the four formulas side by side: permutation, with repetition, circular and combination. Note which divide by a factorial and why.",
    },

    "CSCA431-MV-T04": {
        "explanation": "The binomial theorem expands x plus y to the n into a sum of terms. Each term is n choose k times x to the n minus k times y to the k. The coefficients are the entries of Pascal's triangle, where each entry is the sum of the two above it. That is Pascal's identity in symbols: n choose k equals n minus 1 choose k minus 1 plus n minus 1 choose k. Two identities are used constantly: symmetry, and a row sum of 2 to the n. Symmetry says n choose k equals n choose n minus k. The multinomial theorem does the same job for a sum of several terms.",
        "example": "Row 4 of Pascal's triangle is 1, 4, 6, 4, 1, which are the coefficients in the expansion of x plus y to the 4.",
        "quiz": [
            {
                "q": "What is the sum of all binomial coefficients n choose k for a fixed n?",
                "options": ["n", "n factorial", "2 to the n", "n squared"],
                "answer": 2,
                "why": "Putting x and y both equal to 1 in the binomial theorem gives 1 plus 1 to the n, which is 2 to the n.",
            },
            {
                "q": "Which identity does Pascal's triangle show?",
                "options": ["n choose k equals n choose n minus k", "n choose k equals C(n-1,k-1) + C(n-1,k)", "The sum of a row is 2 to the n", "Every row is symmetric"],
                "answer": 1,
                "why": "Each entry is the sum of the two entries above it, which is exactly Pascal's identity.",
            },
            {
                "q": "What is the coefficient of x squared y squared in the expansion of (x + y) to the 4?",
                "options": ["4", "6", "12", "1"],
                "answer": 1,
                "why": "It is 4 choose 2, which is 6, the middle entry of row 4 of Pascal's triangle.",
            },
            {
                "q": "Which statement about binomial coefficients is NOT correct?",
                "options": ["n choose 0 equals 1", "n choose k equals n choose n minus k", "The rows of Pascal's triangle are symmetric", "n choose k is largest only when k equals n"],
                "answer": 3,
                "why": "The largest entries sit in the middle of a row, and n choose n is 1, the smallest value.",
            },
            {
                "q": "Which theorem expands a power of a sum of several terms?",
                "options": ["The binomial theorem", "The multinomial theorem", "The pigeonhole principle", "The inclusion exclusion principle"],
                "answer": 1,
                "why": "Multinomial coefficients count arrangements of objects of several types, generalising the binomial case.",
            },
        ],
        "examTip": "Write the binomial theorem in sigma form, draw four rows of Pascal's triangle, then state the symmetry and sum identities.",
    },
}
