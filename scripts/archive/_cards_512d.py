# CSCA 512 Internet and Web Technologies - Modules IV and V
# Browser objects, OOP in JavaScript, JSON, jQuery, AJAX, PHP and MySQL.

CODE = "CSCA512"

CARDS = {
    "CSCA512-MIV-T01": {
        "explanation": "The browser object model gathers the objects the browser exposes: window, document, navigator, screen, history and location. Storage comes in two flavours. Cookies are small pieces of data sent with every request. localStorage and sessionStorage keep data in the browser only. Media is handled by elements and objects too. Images, audio and video can be played, paused, moved with currentTime and set to a volume. Graphics come in two styles: canvas draws pixels through a two dimensional context, while SVG describes vector shapes as XML. Beyond that, geolocation, drag and drop and the file reader API extend what a page can do.",
        "example": "A quiz site keeps unfinished answers in localStorage so a student can close the tab and return to them later.",
        "quiz": [
            {
                "q": "What is the difference between cookies and localStorage?",
                "options": ["They are identical", "Cookies are sent with every request, localStorage stays in the browser", "localStorage expires after a day", "Cookies always hold more data"],
                "answer": 1,
                "why": "Cookies travel to the server each time, while web storage never leaves the browser.",
            },
            {
                "q": "Which draws vector graphics as XML?",
                "options": ["canvas", "SVG", "WebGL", "WebP"],
                "answer": 1,
                "why": "SVG describes shapes that stay sharp, while canvas paints pixels that are then fixed.",
            },
            {
                "q": "Which statement about browser storage is NOT correct?",
                "options": ["Cookies are limited in size", "sessionStorage is cleared when the tab closes", "localStorage persists until it is cleared", "Web storage data is sent to the server with each request"],
                "answer": 3,
                "why": "Avoiding that round trip is the point of web storage, which is why it suits larger data.",
            },
            {
                "q": "Which API reports the user's position?",
                "options": ["The file reader API", "The geolocation API", "The history API", "The canvas API"],
                "answer": 1,
                "why": "Geolocation asks permission and then returns coordinates to the page.",
            },
            {
                "q": "Which collection of objects makes up the BOM?",
                "options": ["window, document, navigator, screen, history and location", "head, body and title", "table, tr and td", "class, id and style"],
                "answer": 0,
                "why": "These objects describe the browser and the page rather than the HTML tags.",
            },
        ],
        "examTip": "Name the BOM objects, compare cookies with web storage, and describe canvas, SVG and media control.",
    },

    "CSCA512-MIV-T02": {
        "explanation": "JavaScript objects are built on prototypes, and modern class syntax sits on top of that foundation. The older way uses a constructor function called with new. Inside it, this refers to the new object and shared methods go on the prototype. Every object links up a prototype chain to Object.prototype, and that chain is how properties are inherited. Encapsulation is achieved with closures or with private fields written with a hash prefix. The class keyword gives a cleaner syntax with a constructor, methods, getters and setters, and static members. Inheritance uses extends and super, and a subclass may override a parent method, with the most derived version being called.",
        "example": "A Student class extends Person. Calling super in the constructor sets the name, and the subclass adds a roll number.",
        "quiz": [
            {
                "q": "What does the new keyword do?",
                "options": ["Creates a variable", "Creates an object and calls the constructor with this bound to it", "Imports a module", "Copies a class"],
                "answer": 1,
                "why": "new makes a fresh object, sets its prototype and returns it from the constructor.",
            },
            {
                "q": "How is inheritance written with class syntax?",
                "options": ["With the prototype keyword", "With extends and super", "With the new keyword only", "With a getter"],
                "answer": 1,
                "why": "extends creates the subclass and super calls the parent constructor or method.",
            },
            {
                "q": "Which statement about JavaScript objects is NOT correct?",
                "options": ["Objects inherit through a prototype chain", "class syntax is sugar over prototypes", "Private fields are written with a hash prefix", "Every object has its own copy of every method"],
                "answer": 3,
                "why": "Methods live on the prototype and are shared, which is why they are defined there.",
            },
            {
                "q": "What is polymorphism in this context?",
                "options": ["Many classes in one file", "A subclass replacing a parent method with its own version", "A class with many constructors", "A method with many parameters"],
                "answer": 1,
                "why": "The same call reaches different code depending on the object it is made on.",
            },
            {
                "q": "What does a static member belong to?",
                "options": ["One instance", "The class itself rather than an instance", "The prototype chain", "The window object"],
                "answer": 1,
                "why": "A static member is reached through the class name, not through an object made from it.",
            },
        ],
        "examTip": "Explain prototypes, compare constructors and class syntax, and describe inheritance and overriding.",
    },

    "CSCA512-MIV-T03": {
        "explanation": "JSON is a text format for exchanging structured data between a browser and a server. Its syntax is deliberately small: objects with quoted keys, arrays, strings, numbers, and the literals true, false and null. Functions and comments are not allowed, and keys must be written in double quotes. Two methods do the conversion: JSON.parse turns a JSON string into a JavaScript object, and JSON.stringify does the reverse. Compared with XML it is lighter, easier to read and native to JavaScript, while XML still offers schemas, attributes and namespaces. Nearly every modern web API sends and receives JSON.",
        "example": "A weather API returns a JSON object with a temperature field. One parse call turns it into something a script can read.",
        "quiz": [
            {
                "q": "Which method turns a JSON string into an object?",
                "options": ["JSON.stringify", "JSON.parse", "JSON.toString", "JSON.encode"],
                "answer": 1,
                "why": "parse reads the text and builds the matching JavaScript value.",
            },
            {
                "q": "Which of these is NOT valid in JSON?",
                "options": ["A quoted key", "An array", "A function value", "null"],
                "answer": 2,
                "why": "JSON carries data only, so functions and comments cannot appear in it.",
            },
            {
                "q": "Which statement about JSON is NOT correct?",
                "options": ["Keys must use double quotes", "It supports true, false and null", "It is native to JavaScript", "It supports comments for documentation"],
                "answer": 3,
                "why": "Comments were removed from the format deliberately, to keep it simple.",
            },
            {
                "q": "Compared with XML, JSON is:",
                "options": ["Heavier and harder to parse", "Lighter and easier to parse in JavaScript", "Able to use attributes and namespaces", "Required for SOAP services"],
                "answer": 1,
                "why": "Its size and direct mapping to JavaScript objects are why APIs prefer it.",
            },
            {
                "q": "What does JSON.stringify produce?",
                "options": ["A JavaScript object", "A JSON text string", "An array", "A schema"],
                "answer": 1,
                "why": "It serialises a value into the text form that can be sent over the network.",
            },
        ],
        "examTip": "State the JSON syntax rules, give both conversion methods, and compare JSON with XML.",
    },

    "CSCA512-MIV-T04": {
        "explanation": "jQuery is a small library that simplifies DOM traversal, events, animation and AJAX. Its central idea is the jQuery function, usually written with a dollar sign, which selects elements with CSS style selectors. Methods can then be chained, so several operations read as one line. Manipulation covers text, html, attr, addClass, append and remove, and effects include show, hide, fadeIn and slideToggle. Events are handled with on, click, hover and ready, the last of which waits for the document. AJAX helpers wrap XMLHttpRequest in short calls: get, post and ajax. The trade off is an extra download, and much of what it offered is now built into the browser.",
        "example": "Hiding all error messages takes one line in jQuery. The same work in plain DOM code needs a loop.",
        "quiz": [
            {
                "q": "What does the dollar sign function do in jQuery?",
                "options": ["Creates a variable", "Selects elements with CSS style selectors", "Starts an AJAX call", "Loads a plugin"],
                "answer": 1,
                "why": "Selection is the entry point to everything else, and the result can be chained.",
            },
            {
                "q": "Which jQuery method waits until the document is ready?",
                "options": ["on", "click", "ready", "hover"],
                "answer": 2,
                "why": "Running code only after the document is parsed avoids null element errors.",
            },
            {
                "q": "Which statement about jQuery is NOT correct?",
                "options": ["Methods can be chained", "It simplifies AJAX calls", "It adds an extra file to download", "It is required for modern JavaScript to run"],
                "answer": 3,
                "why": "Browsers now provide querySelector, fetch and classList, so the library is often unnecessary.",
            },
            {
                "q": "Which is a jQuery effect method?",
                "options": ["append", "attr", "fadeIn", "addClass"],
                "answer": 2,
                "why": "fadeIn animates visibility, while the others change content or attributes.",
            },
            {
                "q": "What does the jQuery ajax method wrap?",
                "options": ["The fetch API", "XMLHttpRequest", "The DOM", "Web storage"],
                "answer": 1,
                "why": "It hides the details of creating a request object and reading its state.",
            },
        ],
        "examTip": "Describe selection and chaining, name four effect methods, and give one advantage and one drawback.",
    },

    "CSCA512-MIV-T05": {
        "explanation": "AJAX updates part of a page by exchanging data with the server in the background, without reloading the page. The sequence is always the same. Script sends an asynchronous request, the server replies with data, and the page updates from it. With XMLHttpRequest the steps are to create the object, open the request and set a callback. The handler then checks readyState and status before reading the response. The fetch API is the modern alternative: it returns a promise and is usually written with async and await. One rule governs cross site requests: the same origin policy blocks them unless the server allows them with CORS headers.",
        "example": "Typing in a search box and seeing suggestions appear, with the page never reloading, is AJAX at work.",
        "quiz": [
            {
                "q": "What does AJAX allow a page to do?",
                "options": ["Reload faster", "Update part of the page using server data without a reload", "Run without a server", "Store data locally"],
                "answer": 1,
                "why": "The request happens in the background and only the changed part is redrawn.",
            },
            {
                "q": "What does the fetch API return?",
                "options": ["A string", "A promise", "An event", "A callback"],
                "answer": 1,
                "why": "The promise resolves to a response, whose json method gives the parsed data.",
            },
            {
                "q": "Which statement about AJAX is NOT correct?",
                "options": ["The request is asynchronous", "readyState and status are checked in the handler", "CORS headers let a server permit cross origin requests", "AJAX requires the page to reload to show new data"],
                "answer": 3,
                "why": "Avoiding that reload is the entire purpose of the technique.",
            },
            {
                "q": "What does the same origin policy restrict?",
                "options": ["The size of a request", "Requests to a different origin unless CORS allows them", "The number of requests", "The use of JSON"],
                "answer": 1,
                "why": "It is a browser security rule, and the server relaxes it by sending CORS headers.",
            },
            {
                "q": "Which method actually sends an XMLHttpRequest?",
                "options": ["open", "send", "readyState", "onreadystatechange"],
                "answer": 1,
                "why": "open configures the request and send transmits it.",
            },
        ],
        "examTip": "Describe the AJAX cycle, the XMLHttpRequest steps, fetch with promises, and same origin with CORS.",
    },

    "CSCA512-MV-T01": {
        "explanation": "PHP is a server side scripting language that runs on the web server and outputs HTML. The browser requests a page ending in php. The server executes the script and sends back only the generated HTML. The classic stack for this is LAMP: Linux, Apache, MySQL and PHP. XAMPP or WAMP gives the same combination on a local machine. The key contrast is with client side script. PHP runs on the server and the user never sees it, while JavaScript runs in the browser and is visible. PHP code sits inside its own opening and closing tags and can be mixed freely with markup.",
        "example": "Viewing the source of a PHP page in a browser shows HTML, never the PHP. That is the clearest proof of where it runs.",
        "quiz": [
            {
                "q": "What does LAMP stand for?",
                "options": ["Linux, Apache, MySQL, PHP", "Local Apache, Main PHP", "Linux Application Management Platform", "Link, Apache, Module, PHP"],
                "answer": 0,
                "why": "The four components are the operating system, the server, the database and the language.",
            },
            {
                "q": "Where does PHP code run?",
                "options": ["In the browser", "On the web server", "In the database", "On the network"],
                "answer": 1,
                "why": "The server executes the script and sends only the result to the browser.",
            },
            {
                "q": "Which statement about PHP is NOT correct?",
                "options": ["It outputs HTML", "It can be mixed with markup", "The user can read the PHP source in the browser", "XAMPP provides a local development stack"],
                "answer": 2,
                "why": "Only the generated HTML is sent, so the source stays on the server.",
            },
            {
                "q": "Which tags surround PHP code?",
                "options": ["Angle brackets with a question mark and php", "Curly braces", "Square brackets", "Double quotes"],
                "answer": 0,
                "why": "The opening tag is the php marker and the closing tag ends the block.",
            },
            {
                "q": "Why can PHP keep a database password secret?",
                "options": ["Because it encrypts files", "Because the code runs on the server and is never sent", "Because browsers cannot read text", "Because PHP is compiled"],
                "answer": 1,
                "why": "Anything in the browser is visible, but server side code never reaches the client.",
            },
        ],
        "examTip": "Describe the request cycle with PHP, expand LAMP, and contrast PHP with client side JavaScript.",
    },

    "CSCA512-MV-T02": {
        "explanation": "PHP scripts use loosely typed variables, each written with a dollar sign in front of the name. Statements end with a semicolon, and comments use double slashes, a hash or block syntax. Variable names are case sensitive, which catches beginners out. Scope has three levels: local inside a function, global outside it, and static, which keeps a value between calls. Constants are created with define or const and cannot change. PHP supplies predefined constants such as the version and the current file. Values have types such as string, integer, float, boolean, array, object, null and resource, and PHP converts between them automatically in expressions.",
        "example": "A variable named count and one named Count are different things in PHP, which is not true of keywords.",
        "quiz": [
            {
                "q": "How is a PHP variable written?",
                "options": ["With a name only", "With a dollar sign before the name", "With a hash before the name", "With an at sign"],
                "answer": 1,
                "why": "The dollar sign is required on every variable, including when it is declared.",
            },
            {
                "q": "Which keyword keeps a local variable's value between function calls?",
                "options": ["global", "static", "const", "define"],
                "answer": 1,
                "why": "A static variable is initialised once and then remembers its value.",
            },
            {
                "q": "Which statement about PHP is NOT correct?",
                "options": ["Statements end with a semicolon", "Variable names are case sensitive", "Constants can be redefined at any time", "PHP converts types automatically in expressions"],
                "answer": 2,
                "why": "A constant is fixed once it is defined, which is the point of using one.",
            },
            {
                "q": "Which function creates a constant?",
                "options": ["const", "define", "echo", "isset"],
                "answer": 1,
                "why": "define creates a constant at run time, while const is used at compile time.",
            },
            {
                "q": "Which of these is a PHP data type?",
                "options": ["resource", "tuple", "pointer", "struct"],
                "answer": 0,
                "why": "A resource holds a handle to something external, such as an open database connection.",
            },
        ],
        "examTip": "Show a variable declaration, list the variable scopes, and explain constants and type conversion.",
    },

    "CSCA512-MV-T03": {
        "explanation": "PHP sends content to the browser with several statements. echo can take several arguments and is marginally faster. print takes one argument and returns a value, so it can appear in an expression. For debugging, print_r shows an array or object in readable form, and var_dump goes further by adding types and lengths. Formatted output uses printf with placeholders for strings, integers and floating point numbers. Output is usually mixed into the page. Short echo tags and heredoc syntax let dynamic values sit inside markup without constant opening and closing of tags.",
        "example": "Printing a price to two decimal places is one printf call with a float placeholder, rather than manual rounding.",
        "quiz": [
            {
                "q": "What is the difference between echo and print?",
                "options": ["They are identical", "echo takes several arguments and returns nothing, print returns a value", "print is faster", "echo cannot output strings"],
                "answer": 1,
                "why": "Because print returns a value it can be used in an expression, while echo cannot.",
            },
            {
                "q": "Which function is best for debugging an array?",
                "options": ["echo", "print", "print_r", "printf"],
                "answer": 2,
                "why": "print_r shows the structure, while var_dump adds the type and length of each value.",
            },
            {
                "q": "Which statement about output is NOT correct?",
                "options": ["var_dump shows types and lengths", "printf formats values with placeholders", "Heredoc helps mix values into markup", "echo can print only one value at a time"],
                "answer": 3,
                "why": "echo accepts several comma separated arguments, which is one of its small advantages.",
            },
            {
                "q": "Which placeholder would printf use for a whole number?",
                "options": ["A string placeholder", "An integer placeholder", "A float placeholder", "A boolean placeholder"],
                "answer": 1,
                "why": "The integer placeholder prints a rounded whole number from the value given.",
            },
            {
                "q": "What does var_dump add beyond print_r?",
                "options": ["Colours", "The type and length of each value", "A timestamp", "The file name"],
                "answer": 1,
                "why": "Seeing the type is often what reveals why a comparison did not behave as expected.",
            },
        ],
        "examTip": "Compare echo, print, print_r and var_dump, and give one use of printf and heredoc.",
    },

    "CSCA512-MV-T04": {
        "explanation": "PHP gives a large set of string functions: strlen, strpos, substr, str_replace, strtoupper, trim, explode, implode and nl2br. Interpolation is a useful detail. Double quoted strings expand variables in place, while single quoted strings do not. Arrays come in three kinds. An indexed array uses numeric keys. An associative array uses named keys, like a record. A multidimensional array holds arrays inside arrays, for tables of data. Traversal is usually done with foreach, and the common functions are count, sort, ksort, array_push, array_pop, array_merge, array_keys and array_values.",
        "example": "A row from a database arrives as an associative array, so a value is read by column name rather than position.",
        "quiz": [
            {
                "q": "Which function splits a string into an array?",
                "options": ["implode", "explode", "substr", "trim"],
                "answer": 1,
                "why": "explode breaks a string at a separator, and implode joins the pieces back together.",
            },
            {
                "q": "Which array uses named keys?",
                "options": ["An indexed array", "An associative array", "A numeric array", "A stacked array"],
                "answer": 1,
                "why": "Named keys let a value be read by field name, which suits a database row.",
            },
            {
                "q": "Which statement about PHP strings is NOT correct?",
                "options": ["Double quoted strings expand variables", "Single quoted strings do not expand variables", "str_replace substitutes text", "strlen changes the case of a string"],
                "answer": 3,
                "why": "strlen returns the length, while strtoupper is the function that changes case.",
            },
            {
                "q": "Which function counts the elements of an array?",
                "options": ["count", "sort", "ksort", "array_merge"],
                "answer": 0,
                "why": "count returns the number of elements and is the usual guard before a loop.",
            },
            {
                "q": "How does ksort differ from sort?",
                "options": ["sort orders by key, ksort by value", "ksort orders by key and keeps it, sort reindexes by value", "They are identical", "ksort sorts strings only"],
                "answer": 1,
                "why": "ksort is what you want for an associative array, because sort would discard the keys.",
            },
        ],
        "examTip": "Name five string functions, explain single and double quotes, and describe the three array kinds.",
    },

    "CSCA512-MV-T05": {
        "explanation": "PHP supports the usual operators, with two worth remembering. The dot joins strings, and the null coalescing operator gives a default when a value is missing. Comparison has loose and strict forms: double equals converts types, triple equals does not. Branching uses if, else, elseif and switch, and modern PHP also has the match expression. Loops include for, while, do while and foreach, with break and continue. Functions are declared with the function keyword. They may take defaults, variadic arguments, type hints and a declared return type. Other files are pulled in with include or require. require stops the script when the file is missing, while include only warns.",
        "example": "Requiring a database configuration file at the top of every page is standard, because a missing config should stop everything.",
        "quiz": [
            {
                "q": "Which operator joins two strings in PHP?",
                "options": ["The plus sign", "The dot", "The comma", "The ampersand"],
                "answer": 1,
                "why": "The dot is concatenation, since plus is reserved for arithmetic.",
            },
            {
                "q": "What does the null coalescing operator do?",
                "options": ["Compares two nulls", "Provides a default when a value is missing or null", "Removes null values", "Joins strings with null"],
                "answer": 1,
                "why": "It shortens the common pattern of testing whether a key exists before using it.",
            },
            {
                "q": "Which statement about PHP is NOT correct?",
                "options": ["Triple equals compares without converting types", "foreach suits arrays", "include and require both insert another file", "switch and match behave identically in every way"],
                "answer": 3,
                "why": "match returns a value and uses strict comparison, while switch uses loose comparison.",
            },
            {
                "q": "What is the difference between include and require?",
                "options": ["They are identical", "include warns and continues, require stops the script on failure", "require runs faster", "include cannot be used twice"],
                "answer": 1,
                "why": "A missing required file is a fatal error, which is what you want for configuration.",
            },
            {
                "q": "Which loop is used to walk through an array?",
                "options": ["for", "while", "foreach", "do while"],
                "answer": 2,
                "why": "foreach gives each key and value without the bookkeeping of an index counter.",
            },
        ],
        "examTip": "Name the string and null coalescing operators, compare == and ===, and explain include versus require.",
    },

    "CSCA512-MV-T06": {
        "explanation": "PHP reads user input from forms, URLs and cookies to build its response. The two methods differ sharply. GET places data in the URL, where it is visible and limited in size. POST sends it in the request body and suits sensitive or large data. A script reads each field through the POST or GET superglobal, using the control's name. Every value must then be validated and sanitised. trim, htmlspecialchars and filter_var defend against bad input, cross site scripting and SQL injection. Uploads arrive in the FILES superglobal and are stored with move_uploaded_file after checking type and size. State across requests is kept with cookies or sessions.",
        "example": "A contact form that posts to itself shows errors above the fields on the first attempt, then thanks the user.",
        "quiz": [
            {
                "q": "When should GET be used?",
                "options": ["For passwords", "For harmless data that can live in the URL, such as a search term", "For file uploads", "For large forms"],
                "answer": 1,
                "why": "GET data is visible and has a length limit, so it suits searches and links.",
            },
            {
                "q": "Which function helps prevent cross site scripting when printing user input?",
                "options": ["trim", "htmlspecialchars", "strlen", "explode"],
                "answer": 1,
                "why": "It escapes the characters that would otherwise become markup in the page.",
            },
            {
                "q": "Which statement about reading input is NOT correct?",
                "options": ["POST data travels in the request body", "Files arrive in the FILES superglobal", "Sessions keep state on the server", "GET is the safe way to send a password"],
                "answer": 3,
                "why": "A password in the URL is visible in the address bar, in logs and in browser history.",
            },
            {
                "q": "Which function stores an uploaded file?",
                "options": ["move_uploaded_file", "file_get_contents", "fopen", "copy"],
                "answer": 0,
                "why": "It checks that the file really came from an upload before moving it into place.",
            },
            {
                "q": "What starts a session in PHP?",
                "options": ["session_start", "setcookie", "session_open", "start_session"],
                "answer": 0,
                "why": "session_start must run before any output, because it sends a session cookie header.",
            },
        ],
        "examTip": "Compare GET and POST, name three superglobals, and list three sanitising functions.",
    },

    "CSCA512-MV-T07": {
        "explanation": "PHP connects to MySQL to store and retrieve data with SQL statements. A connection is made with mysqli_connect or by creating a PDO object. Both take the host, user, password and database name, and both can fail. Queries then run through mysqli_query or a prepared statement, whether they are SELECT, INSERT, UPDATE or DELETE. Results come back as rows fetched with mysqli_fetch_assoc or fetch_all. They are usually printed into a table inside a loop. Prepared statements matter most. Binding parameters keeps user input out of the SQL and prevents injection. After a change, affected rows and the insert id confirm what happened. The connection is then closed.",
        "example": "A student form inserts a record, reads back the new id and then lists every student in a table.",
        "quiz": [
            {
                "q": "Which practice prevents SQL injection?",
                "options": ["Escaping the output with trim", "Prepared statements with bound parameters", "Using SELECT instead of INSERT", "Closing the connection quickly"],
                "answer": 1,
                "why": "The statement is sent first and the values separately, so input cannot change the SQL.",
            },
            {
                "q": "Which function fetches a result row as an associative array?",
                "options": ["mysqli_query", "mysqli_fetch_assoc", "mysqli_connect", "mysqli_close"],
                "answer": 1,
                "why": "It returns one row at a time with column names as keys, which suits a loop.",
            },
            {
                "q": "Which statement about PHP and MySQL is NOT correct?",
                "options": ["PDO supports several database systems", "The insert id reports the key of a new row", "Affected rows counts the rows a change touched", "A connection never needs to be checked for failure"],
                "answer": 3,
                "why": "Connection failures are common, and an unchecked one produces confusing errors later.",
            },
            {
                "q": "Which value tells you how many rows an UPDATE changed?",
                "options": ["The insert id", "Affected rows", "The row count of the table", "The query string"],
                "answer": 1,
                "why": "It is the standard way to report success back to the user after an edit.",
            },
            {
                "q": "What is the advantage of PDO over mysqli?",
                "options": ["It is always faster", "It works with several database systems through one interface", "It needs no connection details", "It writes the SQL for you"],
                "answer": 1,
                "why": "Switching database becomes a change of connection string rather than a rewrite.",
            },
        ],
        "examTip": "Describe connecting, running a query, fetching rows, prepared statements and closing the connection.",
    },
}
