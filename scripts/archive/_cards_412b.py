# Cards for CSCA 412 - Module II: Object Oriented Concepts, Classes, Overloading and Inheritance.
# Apply with
#   python3 scripts/archive/_apply_cards.py src/lib/data/tree/CSCA412.json scripts/archive/_cards_412b.py

CARDS = {
    "CSCA412-MII-T01": {
        "explanation": "Object oriented programming builds a program out of objects, where each object keeps its own data and the functions that work on that data. The style rests on a few ideas: encapsulation keeps data and code together and hides what the outside does not need; abstraction shows only the essential behaviour of a thing; inheritance lets one class reuse and extend another; and polymorphism lets the same call behave differently for different objects. In the procedural style, data and functions are separate and the data is passed from function to function, so any function can change anything. Keeping the responsibility inside the class that owns the data is what makes an object oriented program easier to extend without breaking what already works.",
        "example": "In a college portal, a Student object holds its own roll number and marks and knows how to print its own result. The portal never needs to know how student data is stored, only that it can ask the object for a result.",
        "quiz": [
            {
                "q": "Which feature keeps data and the functions that operate on it inside one unit?",
                "options": ["Encapsulation", "Recursion", "Compilation", "Indexing"],
                "answer": 0,
                "why": "Encapsulation is exactly that bundling, and it also decides what the outside may see.",
            },
            {
                "q": "Which of these is NOT one of the four pillars of object oriented programming?",
                "options": ["Encapsulation", "Polymorphism", "Recursion", "Inheritance"],
                "answer": 2,
                "why": "Recursion is a programming technique found in every style; the pillars are encapsulation, abstraction, inheritance and polymorphism.",
            },
            {
                "q": "In the procedural style, data and the functions that use it are usually:",
                "options": [
                    "kept inside one class",
                    "separate, with the data passed to the functions",
                    "always hidden from the program",
                    "stored inside objects",
                ],
                "answer": 1,
                "why": "Procedural programs keep data in variables and pass it to functions; keeping them together is the object oriented answer.",
            },
            {
                "q": "A program adds a new type of bank account without touching the existing account classes. Which two object oriented features make that possible?",
                "options": [
                    "Inheritance and polymorphism",
                    "Preprocessor directives and headers",
                    "Compilation and linking",
                    "Data hiding on its own",
                ],
                "answer": 0,
                "why": "The new class inherits the common behaviour and can be used wherever the base type was expected.",
            },
        ],
        "examTip": "Learn the four pillars with one line and one example each; questions usually ask you to name them and match a definition to each.",
    },
    "CSCA412-MII-T02": {
        "explanation": "A class is a user defined type that declares data members and member functions together, and an object is one instance of that class, with its own copy of the data members. Access specifiers decide who may see what: private members are reachable only inside the class, public members form its interface to the rest of the program, and protected members are for the class and the classes derived from it. A member function written inside the class definition is implicitly inline, while one defined outside uses the scope resolution operator :: as in Box::volume(). Inside a member function the this pointer holds the address of the object on which the function was called, which is how the function knows whose data to use when two objects of the same class both exist.",
        "example": "class Student { private: int roll; public: void setRoll(int r) { roll = r; } }; gives one class, and then Student s1, s2 creates two objects, each carrying its own roll number.",
        "quiz": [
            {
                "q": "What is the default access for members of a class (not a struct)?",
                "options": ["public", "private", "protected", "there is no default"],
                "answer": 1,
                "why": "In a class the default is private, which is the opposite of a struct where it is public.",
            },
            {
                "q": "Which operator is used to define a member function outside the class?",
                "options": ["the dot operator", "the scope resolution operator ::", "the arrow operator ->", "the hash symbol #"],
                "answer": 1,
                "why": "void Box::volume() tells the compiler which class the function belongs to.",
            },
            {
                "q": "Which statement about the this pointer is NOT correct?",
                "options": [
                    "It points to the object that called the member function",
                    "It is available inside every non-static member function",
                    "It must be declared by the programmer inside the class",
                    "It is used when a parameter name hides a member name",
                ],
                "answer": 2,
                "why": "this is supplied automatically by the compiler; you never declare it.",
            },
            {
                "q": "A class has two int members and one double member. How much memory does one object need, taking int as 4 bytes and double as 8 bytes and ignoring padding?",
                "options": ["8 bytes", "12 bytes", "16 bytes", "20 bytes"],
                "answer": 2,
                "why": "Two ints take 8 bytes and the double takes 8 more, so 16 bytes in total.",
            },
        ],
        "examTip": "Write a small class from memory with private data and public getters and setters; one mark is kept for the correct access specifiers and one for the operator used outside the class.",
    },
    "CSCA412-MII-T03": {
        "explanation": "Normally every object of a class has its own copy of each data member, but a static data member belongs to the class itself and is shared by all objects. It is declared inside the class with the keyword static and then defined once outside the class, because the declaration alone does not set aside storage. A static member function is also tied to the class rather than to an object, so it can be called as ClassName::function() before any object exists, and for that reason it has no this pointer and cannot use non-static members directly. The usual purpose is shared bookkeeping, such as counting how many objects exist or holding one setting that every object must obey.",
        "example": "A Counter class with a static integer count increases count in its constructor and decreases it in its destructor, so the class can always say how many Counter objects are alive at that moment, no matter which object is asked.",
        "quiz": [
            {
                "q": "A class has ten objects and one static data member. How many copies of that member exist?",
                "options": ["Ten", "One", "None until it is used", "One copy per module"],
                "answer": 1,
                "why": "A static member belongs to the class, so all ten objects share the single copy.",
            },
            {
                "q": "A static member function can directly use:",
                "options": [
                    "only static members of the class",
                    "any member of any object",
                    "the this pointer",
                    "private members of other classes",
                ],
                "answer": 0,
                "why": "Without an object there is no this, so only members that belong to the class itself are reachable.",
            },
            {
                "q": "Which statement about static members is NOT correct?",
                "options": [
                    "A static data member is shared by all objects of the class",
                    "A static data member is defined outside the class",
                    "A static member function can be called without an object",
                    "Each object keeps its own private copy of a static data member",
                ],
                "answer": 3,
                "why": "That is the definition of a non-static member; the whole point of static is that there is one shared copy.",
            },
            {
                "q": "Which job suits a static member best?",
                "options": [
                    "Storing each student's marks",
                    "Counting how many objects of the class have been created",
                    "Drawing a window on the screen",
                    "Reading one line from a file",
                ],
                "answer": 1,
                "why": "A count that all objects must update is exactly the shared state a static member exists for.",
            },
        ],
        "examTip": "Never forget the outside definition. static int count; inside the class and nothing outside gives a linker error, a favourite one mark question.",
    },
    "CSCA412-MII-T04": {
        "explanation": "A constructor is a special member function with the same name as its class, no return type at all, which runs automatically when an object is created so that the object starts in a valid state. A class may have several constructors, a default one with no arguments, a parameterised one, a copy constructor, and a dynamic one that allocates memory with new, and the compiler picks whichever matches the arguments. The copy constructor takes a reference to another object of the same class and is used when an object is initialised from an existing one, including when an object is passed or returned by value. A destructor is written with a leading tilde and takes no arguments; it runs automatically when the object goes out of scope or is deleted, and it is where memory or open files are released, with destructors running in the reverse order of construction.",
        "example": "A BankAccount constructor takes the opening balance, so no account can ever be created with an unknown balance, and the destructor writes the closing entry to a file when the object is destroyed.",
        "quiz": [
            {
                "q": "Which is true of a constructor?",
                "options": [
                    "It must be declared as returning void",
                    "It has no return type at all",
                    "It must be private",
                    "It can be called by name after the object exists",
                ],
                "answer": 1,
                "why": "A constructor is not allowed to state a return type, not even void, and it is called automatically at creation.",
            },
            {
                "q": "The copy constructor is called when:",
                "options": [
                    "an object is initialised from another object of the same class",
                    "a static data member is defined",
                    "the class is compiled",
                    "a private member is read by a friend function",
                ],
                "answer": 0,
                "why": "That includes passing an object by value and returning one by value, both of which build a copy.",
            },
            {
                "q": "Which statement about destructors is NOT correct?",
                "options": [
                    "A destructor takes no arguments",
                    "A destructor cannot be overloaded",
                    "A destructor must specify a return type of int",
                    "A destructor can release memory obtained with new",
                ],
                "answer": 2,
                "why": "Like a constructor, a destructor has no return type; it only runs the cleanup code you write.",
            },
            {
                "q": "A class defines only a parameterised constructor. What happens to the default constructor?",
                "options": [
                    "The compiler still creates one",
                    "It no longer exists unless you write one yourself",
                    "It is inherited from the base class",
                    "It becomes static",
                ],
                "answer": 1,
                "why": "Declaring any constructor stops the automatic default constructor, so writing new Student() would fail.",
            },
        ],
        "examTip": "Three lines answer most constructor questions: same name as the class, no return type, called automatically. Add the copy constructor situations as a second point.",
    },
    "CSCA412-MII-T05": {
        "explanation": "Operator overloading gives an existing operator such as + or << a meaning for a user defined type, so that Complex c3 = c1 + c2; reads exactly like ordinary arithmetic. The function is named with the keyword operator followed by the symbol, and is written either as a member function, where the left operand is the calling object and only the right operand is a parameter, or as a friend function taking both operands. The rules are strict: no new operators can be invented, and the precedence, associativity and number of operands of an existing operator cannot be changed, while at least one operand must be of a user defined type so that built-in types keep their normal meaning. Conversions work alongside it, since a constructor with one argument can turn a basic value into a class object and a conversion function can turn a class object back into a basic value.",
        "example": "A Matrix class that overloads + and * lets a program multiply two matrices as A * B, which reads like the algebra in the textbook instead of a nest of function calls.",
        "quiz": [
            {
                "q": "Which operator cannot be overloaded in C++?",
                "options": ["+", "::", "<<", "=="],
                "answer": 1,
                "why": "The scope resolution operator, along with the dot operator, .*, ?: and sizeof, is on the forbidden list.",
            },
            {
                "q": "Overloading an operator can change:",
                "options": [
                    "its precedence",
                    "its number of operands",
                    "what the operator means for a user defined type",
                    "its associativity",
                ],
                "answer": 2,
                "why": "Precedence, associativity and arity are fixed by the language; only the meaning for your own type changes.",
            },
            {
                "q": "Which statement about overloaded operators is NOT correct?",
                "options": [
                    "At least one operand must be of a user defined type",
                    "A member operator+ takes one explicit parameter",
                    "A friend operator+ takes two parameters",
                    "Overloading can change how + behaves for two ints",
                ],
                "answer": 3,
                "why": "Built-in types keep their meaning, which is why at least one operand must be a class or structure type.",
            },
            {
                "q": "The statement Complex c = 5; works when the class has:",
                "options": [
                    "a default constructor",
                    "a constructor taking one argument",
                    "a destructor",
                    "a static data member",
                ],
                "answer": 1,
                "why": "The single argument constructor converts the int into a Complex object, which is the basic to class conversion.",
            },
        ],
        "examTip": "Two lines cover most questions: the five operators you cannot overload, and the rule that precedence, associativity and arity stay as they are.",
    },
    "CSCA412-MII-T06": {
        "explanation": "Function overloading lets several functions share one name as long as their parameter lists differ in number, type or order of parameters; changing only the return type is not enough. A friend function is not a member of the class but is granted access to its private and protected members, which is useful for an operator such as << whose left operand is the stream and not your object. A virtual function is one whose binding is delayed until the program runs: calling it through a pointer or reference to the base class runs the version belonging to the object that is actually there, which is runtime polymorphism, while a non-virtual call is fixed at compile time from the type of the pointer. A pure virtual function, written with = 0, has no body at all and makes the class abstract, so no object of that class can be created even though pointers of that type can still be used.",
        "example": "A Shape base class with a pure virtual area(), and Circle and Rectangle that override it. One loop over Shape pointers prints the correct area for each shape without a single if statement to check the kind.",
        "quiz": [
            {
                "q": "Two functions can share the same name only when they differ in:",
                "options": [
                    "the return type alone",
                    "the number, type or order of their parameters",
                    "the access specifier",
                    "whether they are static",
                ],
                "answer": 1,
                "why": "The compiler chooses by matching arguments, so the parameter list must be different.",
            },
            {
                "q": "A friend function of a class:",
                "options": [
                    "is a member of that class",
                    "can access the private members of the class that declares it",
                    "must be declared static",
                    "is inherited by derived classes",
                ],
                "answer": 1,
                "why": "Friendship grants access without membership, and it is not inherited.",
            },
            {
                "q": "Which statement about virtual functions is NOT correct?",
                "options": [
                    "They give runtime polymorphism",
                    "They run the version belonging to the actual object behind a base pointer",
                    "A pure virtual function makes a class abstract",
                    "A virtual function cannot be overridden in a derived class",
                ],
                "answer": 3,
                "why": "Overriding in the derived class is exactly how a virtual function becomes useful.",
            },
            {
                "q": "Dynamic binding means the function to run is decided:",
                "options": [
                    "at compile time",
                    "at runtime, from the actual type of the object",
                    "by the linker",
                    "by the preprocessor",
                ],
                "answer": 1,
                "why": "The virtual table is used at runtime, which is why the pointer type does not decide the outcome.",
            },
        ],
        "examTip": "One line tells the trio apart: overloading is one name with different parameters, friend is access without membership, virtual is binding at run time.",
    },
    "CSCA412-MII-T07": {
        "explanation": "Inheritance builds a new class from an existing one: the derived class automatically has the members of the base class and may add its own, which expresses an is-a relationship such as a Manager is an Employee. C++ supports single inheritance, multiple inheritance from two or more bases, multilevel inheritance in a chain, hierarchical inheritance with one base and many children, and hybrid combinations of these. When two base classes share a common ancestor, the derived object ends up holding two copies of that ancestor and the compiler cannot decide which to use, which is the diamond problem, and it is solved by making the common ancestor a virtual base class. Constructors run base first and then derived, while destructors run in the opposite order, so a derived object is always built on a base that is already complete.",
        "example": "Vehicle as the base, with Car and Bike derived from it, and ElectricCar derived from Car. The wheels and engine members are written once in Vehicle and reused down the chain instead of being repeated in every class.",
        "quiz": [
            {
                "q": "Inheritance expresses which kind of relationship?",
                "options": ["is-a", "has-a", "uses-a", "part-of"],
                "answer": 0,
                "why": "A derived object is a kind of the base object, such as a Car is a Vehicle.",
            },
            {
                "q": "The diamond problem in multiple inheritance is solved by:",
                "options": [
                    "making the common base class a virtual base class",
                    "adding a friend function to the derived class",
                    "overloading the constructor",
                    "making all members private",
                ],
                "answer": 0,
                "why": "A virtual base gives the derived object one shared copy of the common ancestor instead of two.",
            },
            {
                "q": "Which statement about construction order is NOT correct?",
                "options": [
                    "The base class constructor runs before the derived class constructor",
                    "The derived class destructor runs before the base class destructor",
                    "Constructors and destructors of a hierarchy run in the same order",
                    "The base part of a derived object is completed first",
                ],
                "answer": 2,
                "why": "Construction goes from base to derived and destruction runs backwards, from derived to base.",
            },
            {
                "q": "A base class has ten members and a derived class adds two int members. An object of the derived class contains:",
                "options": [
                    "only the two new members",
                    "all the base members plus the new members",
                    "only the public members of the base",
                    "a separate base object that is not part of it",
                ],
                "answer": 1,
                "why": "A derived object carries its own base part, so all the base members are present in it.",
            },
        ],
        "examTip": "Draw the five inheritance shapes as small trees, and remember the pair diamond problem and virtual base class; that is the usual two mark part.",
    },
}
