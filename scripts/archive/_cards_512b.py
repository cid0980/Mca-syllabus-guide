# CSCA 512 Internet and Web Technologies - Module II
# HTML structure, formatting, links, lists, tables, forms, CSS syntax and layout.

CODE = "CSCA512"

CARDS = {
    "CSCA512-MII-T01": {
        "explanation": "HTML is the markup language that gives structure and meaning to web content. A document opens with a DOCTYPE, then an html element containing a head and a body. The head holds the title and meta tags, and the body holds everything the reader sees. Elements are written with an opening tag, content and a closing tag, and attributes such as id, class and src configure them. HTML5 added semantic elements: header, nav, main, section, article, aside, figure and footer each say what their part is. It also added native audio and video, canvas, SVG, local storage, web workers and better form inputs.",
        "example": "Writing nav around the menu links tells a screen reader that this block is navigation, not ordinary text.",
        "quiz": [
            {
                "q": "Which element holds the visible content of a page?",
                "options": ["head", "title", "body", "meta"],
                "answer": 2,
                "why": "The head carries metadata, and everything the reader sees sits in the body.",
            },
            {
                "q": "Which HTML5 element marks the main navigation block?",
                "options": ["div", "nav", "section", "aside"],
                "answer": 1,
                "why": "Semantic elements describe the role of a block, which helps browsers and assistive tools.",
            },
            {
                "q": "Which statement about HTML is NOT correct?",
                "options": ["Elements usually have opening and closing tags", "Attributes such as id and class configure elements", "The DOCTYPE declares the document type", "HTML5 removed every formatting element such as b and i"],
                "answer": 3,
                "why": "Elements such as b and i still exist, though CSS is the preferred way to style text.",
            },
            {
                "q": "Which HTML5 feature draws graphics with script?",
                "options": ["canvas", "footer", "nav", "meta"],
                "answer": 0,
                "why": "The canvas element gives a drawing surface that JavaScript can paint on.",
            },
            {
                "q": "What does a meta tag do?",
                "options": ["Displays a heading", "Carries metadata such as character set and viewport", "Creates a link", "Adds an image"],
                "answer": 1,
                "why": "Meta tags describe the document itself rather than displaying content.",
            },
        ],
        "examTip": "Sketch the document skeleton, name four semantic elements and four HTML5 features.",
    },

    "CSCA512-MII-T02": {
        "explanation": "Formatting elements change the appearance or the meaning of text. The b and i elements make text bold and italic. The strong and em elements carry importance and emphasis, which matters to screen readers. Other elements include u, sub, sup, mark, small and del. Comments let a developer leave notes in the file, and the browser ignores them completely. Old HTML set fonts and colours with the font tag and with attributes on the body element. Modern pages use CSS instead, with font-family, size and colour, which keeps presentation separate from content.",
        "example": "Using strong instead of b means a screen reader can stress the word rather than ignore the styling.",
        "quiz": [
            {
                "q": "Which element indicates importance rather than bold styling?",
                "options": ["b", "strong", "i", "u"],
                "answer": 1,
                "why": "strong carries meaning, while b only changes the appearance.",
            },
            {
                "q": "What happens to an HTML comment in the browser?",
                "options": ["It is shown in small text", "It is ignored and never rendered", "It is printed at the top of the page", "It becomes a tooltip"],
                "answer": 1,
                "why": "Comments exist for the people reading the source, not for the reader of the page.",
            },
            {
                "q": "Which statement about formatting is NOT correct?",
                "options": ["mark highlights text", "sup raises text above the line", "The font tag is the recommended way to set type", "CSS is preferred for fonts and colours"],
                "answer": 2,
                "why": "The font element is obsolete, and CSS replaced it.",
            },
            {
                "q": "Which element marks text that has been deleted?",
                "options": ["del", "small", "mark", "sub"],
                "answer": 0,
                "why": "del carries the meaning of removal, which is why it suits edit histories.",
            },
            {
                "q": "How is text coloured in a modern page?",
                "options": ["With the font tag", "With the CSS color property", "With the body attribute", "With the title tag"],
                "answer": 1,
                "why": "CSS separates presentation from content, so one change updates every page.",
            },
        ],
        "examTip": "List four formatting elements, explain strong versus b, and say why CSS replaced the font tag.",
    },

    "CSCA512-MII-T03": {
        "explanation": "The a element creates a link, and its href attribute says where the link goes. That destination may be another page, a section of the same page, an email address or a file to download. Links are internal when they stay inside the site and external when they leave it. A fragment link jumps to an element with a matching id. The target attribute decides where the result opens, such as in a new tab. Images use the img element with src for the file and alt for the text alternative. Formats differ in purpose: JPEG suits photographs and PNG suits sharp graphics. GIF suits simple animation, SVG suits scalable drawings and WebP gives smaller files.",
        "example": "An image with a missing alt attribute leaves a screen reader with nothing to announce. A short description fixes that.",
        "quiz": [
            {
                "q": "Which attribute holds the destination of a link?",
                "options": ["src", "href", "alt", "target"],
                "answer": 1,
                "why": "href names the target resource, while src is used for embedded files such as images.",
            },
            {
                "q": "What is a fragment link?",
                "options": ["A broken link", "A link to a section of the same page using an id", "A link to another site", "A link that opens a file"],
                "answer": 1,
                "why": "The URL ends with a hash and the element id, so the browser scrolls to that place.",
            },
            {
                "q": "Which statement about images is NOT correct?",
                "options": ["src names the image file", "alt provides a text alternative", "SVG loses quality when enlarged", "WebP usually produces smaller files than JPEG"],
                "answer": 2,
                "why": "SVG is vector based, so it stays sharp at any size.",
            },
            {
                "q": "Which attribute opens a link in a new tab?",
                "options": ["href", "target", "rel", "alt"],
                "answer": 1,
                "why": "Setting target makes the browser open the result in a new tab or a named frame.",
            },
            {
                "q": "Which image format suits a logo that must scale?",
                "options": ["JPEG", "GIF", "SVG", "WebP"],
                "answer": 2,
                "why": "SVG describes shapes rather than pixels, so it scales without losing sharpness.",
            },
        ],
        "examTip": "Write an anchor tag with href and target, list three link types, and compare four image formats.",
    },

    "CSCA512-MII-T04": {
        "explanation": "Lists group related items, and there are three kinds. An ordered list numbers its items and an unordered list marks them with bullets. A definition list pairs a term with its description. Each item is written with li, and lists may be nested inside one another. Tables arrange data in rows and columns using table, tr, th and td, with caption, thead and tbody giving structure. A cell can span several rows or columns with rowspan and colspan. Framesets once split a window into panes but are obsolete now, while the iframe element embeds another document inside a page.",
        "example": "A timetable needs a table with th for the days and td for each subject. A list would lose the row and column structure.",
        "quiz": [
            {
                "q": "Which list pairs a term with its description?",
                "options": ["ol", "ul", "dl", "li"],
                "answer": 2,
                "why": "A definition list uses dl with dt for the term and dd for the description.",
            },
            {
                "q": "Which element marks a header cell in a table?",
                "options": ["td", "th", "tr", "caption"],
                "answer": 1,
                "why": "th marks a header cell and td an ordinary data cell, and browsers style them differently.",
            },
            {
                "q": "Which statement about tables is NOT correct?",
                "options": ["thead groups the header rows", "colspan makes a cell span columns", "rowspan makes a cell span rows", "Tables should be used to lay out a whole page"],
                "answer": 3,
                "why": "Layout is a CSS job, and tables are meant for data with rows and columns.",
            },
            {
                "q": "Which element embeds another document inside a page?",
                "options": ["frameset", "iframe", "frame", "div"],
                "answer": 1,
                "why": "The iframe element is still supported, while framesets were removed from HTML5.",
            },
            {
                "q": "Which element gives a table a title?",
                "options": ["caption", "thead", "title", "legend"],
                "answer": 0,
                "why": "caption is placed inside the table element and describes what the table shows.",
            },
        ],
        "examTip": "Name the three list types with their tags, the table tags, and explain rowspan, colspan and iframe.",
    },

    "CSCA512-MII-T05": {
        "explanation": "A form collects user input and sends it to a server for processing. The form element names the processing URL with action and the sending method with method, usually GET or POST. Inside it, the input element covers many types: text, password, email, number, date, radio, checkbox, file, hidden, submit and reset. Drop down lists use select with option, longer text uses textarea, and button gives a clickable control. Every control should have a name, because that is what the server reads. Labels and fieldsets improve accessibility, and attributes such as required, pattern, min and max validate input in the browser before submission.",
        "example": "A signup form with required on the email field stops an empty submission before any request reaches the server.",
        "quiz": [
            {
                "q": "Which attribute names the script that will process a form?",
                "options": ["method", "action", "name", "id"],
                "answer": 1,
                "why": "action gives the destination URL, while method says how the data will be sent.",
            },
            {
                "q": "When should POST be used instead of GET?",
                "options": ["For short search terms", "For sensitive or large data, sent in the request body", "For links between pages", "For loading images"],
                "answer": 1,
                "why": "GET puts data in the URL, which is visible and limited in size.",
            },
            {
                "q": "Which statement about forms is NOT correct?",
                "options": ["A control needs a name to be submitted", "textarea suits multi-line text", "select creates a drop down list", "Client side validation is enough on its own"],
                "answer": 3,
                "why": "Browser validation can be bypassed, so the server must validate as well.",
            },
            {
                "q": "Which element ties a caption to a control?",
                "options": ["legend", "label", "fieldset", "span"],
                "answer": 1,
                "why": "A label with a for attribute makes the caption clickable and helps screen readers.",
            },
            {
                "q": "Which input type shows dots instead of characters?",
                "options": ["text", "password", "hidden", "number"],
                "answer": 1,
                "why": "The password type masks what is typed, though it does not encrypt the value sent.",
            },
        ],
        "examTip": "Write a form tag with action and method, list five input types, and explain labels and validation.",
    },

    "CSCA512-MII-T06": {
        "explanation": "CSS separates presentation from content and controls layout, colour and typography. It is needed because one stylesheet keeps a whole site consistent, makes maintenance easier and keeps HTML smaller. A rule has a selector and a declaration block of property value pairs, each ending with a semicolon. There are three ways to apply it. An inline style goes in the style attribute of one element and has the highest priority. An embedded sheet sits in a style element in the head and applies to one page. An external sheet is linked with the link element, and one file then styles an entire site.",
        "example": "Changing a colour in one linked stylesheet updates every page at once. Copying that change into fifty files would take hours.",
        "quiz": [
            {
                "q": "Which type of stylesheet affects an entire site?",
                "options": ["Inline", "Embedded", "External", "Imported"],
                "answer": 2,
                "why": "One external file is linked from every page, so a single edit updates them all.",
            },
            {
                "q": "What are the two parts of a CSS rule?",
                "options": ["A tag and an attribute", "A selector and a declaration block", "A class and an id", "A head and a body"],
                "answer": 1,
                "why": "The selector chooses the elements and the declarations say what to change.",
            },
            {
                "q": "Which statement about CSS is NOT correct?",
                "options": ["Inline styles have the highest priority", "More specific selectors override less specific ones", "Some properties are inherited from parent to child", "External styles always override inline styles"],
                "answer": 3,
                "why": "Inline styles win over external ones, which is why they are used sparingly.",
            },
            {
                "q": "Which element links an external stylesheet?",
                "options": ["style", "link", "script", "meta"],
                "answer": 1,
                "why": "The link element with rel stylesheet and an href points to the CSS file.",
            },
            {
                "q": "Why is CSS preferred over formatting tags?",
                "options": ["It loads faster than HTML", "It keeps presentation separate from content", "It is required by HTML5", "It works without a browser"],
                "answer": 1,
                "why": "Separation means the look can change without touching the structure or the text.",
            },
        ],
        "examTip": "Explain why CSS is needed, write a rule, and compare inline, embedded and external stylesheets.",
    },

    "CSCA512-MII-T07": {
        "explanation": "CSS controls typography, colour, spacing and the position of every element. Text is shaped with font-family, font-size, font-weight, line-height, letter-spacing, text-align and text-decoration. Backgrounds take a colour, a gradient or an image, and borders get rounded corners and shadows. The box model is the key idea: content, padding, border and margin. Box-sizing decides whether padding counts towards the declared width. Position can be static, relative, absolute, fixed or sticky, with z-index setting the stacking order. Layout uses floats for wrapping text, flexbox for one dimension and grid for two. Media queries adapt the layout to smaller screens.",
        "example": "A card with 20 pixels of padding and a 1 pixel border is 42 pixels wider than its content unless box-sizing is set to border-box.",
        "quiz": [
            {
                "q": "What is the correct order of the box model from the inside out?",
                "options": ["Content, margin, border, padding", "Content, padding, border, margin", "Padding, content, border, margin", "Border, padding, content, margin"],
                "answer": 1,
                "why": "Padding is inside the border, and margin is the space outside it.",
            },
            {
                "q": "Which positioning value keeps an element in place while the page scrolls?",
                "options": ["static", "relative", "absolute", "fixed"],
                "answer": 3,
                "why": "Fixed positioning removes the element from the flow and pins it to the viewport.",
            },
            {
                "q": "Which statement about layout is NOT correct?",
                "options": ["Flexbox handles one dimension at a time", "Grid handles rows and columns together", "Media queries support responsive design", "Floats are the best tool for a full page layout"],
                "answer": 3,
                "why": "Floats suit wrapping text around an image, while flexbox and grid handle real layouts.",
            },
            {
                "q": "What does box-sizing border-box do?",
                "options": ["Adds a border", "Includes padding and border in the declared width", "Removes the margin", "Centres the element"],
                "answer": 1,
                "why": "Without it, padding and border are added on top of the width you set.",
            },
            {
                "q": "What does z-index control?",
                "options": ["The zoom level", "The stacking order of overlapping elements", "The font size", "The page width"],
                "answer": 1,
                "why": "A higher z-index draws an element in front of one with a lower value.",
            },
        ],
        "examTip": "Draw the box model, list the five position values, and compare float, flexbox and grid.",
    },
}
