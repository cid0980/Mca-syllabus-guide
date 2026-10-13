# Cards for CSCA 412 - Module I: Introduction to C++ and User Defined Functions.
# Written from the topic definitions in src/lib/data/tree/CSCA412.json. Apply with
#   python3 scripts/archive/_apply_cards.py src/lib/data/tree/CSCA412.json scripts/archive/_cards_412a.py

CARDS = {
    "CSCA412-MI-T01": {
        "explanation": "C++ was created by Bjarne Stroustrup at Bell Labs, first as C with Classes and released under the name C++ in 1985. It keeps everything C can do, including pointers, direct memory control and close contact with the hardware, and adds classes, objects, overloading, inheritance and templates on top. Because a C++ program is compiled into machine code before it runs, it executes quickly and uses little memory at runtime. That combination is why it is used for game engines, parts of operating systems, embedded devices and competitive programming, while work that cares more about developer speed than machine speed often prefers Java or Python.",
        "example": "A live cricket scoreboard that must refresh sixty times a second cannot afford slow code. The same job written in C++ needs far fewer machine instructions than an interpreted language, so the scoreboard keeps up on cheap hardware.",
        "quiz": [
            {
                "q": "Who developed C++?",
                "options": [
                    "Dennis Ritchie",
                    "Bjarne Stroustrup",
                    "James Gosling",
                    "Guido van Rossum",
                ],
                "answer": 1,
                "why": "Stroustrup developed it at Bell Labs as C with Classes. Ritchie made C, Gosling made Java.",
            },
            {
                "q": "Which of these is NOT a feature that C++ adds on top of C?",
                "options": [
                    "Classes and objects",
                    "Automatic garbage collection",
                    "Operator overloading",
                    "Templates",
                ],
                "answer": 1,
                "why": "C++ has no automatic garbage collection. You release memory yourself with delete.",
            },
            {
                "q": "A program must run on a small microcontroller with 2 KB of memory and no operating system. Which property of C++ matters most here?",
                "options": [
                    "Its automatic memory management",
                    "Its built-in database support",
                    "Low-level memory control and a small runtime",
                    "Its rich graphics library",
                ],
                "answer": 2,
                "why": "Without an operating system the program must manage memory itself and stay small, which is what C and C++ are built for.",
            },
            {
                "q": "Which statement about C++ is correct?",
                "options": [
                    "It is an interpreted language",
                    "It cannot use pointers",
                    "It is a superset of C with object oriented features",
                    "It runs only inside a web browser",
                ],
                "answer": 2,
                "why": "C++ takes C as its base and adds classes, objects and the rest of the object oriented features.",
            },
        ],
        "examTip": "Keep three names in order: C by Ritchie, C with Classes, then C++ by Stroustrup in 1985. One mark questions ask who developed it and what it adds to C.",
    },
    "CSCA412-MI-T02": {
        "explanation": "Every C++ program is built from preprocessor directives, then optional class and function definitions, and finally the main function, which is where execution starts. In the usual skeleton, #include <iostream> brings in the input and output library, and a using namespace std; statement lets you write cin and cout without the std:: prefix. Statements sit inside braces and each one ends with a semicolon, and any missing semicolon stops the compiler on the next line. main returns an int, and returning 0 tells the operating system that the program finished without an error.",
        "example": "Open any program in your practical record: the first two lines are the include and the using statement, then int main(), then braces around the statements. The same skeleton appears in every program you write this semester.",
        "quiz": [
            {
                "q": "Where does execution of a C++ program begin?",
                "options": [
                    "At the first #include line",
                    "At the first function written in the file",
                    "In main()",
                    "At the last statement of the file",
                ],
                "answer": 2,
                "why": "main is the entry point; the linker looks for it when it builds the executable.",
            },
            {
                "q": "What does #include <iostream> do?",
                "options": [
                    "Runs the program",
                    "Copies the contents of the iostream header into the file before compilation",
                    "Declares the main function",
                    "Creates an object for you",
                ],
                "answer": 1,
                "why": "The preprocessor pastes the header text into the file so the compiler can see the declarations of cout and cin.",
            },
            {
                "q": "Which line of the skeleton is NOT required for a program to compile and run?",
                "options": [
                    "int main()",
                    "#include <iostream>",
                    "using namespace std;",
                    "the closing brace of main",
                ],
                "answer": 2,
                "why": "Without it you can still write std::cout, so it is a convenience rather than a requirement.",
            },
            {
                "q": "A student writes a full program but forgets to define main(). What does the build report?",
                "options": [
                    "The program runs and prints nothing",
                    "The linker reports that there is no entry point",
                    "The first function written runs instead",
                    "main is created automatically by the compiler",
                ],
                "answer": 1,
                "why": "Compilation succeeds, but the linker needs a main to start from and stops with an error.",
            },
        ],
        "examTip": "Write the skeleton from memory in the practical exam: include, using namespace, int main, braces, statements, return 0.",
    },
    "CSCA412-MI-T03": {
        "explanation": "Turning a source file into a running program takes four stages. The preprocessor handles lines beginning with #, such as #include and #define, and produces one expanded file; the compiler translates that file into assembly for the target processor; the assembler turns the assembly into an object file of machine code; and the linker joins your object file with the library code it uses, such as the code behind cout, to produce the executable. The stages also explain the three kinds of mistake: a missing semicolon stops the compiler, an undefined function stops the linker, and a wrong calculation is only seen when the program runs.",
        "example": "Running g++ hello.cpp -o hello on the lab machine silently performs all four stages: cpp expands the file, cc1plus compiles it, as assembles it, ld links it, and the file hello is what you run.",
        "quiz": [
            {
                "q": "Which stage joins your object file with the library code the program uses?",
                "options": ["Preprocessor", "Compiler", "Assembler", "Linker"],
                "answer": 3,
                "why": "The linker is the last stage; it resolves calls such as cout to the code in the library.",
            },
            {
                "q": "A program calls sqrt() but forgets to include <cmath>. Which stage reports the error?",
                "options": ["Preprocessor", "Compiler", "Linker", "Runtime"],
                "answer": 1,
                "why": "Without the declaration the compiler cannot check the call, so it stops before any object file is made.",
            },
            {
                "q": "The file produced by the assembler is called a:",
                "options": ["preprocessed file", "assembly file", "object file", "executable file"],
                "answer": 2,
                "why": "Assembly (.s) is the compiler's output and the assembler's input; the assembler produces the object file (.o).",
            },
            {
                "q": "A program compiles and links cleanly but divides by zero when it runs. This is a:",
                "options": ["syntax error", "linker error", "runtime error", "preprocessor error"],
                "answer": 2,
                "why": "Nothing is wrong with the text of the program, so only execution reveals the fault.",
            },
        ],
        "examTip": "Learn the order with the tool names that perform it: preprocess with cpp, compile with cc1plus, assemble with as, link with ld.",
    },
    "CSCA412-MI-T04": {
        "explanation": "The smallest unit the compiler recognises is a token: keywords such as int and return, identifiers such as marks, literals such as 21 and 'A', operators such as + and ==, and separators such as ; and the braces. Tokens are combined into expressions using variables, which reserve memory of a stated type such as int, float, double, char or bool, and constants, whose value cannot change once it is set. Control statements then decide the order in which things happen: if and switch choose a branch, for and while repeat a block, and break and continue alter those loops. Input and output are carried by cin and cout, which take values from the keyboard and send them to the screen.",
        "example": "In the line int marks = 21; the compiler sees five tokens, int, marks, =, 21 and ;, of which one is a keyword, one is an identifier you chose, one is a literal and one is an operator.",
        "quiz": [
            {
                "q": "Which of these is a keyword in C++?",
                "options": ["marks", "int", "total_marks", "MaxMarks"],
                "answer": 1,
                "why": "int is reserved by the language; the others are identifiers chosen by the programmer.",
            },
            {
                "q": "Which statement about a constant is correct?",
                "options": [
                    "It can be given a new value later in the program",
                    "Its value cannot be changed after initialisation",
                    "It must always be of type float",
                    "It cannot be used inside an expression",
                ],
                "answer": 1,
                "why": "That is the whole meaning of a constant; the compiler refuses any later assignment to it.",
            },
            {
                "q": "Which control statement repeats a block while a condition stays true?",
                "options": ["if", "switch", "while", "break"],
                "answer": 2,
                "why": "while tests its condition before each pass; break leaves a loop rather than repeating one.",
            },
            {
                "q": "Which statement about tokens is NOT correct?",
                "options": [
                    "A keyword is a token",
                    "An identifier you choose is a token",
                    "Every token must be exactly one character long",
                    "A literal such as 21 is a token",
                ],
                "answer": 2,
                "why": "A token can be many characters long: total_marks is one single identifier token.",
            },
        ],
        "examTip": "Be ready to split one line of code into tokens and to name the five token families with an example of each.",
    },
    "CSCA412-MI-T05": {
        "explanation": "C++ ships with a standard library whose functions are grouped into headers: iostream for input and output, cmath for mathematics, cstring for C style strings and cstdlib for conversions and random numbers, among others. You bring a header in with #include and then call its functions directly instead of writing that code yourself. Library functions are already tested and optimised, so using them makes a program shorter and less likely to carry a bug of your own. The trade is that you must know which header holds each function and how it behaves at the edges, for example that strlen does not count the terminating null character.",
        "example": "To find a square root you include <cmath> and call sqrt(49). That saves writing and debugging the whole numerical method yourself.",
        "quiz": [
            {
                "q": "Which header must be included to use sqrt()?",
                "options": ["iostream", "cmath", "cstring", "cstdlib"],
                "answer": 1,
                "why": "The mathematical functions, including sqrt and pow, live in cmath.",
            },
            {
                "q": "strlen(\"MCA\") returns:",
                "options": ["2", "3", "4", "0"],
                "answer": 1,
                "why": "It counts the characters up to, but not including, the null character that ends the string.",
            },
            {
                "q": "Why does using a library function save time?",
                "options": [
                    "It makes the program run on any computer",
                    "The function is already written and tested, so you reuse it instead of writing it",
                    "It removes the need for main()",
                    "It deletes syntax errors automatically",
                ],
                "answer": 1,
                "why": "Reuse of tested code is the point of a library; portability and error removal are not its promises.",
            },
            {
                "q": "Which function reads a whole line of text typed by the user into a string?",
                "options": ["getline(cin, name)", "sqrt(name)", "strlen(name)", "atoi(name)"],
                "answer": 0,
                "why": "getline takes the stream and the string; cin >> name would stop at the first space.",
            },
        ],
        "examTip": "Memorise four headers with one function each: iostream for cout, cmath for sqrt, cstring for strlen, cstdlib for atoi.",
    },
    "CSCA412-MI-T06": {
        "explanation": "A user defined function is a block of code with a name, a parameter list and a return type, written once so a task can be called as many times as needed. A declaration, or prototype, tells the compiler the name, the parameter types and the return type before the function is used; the definition supplies the body; and the call runs it with real values. The names in the declaration are formal parameters and the values passed at the call are actual parameters, and anything the function hands back travels through the return statement. A void function performs an action and returns nothing, while default arguments let the caller leave the last parameters out, and an inline function asks the compiler to place the body at the call instead of jumping to it.",
        "example": "A function that computes a student's average is written once and then called for all fifty students of a class. One body, fifty calls, and no repeated code to keep in step.",
        "quiz": [
            {
                "q": "What is the purpose of a function prototype?",
                "options": [
                    "To run the function",
                    "To tell the compiler the name, parameter types and return type before the function is used",
                    "To reserve memory for the function body",
                    "To print the result",
                ],
                "answer": 1,
                "why": "With the prototype in front of it, the compiler can check every call it later meets.",
            },
            {
                "q": "A function declared void show() must:",
                "options": ["return an int", "return nothing", "take no arguments", "be called only once"],
                "answer": 1,
                "why": "void is the return type and it means the function hands nothing back to the caller.",
            },
            {
                "q": "Which statement about default arguments is NOT correct?",
                "options": [
                    "They let the caller leave out the last arguments of a call",
                    "They must be the rightmost parameters in the list",
                    "A parameter with a default may be followed by one without a default",
                    "They are written in the prototype",
                ],
                "answer": 2,
                "why": "Once one parameter has a default, every parameter after it must have one too, otherwise a call could not be matched.",
            },
            {
                "q": "In int add(int a, int b), the names a and b are called:",
                "options": ["actual parameters", "formal parameters", "return values", "default arguments"],
                "answer": 1,
                "why": "Formal parameters appear in the definition; the values supplied at the call are the actual parameters.",
            },
        ],
        "examTip": "Tell the three part story in order: prototype before main, definition with the body, call inside main. Then swap formal and actual parameters in one written line.",
    },
    "CSCA412-MI-T07": {
        "explanation": "When a function is called, C++ normally copies the argument into the parameter, so the function works on its own copy and the caller's variable stays as it was: that is call by value. If the function must change the caller's variable, you pass it by reference using &, or by address using a pointer, and both give the function the original object instead of a copy. Both work, and the difference is in what they make visible: a reference is written like an ordinary variable and cannot be null, while a pointer shows at the call site that an address is handed over and can be tested for null. The choice also affects speed, because copying a large object costs time while a reference simply refers to the object that already exists.",
        "example": "A swap function written as swap(int &a, int &b) really exchanges the caller's two numbers, while the same function written with plain int parameters swaps two copies and the caller sees no change at all.",
        "quiz": [
            {
                "q": "Which function can change the variable in the caller?",
                "options": [
                    "void f(int x)",
                    "void f(int &x)",
                    "void f(int x) called twice with f(n)",
                    "void f(const int x)",
                ],
                "answer": 1,
                "why": "The & makes the parameter another name for the caller's variable, so writing to it writes to the original.",
            },
            {
                "q": "In call by value, the parameter and the argument:",
                "options": [
                    "share one memory location",
                    "are stored in separate memory locations",
                    "are the same variable",
                    "must both be pointers",
                ],
                "answer": 1,
                "why": "The value is copied into the parameter, which is why changes inside the function are lost on return.",
            },
            {
                "q": "A large structure is passed to a function that only reads it and never changes it. The cheapest correct choice is:",
                "options": [
                    "pass it by value",
                    "pass it by reference without allowing changes",
                    "copy it inside the function",
                    "make it a global variable",
                ],
                "answer": 1,
                "why": "A reference avoids the copy while still protecting the original if it is marked const.",
            },
            {
                "q": "Which statement about pointers is NOT correct?",
                "options": [
                    "A pointer stores an address",
                    "A pointer can hold a null value",
                    "A pointer is dereferenced with the & operator",
                    "A pointer parameter lets the function change the caller's variable",
                ],
                "answer": 2,
                "why": "& takes the address of a variable and * dereferences a pointer; the two operators do opposite jobs.",
            },
        ],
        "examTip": "One line decides the mark: value copies, reference and pointer both reach the original. Write a two line swap to prove it.",
    },
}
