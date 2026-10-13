# Cards for CSCA 412 - Module III: Java Applets, Graphics, Files and Collections,
# and Module IV: Event Handling, Applets and AWT.
# Apply with
#   python3 scripts/archive/_apply_cards.py src/lib/data/tree/CSCA412.json scripts/archive/_cards_412c.py

CARDS = {
    "CSCA412-MIII-T01": {
        "explanation": "An applet was a small Java program that was embedded in a web page and run inside the browser, with no main method of its own, because the browser called its life cycle methods instead. That cycle runs init() once when the applet is loaded, start() every time it becomes visible, paint() whenever it must be drawn, stop() when it is hidden and destroy() when it is removed for good. The browser supplied the Java plugin, so the same bytecode ran on any operating system. Browsers have removed that plugin and the applet tag has gone from HTML, the HyperText Markup Language that web pages are written in, which is why applets are obsolete and the same work is now done by servlets on the server and JavaScript in the page, but the life cycle and the paint model are still standard exam material.",
        "example": "An old college website showed a scrolling banner as an applet. Opening the page called start() and switching to another tab called stop(), so the animation paused instead of wasting the processor.",
        "quiz": [
            {
                "q": "Which method of an applet runs exactly once when it is loaded?",
                "options": ["start()", "init()", "paint()", "stop()"],
                "answer": 1,
                "why": "init() does one time setup; start() may run many times as the applet is shown and hidden.",
            },
            {
                "q": "paint() in an applet is called:",
                "options": [
                    "by the programmer whenever drawing is needed",
                    "by the system when the applet has to be drawn or redrawn",
                    "once at compilation time",
                    "only when the applet is destroyed",
                ],
                "answer": 1,
                "why": "Your code calls repaint(), which asks the system to call paint() when it is ready.",
            },
            {
                "q": "Which statement about applets is NOT correct?",
                "options": [
                    "An applet runs inside a browser",
                    "An applet needs a main method to start",
                    "An applet's life cycle begins with init()",
                    "Applets are obsolete because browsers removed the Java plugin",
                ],
                "answer": 1,
                "why": "There is no main in an applet; the browser drives it through the life cycle methods.",
            },
            {
                "q": "Which applet method is called when the applet is about to be removed permanently?",
                "options": ["destroy()", "stop()", "init()", "repaint()"],
                "answer": 0,
                "why": "stop() only pauses a hidden applet; destroy() releases whatever it was using.",
            },
        ],
        "examTip": "Memorise the life cycle order init, start, paint, stop, destroy. That one line answers most applet questions.",
    },
    "CSCA412-MIII-T02": {
        "explanation": "Java draws on a component through a Graphics object, which the system passes to paint(Graphics g) whenever the component needs to be drawn. The coordinate system begins at the top left of the component: x grows to the right and y grows downwards, so (0,0) is the top left corner and not the bottom left. The class offers primitives for outlines such as drawLine, drawRect, drawOval, drawPolygon and drawString, and the matching fillRect, fillOval and fillPolygon for filled shapes, together with setColor and setFont to control appearance. Animation is produced by changing the values you draw with and then calling repaint(), which asks the system to call paint() again as soon as it can, because the program must never call paint() directly.",
        "example": "A ball animation moves the ball five pixels to the right on each pass: the program changes the x coordinate, calls repaint(), and the next paint() draws the oval at its new place.",
        "quiz": [
            {
                "q": "In Java graphics, the point (0,0) is at the:",
                "options": ["centre of the component", "bottom left corner", "top left corner", "bottom right corner"],
                "answer": 2,
                "why": "x increases to the right and y increases downwards, so the origin is the top left.",
            },
            {
                "q": "Which method draws a filled circle (oval)?",
                "options": ["drawOval", "fillOval", "drawRect", "drawString"],
                "answer": 1,
                "why": "The draw methods give outlines and the fill methods give solid shapes.",
            },
            {
                "q": "Which statement about repaint() is NOT correct?",
                "options": [
                    "It asks the system to call paint()",
                    "It can be called from your own code",
                    "It draws the shape immediately, all by itself",
                    "It is the usual way to produce animation",
                ],
                "answer": 2,
                "why": "repaint() only requests a redraw; the drawing is done later by paint().",
            },
            {
                "q": "The call g.drawString(\"MCA\", 20, 50) places the text with its baseline at:",
                "options": ["x = 20 and y = 50", "x = 50 and y = 20", "the centre of the component", "always the top left corner"],
                "answer": 0,
                "why": "drawString takes x first and then y, and y marks the baseline of the text.",
            },
        ],
        "examTip": "Write down the origin convention and the draw and fill pair for each shape. The direction of the y axis is a favourite trick question.",
    },
    "CSCA412-MIII-T03": {
        "explanation": "Java treats every file as a stream of data and splits the classes into byte streams for raw binary data and character streams for text. FileInputStream and FileOutputStream move bytes, while FileReader and FileWriter move characters, and BufferedReader and BufferedWriter wrap those so that you can read or write a whole line at a time and with fewer calls to the disk. You name the file with a File object, wrap it in the stream you need and close it when the work is done, usually in a finally block or with try with resources, so it is closed even when something fails in between. Almost every file operation can throw IOException, which is a checked exception and so must be handled or declared by the compiler.",
        "example": "A marks file is read line by line with BufferedReader in = new BufferedReader(new FileReader(\"marks.txt\")); each readLine() returns one line and returns null when the file has no more lines.",
        "quiz": [
            {
                "q": "Which class is a character stream for reading a text file?",
                "options": ["FileInputStream", "FileReader", "FileOutputStream", "DataOutputStream"],
                "answer": 1,
                "why": "Reader and Writer classes work in characters, which is what text files hold.",
            },
            {
                "q": "What does BufferedReader.readLine() return when the end of the file is reached?",
                "options": ["an empty string", "null", "-1", "it always throws IOException"],
                "answer": 1,
                "why": "A null return is the standard signal that there is nothing more to read.",
            },
            {
                "q": "Which statement about Java file handling is NOT correct?",
                "options": [
                    "IOException is a checked exception",
                    "FileWriter writes characters",
                    "FileInputStream reads bytes",
                    "The file closes automatically as soon as a read statement finishes",
                ],
                "answer": 3,
                "why": "You must close the stream yourself, or use try with resources so Java closes it for you.",
            },
            {
                "q": "Wrapping a FileReader inside a BufferedReader is done mainly to:",
                "options": [
                    "read a line at a time and cut down the number of reads",
                    "convert bytes into characters",
                    "compress the file",
                    "lock the file from other programs",
                ],
                "answer": 0,
                "why": "Buffering collects the data in one place, and with a reader you gain the handy readLine().",
            },
        ],
        "examTip": "Practise the exact two line idiom, a FileReader wrapped in a BufferedReader, and mention try or try with resources so the file is certainly closed.",
    },
    "CSCA412-MIII-T04": {
        "explanation": "The Java collections framework is a set of ready made containers that share common interfaces, so you can pick the right structure instead of writing one yourself. A List keeps an ordered sequence and allows duplicates, a Set keeps elements unique, a Map stores each key with one value and a Queue arranges elements for processing in order. Each interface has several implementations with different costs: ArrayList gives fast access by index, LinkedList is quicker when you insert or remove in the middle, HashSet is unordered and fast for lookup, and TreeSet keeps its elements sorted. Any collection can be walked with an Iterator or the for each loop, which makes the same loop work for every container, while an array has a fixed length and needs an index, which is why these classes are the normal choice.",
        "example": "A student list held in an ArrayList grows as new admissions arrive, and a HashMap from roll number to marks answers the question \"what did roll 21 score?\" without searching through the whole list.",
        "quiz": [
            {
                "q": "Which collection type stores key and value pairs?",
                "options": ["List", "Set", "Map", "Queue"],
                "answer": 2,
                "why": "A Map looks up a value by its key, which is what a roll number to marks lookup needs.",
            },
            {
                "q": "Which implementation keeps its elements in sorted order?",
                "options": ["ArrayList", "HashSet", "TreeSet", "LinkedList"],
                "answer": 2,
                "why": "Tree based collections keep things ordered; HashSet gives speed instead of order.",
            },
            {
                "q": "Which statement about the collections framework is NOT correct?",
                "options": [
                    "A List may contain duplicates",
                    "A Set cannot contain duplicates",
                    "A Map can hold two different values under the same key",
                    "An ArrayList grows as elements are added",
                ],
                "answer": 2,
                "why": "One key maps to one value, and putting a value again replaces the earlier one.",
            },
            {
                "q": "A program inserts and deletes at the front of a long list very often. The better choice is:",
                "options": ["ArrayList", "LinkedList", "TreeSet", "HashMap"],
                "answer": 1,
                "why": "An ArrayList has to shift every later element, while a linked list only changes a few links.",
            },
        ],
        "examTip": "Learn one line for each interface: List ordered with duplicates, Set unique, Map key to value, Queue in order of processing. Then name one implementation for each.",
    },
    "CSCA412-MIV-T01": {
        "explanation": "Java handles user actions with the delegation event model: the component where something happens is the source, it creates an event object, and every object registered with it as a listener for that event type is told about it. Registration is a call such as button.addActionListener(this), and the listener must implement the matching interface, ActionListener for a button, MouseListener for the mouse, WindowListener for window events, whose method is then called. Adapter classes such as MouseAdapter and WindowAdapter provide empty versions of every method in the interface, so you can extend the adapter and override only the one or two methods you care about. The handler receives the event object itself, for example ActionEvent, which carries the source and any command text, so a single handler can serve many buttons.",
        "example": "A calculator registers one actionPerformed method for all twenty buttons. The handler asks getActionCommand() and so knows which digit or operator was pressed, without twenty separate methods.",
        "quiz": [
            {
                "q": "Which model does Java use for handling events?",
                "options": ["delegation", "inheritance", "polling", "compilation"],
                "answer": 0,
                "why": "The source passes the event to whichever listeners registered for it, which is delegation.",
            },
            {
                "q": "Which method must a class implementing ActionListener write?",
                "options": [
                    "actionPerformed(ActionEvent e)",
                    "mouseClicked(MouseEvent e)",
                    "paint(Graphics g)",
                    "windowClosing(WindowEvent e)",
                ],
                "answer": 0,
                "why": "Each listener interface declares its own method, and ActionListener declares actionPerformed.",
            },
            {
                "q": "Which statement about adapter classes is NOT correct?",
                "options": [
                    "MouseAdapter supplies empty versions of all mouse methods",
                    "You extend an adapter so you override only what you need",
                    "Using an adapter removes the need to register a listener",
                    "MouseListener on its own lists every mouse method, not just the one you want",
                ],
                "answer": 2,
                "why": "An adapter only saves you from writing empty methods; registration is still done with addMouseListener.",
            },
            {
                "q": "A class that wants to act when the user closes the window must register a:",
                "options": ["WindowListener", "ActionListener", "ItemListener", "TextListener"],
                "answer": 0,
                "why": "Closing the window is a window event, so a WindowListener or WindowAdapter is needed.",
            },
        ],
        "examTip": "Write the three steps in order: implement the listener interface, register with addXListener(), do the work in the handler method. Name one adapter as the example.",
    },
    "CSCA412-MIV-T02": {
        "explanation": "The Abstract Window Toolkit, or AWT, is Java's original window toolkit, built from heavyweight components, each of which uses a real window provided by the operating system. A Frame is a top level window with a title bar: you create it, set its size and layout, add components to it and make it visible, and it stays until the program ends or you dispose of it. A component draws itself by overriding paint(Graphics g) and using the drawing methods of the Graphics object, and text is drawn with drawString together with a Font object that carries a name, a style and a size. Since the operating system also decides when repainting is needed, drawing belongs in paint() and not in the constructor, and actions such as closing the frame are handled by registering a listener.",
        "example": "A marks entry window is a Frame with setSize(400, 300), a Label, two TextFields and a Button added before setVisible(true). Change that last call to false and the window never appears at all.",
        "quiz": [
            {
                "q": "Which AWT class creates a top level window with a title bar?",
                "options": ["Panel", "Frame", "Label", "Canvas"],
                "answer": 1,
                "why": "Frame, Window and Dialog are the top level containers; Panel must sit inside one of them.",
            },
            {
                "q": "Where should drawing code be written so that it survives a resize or another window covering your window?",
                "options": ["in main()", "in paint(Graphics g)", "in the constructor", "in actionPerformed()"],
                "answer": 1,
                "why": "The system calls paint() again whenever the window must be drawn afresh.",
            },
            {
                "q": "Which statement about a Frame program is NOT correct?",
                "options": [
                    "setSize() sets the size of the window",
                    "setVisible(true) makes the window appear",
                    "paint() is called by the system when the window needs drawing",
                    "A Frame is a lightweight component drawn by Java itself",
                ],
                "answer": 3,
                "why": "AWT components are heavyweights because each one uses a native window; lightweight drawing is Swing's specialty.",
            },
            {
                "q": "A Font object is created with three pieces of information:",
                "options": [
                    "name, style and size",
                    "colour, width and height",
                    "x, y and z coordinates",
                    "name, colour and file format",
                ],
                "answer": 0,
                "why": "new Font(\"Serif\", Font.BOLD, 16) is the usual form, and colour is set separately with setColor.",
            },
        ],
        "examTip": "Remember the four lines in order: create the Frame, setSize, add the components, setVisible(true).",
    },
    "CSCA412-MIV-T03": {
        "explanation": "The Abstract Window Toolkit, or AWT, supplies standard controls for user input, and each is a class that you create, configure, add to a container and connect to a listener. A Label shows text the user cannot edit, a Button fires an ActionEvent, a TextField holds a single line and a TextArea holds several lines, a Checkbox gives a tick box while several Checkboxes placed in the same CheckboxGroup behave as radio buttons, a Choice is a drop down list and a List shows rows that scroll, while a Scrollbar reports its value through an AdjustmentListener. The important distinction is between Component, which is anything that can be displayed, and Container, which is itself a Component that can hold other components inside it, such as Frame, Window and Panel.",
        "example": "A login form is a Frame holding two Labels for the prompts, two TextFields for the entries, a Button to submit and a Checkbox for remember me, all added before the frame is made visible.",
        "quiz": [
            {
                "q": "Which control gives a drop down list of choices?",
                "options": ["List", "Choice", "Checkbox", "TextArea"],
                "answer": 1,
                "why": "Choice shows one selected item and drops down for the rest; List shows several rows at once.",
            },
            {
                "q": "Radio button behaviour is obtained by placing Checkboxes inside the same:",
                "options": ["Panel", "CheckboxGroup", "List", "Scrollbar"],
                "answer": 1,
                "why": "A CheckboxGroup allows only one of its members to stay selected.",
            },
            {
                "q": "Which statement about components and containers is NOT correct?",
                "options": [
                    "Every Container is also a Component",
                    "A Panel can hold other components",
                    "A Button can hold other components inside it",
                    "A Frame is a Container",
                ],
                "answer": 2,
                "why": "A Button is a leaf control; only containers such as Frame and Panel hold other components.",
            },
            {
                "q": "A multi line box for a student's address should be a:",
                "options": ["TextField", "TextArea", "Label", "Choice"],
                "answer": 1,
                "why": "TextField takes one line only, so more than one line needs a TextArea.",
            },
        ],
        "examTip": "Sketch one form and label every control with its class name; the Choice against List and the CheckboxGroup points are asked often.",
    },
    "CSCA412-MIV-T04": {
        "explanation": "A layout manager decides the position and size of every component inside a container, so the same program still looks sensible when the window is resized or run on another platform. FlowLayout places components left to right and wraps to the next row; BorderLayout divides the container into North, South, East, West and Center; GridLayout gives equal sized cells in a stated number of rows and columns; CardLayout shows one component at a time from a stack, which is how step by step forms are built; and GridBagLayout gives exact control through constraint objects. A Frame uses BorderLayout by default and a Panel uses FlowLayout, and calling setLayout replaces that default. Menus follow their own hierarchy: a MenuBar attached to the frame with setMenuBar contains Menus, and each Menu contains MenuItems, which fire an ActionEvent when chosen.",
        "example": "A four function calculator lays its buttons out with new GridLayout(4, 4), while a text editor puts the text area in the Center and a status label in the South of a BorderLayout.",
        "quiz": [
            {
                "q": "Which layout arranges components in five regions, North, South, East, West and Center?",
                "options": ["FlowLayout", "BorderLayout", "GridLayout", "CardLayout"],
                "answer": 1,
                "why": "BorderLayout names its five areas, and the Center takes whatever space is left.",
            },
            {
                "q": "Which layout shows only one component at a time?",
                "options": ["GridLayout", "CardLayout", "FlowLayout", "GridBagLayout"],
                "answer": 1,
                "why": "CardLayout keeps components in a stack and shows the top card, which suits multi step forms.",
            },
            {
                "q": "Which statement about layout defaults is NOT correct?",
                "options": [
                    "The default layout of a Frame is BorderLayout",
                    "The default layout of a Panel is FlowLayout",
                    "GridLayout gives every cell the same size",
                    "CardLayout places components one below the other",
                ],
                "answer": 3,
                "why": "CardLayout stacks components on top of each other and shows one, rather than placing them in a column.",
            },
            {
                "q": "Choosing File and then Open from a menu means Open is a:",
                "options": ["MenuItem", "MenuBar", "Frame", "Layout"],
                "answer": 0,
                "why": "The MenuBar holds Menus, and the clickable entries inside a Menu are MenuItems.",
            },
        ],
        "examTip": "Draw each layout as a small box with arrows, and learn the default layout of Frame and Panel plus the five BorderLayout regions.",
    },
    "CSCA412-MIV-T05": {
        "explanation": "Java loads an image as an Image object, most simply with getImage() in an applet or with ImageIcon in Swing, and the picture arrives asynchronously, so the program may have to wait before all of it is available. To show it you call drawImage(image, x, y, observer) inside paint, where the observer argument lets Java repaint the area as more of the image arrives. Because an image is only a grid of pixels, it can also be processed directly: PixelGrabber copies the pixel values into an array of integers, you change those values, for example swapping red and green, and MemoryImageSource turns the changed array back into an image that can be drawn. The MediaTracker class exists to check that an image has finished loading before the program uses it.",
        "example": "A photo viewer that turns a picture into greyscale reads the pixels with PixelGrabber, averages the colour of each pixel, builds a new image with MemoryImageSource and shows it with drawImage.",
        "quiz": [
            {
                "q": "Which Swing class is commonly used to load an image for display on a component?",
                "options": ["ImageIcon", "PixelGrabber", "MediaTracker", "Graphics"],
                "answer": 0,
                "why": "ImageIcon loads the file and can be given straight to a JLabel or a JButton.",
            },
            {
                "q": "drawImage() needs an observer argument because:",
                "options": [
                    "the image may still be loading and Java repaints as more of it arrives",
                    "the image must be resized first",
                    "the colours have to be converted",
                    "the file must be closed afterwards",
                ],
                "answer": 0,
                "why": "The observer is told when a new part of the image is ready, which triggers another repaint.",
            },
            {
                "q": "Which statement about image handling in Java is NOT correct?",
                "options": [
                    "An image is a grid of pixels",
                    "PixelGrabber copies pixels into an array",
                    "MemoryImageSource builds an image from an array of pixels",
                    "drawImage must be called from main()",
                ],
                "answer": 3,
                "why": "Drawing belongs in paint(), which the system calls; main() is not a drawing method.",
            },
            {
                "q": "Changing every pixel of an image requires access to:",
                "options": ["the pixel array", "the file name", "the Font object", "the layout manager"],
                "answer": 0,
                "why": "PixelGrabber hands you the pixels as an int array, which is what you edit and turn back into an image.",
            },
        ],
        "examTip": "One line each for the three names: getImage or ImageIcon to load, drawImage to show, PixelGrabber with MemoryImageSource to process.",
    },
}
