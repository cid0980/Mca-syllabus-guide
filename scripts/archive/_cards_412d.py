# Cards for CSCA 412 - Module V: Java Swing, Java Beans and Servlets.
# Apply with
#   python3 scripts/archive/_apply_cards.py src/lib/data/tree/CSCA412.json scripts/archive/_cards_412d.py

CARDS = {
    "CSCA412-MV-T01": {
        "explanation": "Swing is a library of graphical components that builds on AWT, the Abstract Window Toolkit that Java started with, but is lightweight, meaning the components are drawn by Java itself instead of each one asking the operating system for its own window, so they look the same everywhere and allow a pluggable look and feel. Its classes carry the J prefix, JFrame, JPanel, JButton, JTextField, JLabel, JTable and JList among them, and they follow a container hierarchy in which a top level container such as JFrame holds a content pane and that pane holds the components. Compared with the AWT Frame, a JFrame offers getContentPane(), a default BorderLayout and buttons that can show an icon as well as text. Ready made dialogs come from JOptionPane, and menus use JMenuBar, JMenu and JMenuItem, with the menu bar set on the frame.",
        "example": "A marks entry screen in Swing: a JFrame holding a JPanel, JLabels and JTextFields arranged in a GridLayout, a JButton to save, and JOptionPane.showMessageDialog to confirm that the marks were saved.",
        "quiz": [
            {
                "q": "Which of these is a Swing top level container?",
                "options": ["Frame", "JFrame", "Container", "Graphics"],
                "answer": 1,
                "why": "Swing containers begin with J; Frame and Container come from AWT.",
            },
            {
                "q": "Swing components are called lightweight because:",
                "options": [
                    "they use less memory than any other library",
                    "they are drawn by Java instead of by the operating system",
                    "they cannot display text",
                    "they need no layout manager",
                ],
                "answer": 1,
                "why": "Light and heavy refer to who draws the component, not to how much memory it uses.",
            },
            {
                "q": "Which statement about Swing and AWT is NOT correct?",
                "options": [
                    "Swing component names start with J",
                    "Swing supports a pluggable look and feel",
                    "Swing is built on top of AWT",
                    "Swing components are heavyweight native windows",
                ],
                "answer": 3,
                "why": "Being lightweight is the whole difference from AWT, which uses native windows.",
            },
            {
                "q": "A short confirmation message with an OK button is shown with:",
                "options": ["JOptionPane.showMessageDialog", "paint()", "System.out.println", "setVisible(true)"],
                "answer": 0,
                "why": "JOptionPane supplies the standard dialogs, including message, input and confirm.",
            },
        ],
        "examTip": "Learn five J classes by name with a one line role for each, and be ready for the standard AWT against Swing short question.",
    },
    "CSCA412-MV-T02": {
        "explanation": "A Java Bean is a reusable software component built to a fixed shape, so that tools can inspect it and use it without knowing your program: it has a public constructor with no arguments so it can be created automatically, private fields reached through public accessor methods that follow the get and set naming pattern, and it implements the Serializable interface so its state can be saved and restored. A builder tool examines the methods and works out the bean's properties, and this discovery is called introspection. Beans also communicate through events, and a bound property fires a property change event whenever its value changes so that other objects can react. The Bean Development Kit was the tool supplied to test and inspect beans, and the point of all the conventions is that a designed bean can be dropped into a visual editor and wired together without writing code.",
        "example": "A numeric keypad bean built once for a college project is dropped into the fee counter screen, the library issue screen and the attendance screen, each time with a different label and a different action to perform.",
        "quiz": [
            {
                "q": "Which pair of names marks the bean property called marks?",
                "options": [
                    "getMarks and setMarks",
                    "marksGet and marksSet",
                    "readMarks on its own",
                    "Marks() and Marks(int)",
                ],
                "answer": 0,
                "why": "The get and set convention is what allows a tool to discover the property by name.",
            },
            {
                "q": "A Java Bean must normally have:",
                "options": [
                    "a public constructor with no arguments",
                    "a main method",
                    "a paint method",
                    "at least one static data member",
                ],
                "answer": 0,
                "why": "The tool creates the bean itself before setting properties, so it needs an argument free constructor.",
            },
            {
                "q": "Introspection means:",
                "options": [
                    "a tool discovering the properties, methods and events of a bean",
                    "the bean reading its own configuration file",
                    "converting a bean into a servlet",
                    "hiding the fields of a bean from the program",
                ],
                "answer": 0,
                "why": "The class is examined at work time rather than known in advance, which is what makes visual assembly possible.",
            },
            {
                "q": "Which statement about beans is NOT correct?",
                "options": [
                    "Beans are reusable components",
                    "A bound property notifies listeners when its value changes",
                    "The Bean Development Kit was used to test beans",
                    "A bean must contain a graphical window",
                ],
                "answer": 3,
                "why": "A bean may have no user interface at all; reuse and conventions are what make it a bean.",
            },
        ],
        "examTip": "Answer bean questions with the four conventions: an argument free public constructor, get and set accessors, Serializable and event support.",
    },
    "CSCA412-MV-T03": {
        "explanation": "A servlet is a Java class that runs inside a web server, strictly inside a servlet container such as Apache Tomcat, and answers HTTP, the HyperText Transfer Protocol that web browsers speak, so the page is built on the server instead of inside the browser as it was with an applet. Its life cycle has three stages: the container calls init() once when the servlet is loaded, then service() for every request, which passes the work to doGet() or doPost() depending on the request method, and finally destroy() once before the servlet is removed. The request and response arrive as HttpServletRequest and HttpServletResponse, and because HTTP itself remembers nothing between requests, state is carried by session tracking, using cookies, URL, the Uniform Resource Locator that names a page, rewriting, hidden form fields or the HttpSession API, the application programming interface the container keeps for the session. Compared with CGI, the Common Gateway Interface that runs a separate program for each request, where every single request starts a whole new process, a servlet stays loaded and serves requests on threads, which is faster and easier to scale, and it is deployed through a web.xml descriptor or an annotation.",
        "example": "A college results page: the student submits a roll number in a GET request, which asks the server for a page and carries the data in the address line, doGet() reads the parameter, fetches the marks and writes back HTML (HyperText Markup Language, what browsers render), all inside one servlet that keeps running for every student who asks.",
        "quiz": [
            {
                "q": "Which servlet method runs exactly once when the servlet is first loaded?",
                "options": ["init()", "service()", "doGet()", "destroy()"],
                "answer": 0,
                "why": "init() does one time setup; service() and doGet() run again for every request.",
            },
            {
                "q": "A form submitted with method = \"post\" is handled by:",
                "options": ["doGet()", "doPost()", "init()", "destroy()"],
                "answer": 1,
                "why": "service() checks the HTTP method and forwards a POST to doPost().",
            },
            {
                "q": "Which statement about session tracking is NOT correct?",
                "options": [
                    "A cookie can carry a session identifier",
                    "URL rewriting can carry a session identifier",
                    "A hidden form field can carry a session identifier",
                    "HTTP remembers each client's earlier requests by itself",
                ],
                "answer": 3,
                "why": "HTTP is stateless, which is exactly why one of the tracking techniques is needed.",
            },
            {
                "q": "A servlet is faster than CGI mainly because:",
                "options": [
                    "it uses no memory at all",
                    "it stays loaded and serves requests with threads instead of starting a process each time",
                    "it compiles faster",
                    "it runs inside the browser",
                ],
                "answer": 1,
                "why": "One process with many threads beats one process per request, which is what CGI does.",
            },
        ],
        "examTip": "Three lists to memorise: the life cycle init, service, destroy, the four ways of session tracking, and the servlet against CGI comparison of thread against process.",
    },
}
