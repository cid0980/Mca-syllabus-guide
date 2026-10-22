# CSCA 512 Internet and Web Technologies - Module III
# JavaScript core, functions, built-in objects, the DOM, events, windows and form validation.

CODE = "CSCA512"

CARDS = {
    "CSCA512-MIII-T01": {
        "explanation": "JavaScript is the scripting language of the browser, and it is what makes a page interactive. It can also run outside the browser nowadays, on a server through Node.js. The language is interpreted, dynamically typed and object based, and it is event driven with a single thread and an event loop. Code reaches a page in three ways: inline handlers, a script element, or an external file. External files are preferred, and defer or async control when the code runs. Its strengths are instant validation and rich interfaces. Its limits are browser differences and the fact that the user can see the code.",
        "example": "A page that checks a mobile number as you type is using JavaScript. The same check could run on the server, but not instantly.",
        "quiz": [
            {
                "q": "Where can JavaScript run besides the browser?",
                "options": ["Only in the browser", "On a server through Node.js", "Inside a CSS file", "Inside a database"],
                "answer": 1,
                "why": "Node.js runs the same language outside the browser, which is why it is used for servers.",
            },
            {
                "q": "What does defer do on a script tag?",
                "options": ["Stops the script running", "Runs the script after the document is parsed", "Loads the script twice", "Compresses the script"],
                "answer": 1,
                "why": "Deferred scripts run in order once the page structure exists, so they can find elements.",
            },
            {
                "q": "Which statement about JavaScript is NOT correct?",
                "options": ["It is event driven", "It is dynamically typed", "It uses a single thread with an event loop", "It is the same language as Java"],
                "answer": 3,
                "why": "The shared name is a historical accident; the two languages are quite different.",
            },
            {
                "q": "Which is a limitation of client side JavaScript?",
                "options": ["It cannot validate forms", "The user can see and modify the code", "It cannot respond to events", "It cannot change the page"],
                "answer": 1,
                "why": "Anything that runs in the browser is under the user's control, so the server must recheck.",
            },
            {
                "q": "What is the preferred way to add JavaScript to a page?",
                "options": ["An external file", "An inline handler", "A style attribute", "A meta tag"],
                "answer": 0,
                "why": "An external file can be cached, reused across pages and kept out of the markup.",
            },
        ],
        "examTip": "Say where JavaScript runs, list its core features, the three ways to include it, and one limit.",
    },

    "CSCA512-MIII-T02": {
        "explanation": "JavaScript values are either primitive or objects. The primitive types are string, number, bigint, boolean, undefined, null and symbol, and everything else, including arrays and functions, is an object. Variables are declared with var, let or const, and the difference matters. var is function scoped and hoisted, let is block scoped, and const cannot be reassigned. Operators build expressions out of values: arithmetic, comparison, logical, assignment, ternary and typeof. Comparison has a trap, because the double equals operator converts types before comparing while the triple equals does not. Control flow uses if, else, switch, for, while, do while, for of and for in, with break, continue and try catch finally.",
        "example": "The expression 5 == '5' is true, but 5 === '5' is false. That difference causes a surprising number of bugs.",
        "quiz": [
            {
                "q": "What is the difference between let and var?",
                "options": ["They are identical", "let is block scoped, var is function scoped and hoisted", "var cannot be reassigned", "let is the older keyword"],
                "answer": 1,
                "why": "Block scoping keeps a variable inside the braces where it was declared, which avoids surprises.",
            },
            {
                "q": "Which of these is a primitive type?",
                "options": ["Array", "Object", "Symbol", "Function"],
                "answer": 2,
                "why": "Arrays, objects and functions are object types, while symbol is one of the primitives.",
            },
            {
                "q": "Which statement about JavaScript is NOT correct?",
                "options": ["const prevents reassignment of the binding", "typeof returns the type of a value", "The triple equals operator compares without converting types", "undefined and null are the same value"],
                "answer": 3,
                "why": "undefined means a variable has no value, while null is a value meaning no object.",
            },
            {
                "q": "What does the ternary operator do?",
                "options": ["Loops over an array", "Chooses one of two values based on a condition", "Declares a variable", "Converts a string"],
                "answer": 1,
                "why": "It is a compact form of if and else that produces a value.",
            },
            {
                "q": "Which loop iterates over the values of an array?",
                "options": ["for in", "for of", "while", "switch"],
                "answer": 1,
                "why": "for of gives the values, while for in walks the property names of an object.",
            },
        ],
        "examTip": "List the primitive types, compare var, let and const, explain == versus ===, and name four loops.",
    },

    "CSCA512-MIII-T03": {
        "explanation": "A function is a reusable block of code that may take parameters and return a value. A function declaration is hoisted, so it can be called before it appears in the file. A function expression assigned to a variable cannot be called that way. Parameters receive the arguments, the arguments object holds them all, and return sends a value back, with undefined as the default. Scope decides what a function can see. A closure is a function that remembers the variables of the one that created it. Arrow functions give shorter syntax with lexical this, so they are common as callbacks. Modern syntax adds rest, spread and default parameters.",
        "example": "A counter built with a closure keeps its own count. Two counters made the same way never share that number.",
        "quiz": [
            {
                "q": "What is a closure?",
                "options": ["A way to end a function", "A function that remembers the variables of the function that created it", "A syntax error", "A type of loop"],
                "answer": 1,
                "why": "The inner function keeps a reference to the outer scope, so the value survives the call.",
            },
            {
                "q": "What does a function return if there is no return statement?",
                "options": ["null", "undefined", "0", "An empty string"],
                "answer": 1,
                "why": "Every function returns something, and without a return the value is undefined.",
            },
            {
                "q": "Which statement about functions is NOT correct?",
                "options": ["Function declarations are hoisted", "Arrow functions have lexical this", "A function expression can be stored in a variable", "Parameters and scope are the same thing"],
                "answer": 3,
                "why": "Parameters are the names receiving arguments, while scope is about what is visible inside.",
            },
            {
                "q": "What does the rest parameter do?",
                "options": ["Stops the function", "Collects the remaining arguments into an array", "Repeats the function", "Returns the last value"],
                "answer": 1,
                "why": "It lets a function accept any number of arguments without naming them all.",
            },
            {
                "q": "Why is an arrow function often used as a callback?",
                "options": ["It always runs faster", "It keeps the surrounding this value instead of rebinding it", "It can return nothing", "It is hoisted"],
                "answer": 1,
                "why": "Lexical this avoids the old workaround of storing this in another variable.",
            },
        ],
        "examTip": "Compare declaration and expression, define closure and arrow function, and explain return, rest and spread.",
    },

    "CSCA512-MIII-T04": {
        "explanation": "JavaScript supplies built-in objects for structured data, dates and mathematics. An object stores key value pairs, and its properties and methods are reached with a dot or with square brackets. An array is an ordered collection with two families of methods. push, pop, shift, unshift and splice change the array itself. slice, map, filter and reduce return something new. Strings have their own methods, including length, indexOf, slice, split, replace and trim. The Date object handles dates and times, and the Math object supplies round, floor, ceil, abs, pow, sqrt, random, min and max. Regular expressions add pattern matching through test, match, replace and split.",
        "example": "Filtering a list of marks above 60 is one line with filter. Sorting needs a compare function, because sort compares strings by default.",
        "quiz": [
            {
                "q": "Which array method returns a new array instead of changing the original?",
                "options": ["push", "splice", "map", "pop"],
                "answer": 2,
                "why": "map, filter and slice leave the original alone, which makes them safer to use.",
            },
            {
                "q": "How are object properties accessed?",
                "options": ["Only with a dot", "With a dot or with square brackets", "Only with parentheses", "With a colon"],
                "answer": 1,
                "why": "Bracket notation also allows a property name held in a variable.",
            },
            {
                "q": "Which statement about built-in objects is NOT correct?",
                "options": ["sort arranges elements in place", "Math.random returns a number below one", "Date objects can be compared by subtraction", "split joins array elements into a string"],
                "answer": 3,
                "why": "split breaks a string into an array, while join does the opposite.",
            },
            {
                "q": "Which Math method rounds down to the nearest integer?",
                "options": ["Math.round", "Math.floor", "Math.ceil", "Math.abs"],
                "answer": 1,
                "why": "floor rounds down, ceil rounds up and round goes to the nearest.",
            },
            {
                "q": "Which method tests whether a string matches a pattern?",
                "options": ["match", "test", "replace", "slice"],
                "answer": 1,
                "why": "A regular expression's test method returns true or false, which suits validation.",
            },
        ],
        "examTip": "List four array methods of each family, four string methods, and the roles of Date, Math and regex.",
    },

    "CSCA512-MIII-T05": {
        "explanation": "The DOM is a tree representation of the page that JavaScript can read and change. Elements, attributes and text become nodes in a hierarchy under the document node. Elements are found with getElementById, getElementsByClassName, getElementsByTagName, querySelector and querySelectorAll. Content is then changed with innerHTML, textContent and setAttribute, while classList and style handle appearance. New nodes are built with createElement and placed with appendChild or insertBefore, and removed with removeChild. Traversal moves around the tree using parentNode, children, firstElementChild, nextElementSibling and closest.",
        "example": "A shopping list app adds an item by creating an li element, setting its text and appending it to the ul.",
        "quiz": [
            {
                "q": "Which method returns the first element matching a CSS selector?",
                "options": ["getElementById", "querySelector", "querySelectorAll", "getElementsByTagName"],
                "answer": 1,
                "why": "querySelector takes any CSS selector and returns the first match, or null.",
            },
            {
                "q": "Which property should be used to insert plain text safely?",
                "options": ["innerHTML", "textContent", "value", "outerHTML"],
                "answer": 1,
                "why": "textContent treats the value as text, so it cannot inject markup the way innerHTML can.",
            },
            {
                "q": "Which statement about the DOM is NOT correct?",
                "options": ["The DOM is a tree of nodes", "createElement makes a new element", "appendChild attaches a node to a parent", "The DOM is the same thing as the HTML source file"],
                "answer": 3,
                "why": "The DOM is the live object the browser builds from the source, and script can change it.",
            },
            {
                "q": "Which method removes a node from its parent?",
                "options": ["removeChild", "cloneNode", "insertBefore", "createElement"],
                "answer": 0,
                "why": "removeChild is called on the parent and takes the node to be removed.",
            },
            {
                "q": "What does closest do?",
                "options": ["Finds the nearest child", "Walks up to the nearest ancestor matching a selector", "Compares two nodes", "Finds the previous sibling"],
                "answer": 1,
                "why": "It starts at the element and searches upwards, which is handy in event handlers.",
            },
        ],
        "examTip": "Explain the DOM tree, list three selection methods, three change methods and three traversal properties.",
    },

    "CSCA512-MIII-T06": {
        "explanation": "Event handling lets a page respond to clicks, typing, scrolling and the rest. The browser passes an event object that carries the type, the target, the coordinates, the key pressed and any modifier keys. Handlers can be attached as an inline attribute, a property, or with addEventListener. addEventListener is preferred, because several listeners can then coexist. Events travel in three phases: capture down to the target, the target itself, then bubble back up. Calling stopPropagation ends that journey. Event delegation puts one listener on a parent and lets it handle events from many children. Form work often calls preventDefault to stop submission while validation runs.",
        "example": "One listener on a table can handle clicks on any row. Adding a listener to every row would waste memory and break for new rows.",
        "quiz": [
            {
                "q": "Why is addEventListener preferred over onclick?",
                "options": ["It is faster", "Several listeners can be attached and removed cleanly", "It works without a browser", "It is the only one that fires"],
                "answer": 1,
                "why": "A property holds one handler at a time, while listeners accumulate and can be removed.",
            },
            {
                "q": "What is event delegation?",
                "options": ["Passing an event to the server", "One listener on a parent handling events from many children", "Writing events in HTML", "Blocking an event"],
                "answer": 1,
                "why": "Events bubble up, so the parent can inspect the target and act accordingly.",
            },
            {
                "q": "Which statement about events is NOT correct?",
                "options": ["The event object carries the target", "Events bubble back up the tree", "preventDefault stops the default action", "Bubbling happens before the capture phase"],
                "answer": 3,
                "why": "Capture runs first on the way down, then the target, then bubbling on the way up.",
            },
            {
                "q": "Which event fires while a user types in a field?",
                "options": ["click", "input", "load", "scroll"],
                "answer": 1,
                "why": "input fires on every change to the value, which suits live validation.",
            },
            {
                "q": "What does stopPropagation do?",
                "options": ["Reloads the page", "Stops the event travelling further through the tree", "Deletes the handler", "Cancels the default action"],
                "answer": 1,
                "why": "It halts capture and bubbling, while preventDefault stops the browser's own action.",
            },
        ],
        "examTip": "Name three ways to attach a handler, the three event phases, and explain delegation and preventDefault.",
    },

    "CSCA512-MIII-T07": {
        "explanation": "The window object is the top of the browser object model, and it can open, close, move and resize windows. It also supplies the dialogs alert, confirm and prompt, and the timers setTimeout and setInterval. Around it sit other useful objects: navigator describes the browser, screen the display, history the visited pages and location the current URL. Assigning to location.href redirects the browser to a new page. Frames and iframes are reachable as collections. A script may reach into the document of a frame from the same origin. Timers are what drive repeated updates and simple animation.",
        "example": "A page that asks for confirmation before deleting uses confirm. A banner that changes every five seconds uses setInterval.",
        "quiz": [
            {
                "q": "Which object holds the current URL?",
                "options": ["navigator", "screen", "history", "location"],
                "answer": 3,
                "why": "location exposes the URL, and assigning to its href navigates somewhere else.",
            },
            {
                "q": "What is the difference between setTimeout and setInterval?",
                "options": ["They are the same", "setTimeout runs once after a delay, setInterval repeats", "setInterval is faster", "setTimeout cannot be cancelled"],
                "answer": 1,
                "why": "setTimeout fires once, while setInterval keeps firing until it is cleared.",
            },
            {
                "q": "Which statement about windows is NOT correct?",
                "options": ["alert shows a message box", "confirm returns true or false", "prompt asks for text input", "Scripts may freely read any frame from any site"],
                "answer": 3,
                "why": "The same origin policy blocks access to documents from a different origin.",
            },
            {
                "q": "Which object describes the display size?",
                "options": ["navigator", "screen", "history", "document"],
                "answer": 1,
                "why": "screen reports the display, while navigator reports the browser itself.",
            },
            {
                "q": "What does history.back do?",
                "options": ["Reloads the page", "Goes to the previous page in the session history", "Closes the window", "Clears the cache"],
                "answer": 1,
                "why": "The history object lets scripts move backwards and forwards through visited pages.",
            },
        ],
        "examTip": "List five window methods, describe navigator, screen, history and location, and give the same origin rule.",
    },

    "CSCA512-MIII-T08": {
        "explanation": "Forms are checked in the browser before submission, which saves the server work and gives the user instant feedback. A script reaches the controls through document.forms, element names or a selector. It then reads value, checked or the selected options. Validation checks the usual things: empty fields, lengths, patterns with regular expressions and numeric ranges. The checks are wired to events such as onsubmit, onblur and oninput, and error messages are placed next to the field that failed. Client side validation is fast and helpful, but it can be bypassed, so the server must validate every value again.",
        "example": "A form that checks the PIN code with a regular expression can warn about the format the moment the user leaves the field.",
        "quiz": [
            {
                "q": "Why is client side validation still not enough?",
                "options": ["It is too slow", "It can be bypassed, so the server must check again", "It cannot read values", "It works only on phones"],
                "answer": 1,
                "why": "Anything in the browser is under the user's control, including the checks themselves.",
            },
            {
                "q": "Which event fires when a field loses focus?",
                "options": ["onsubmit", "onblur", "oninput", "onload"],
                "answer": 1,
                "why": "onblur is the usual place to validate one field as soon as the user leaves it.",
            },
            {
                "q": "Which statement about form validation is NOT correct?",
                "options": ["Values are read with the value property", "Regular expressions can test a pattern", "Error messages belong near the field", "Server validation is optional if the browser checks"],
                "answer": 3,
                "why": "Server side validation is mandatory, because the browser's checks can be turned off.",
            },
            {
                "q": "How is the state of a checkbox read?",
                "options": ["With value", "With the checked property", "With the name attribute", "With the action attribute"],
                "answer": 1,
                "why": "checked is a boolean, while value is the text sent when the box is ticked.",
            },
            {
                "q": "What does preventDefault do in a submit handler?",
                "options": ["Clears the form", "Stops the form submitting so the script can decide", "Reloads the page", "Sends the data twice"],
                "answer": 1,
                "why": "The handler can then allow submission only if every check passes.",
            },
        ],
        "examTip": "Describe reading form values, name three checks and three events, and say why server validation is required.",
    },
}
