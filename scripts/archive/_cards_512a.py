# CSCA 512 Internet and Web Technologies - Module I
# Internet standards, web architecture, mail and transfer protocols, HTTP, dynamic pages.

CODE = "CSCA512"

CARDS = {
    "CSCA512-MI-T01": {
        "explanation": "Internet standards are agreed specifications that let systems from different vendors work together. They begin as requests for comments, the working documents of the Internet Engineering Task Force. A specification moves through maturity levels: proposed standard, draft standard and then Internet standard, while some stay experimental or become historic. Other bodies matter too: W3C standardises web technologies, ISO covers information technology broadly, and IEEE standardises local area networks. The point of all of it is interoperability. Any browser can talk to any server because both follow the same written rules.",
        "example": "A phone from one maker loads a page hosted on another because HTTP and HTML are written down and agreed by everyone.",
        "quiz": [
            {
                "q": "What is an RFC?",
                "options": ["A registered file company", "A request for comments, the working document of the IETF", "A router configuration file", "A radio frequency channel"],
                "answer": 1,
                "why": "Every Internet protocol is published as an RFC before it can become a standard.",
            },
            {
                "q": "Which organisation standardises web technologies such as HTML and CSS?",
                "options": ["IEEE", "ISO", "W3C", "ITU"],
                "answer": 2,
                "why": "The World Wide Web Consortium publishes the specifications that browsers implement.",
            },
            {
                "q": "Which statement about Internet standards is NOT correct?",
                "options": ["They pass through proposed and draft stages", "They let equipment from different vendors interoperate", "IEEE standardises local area networks", "A standard is final the moment it is first written"],
                "answer": 3,
                "why": "Maturity levels exist so a specification is tested in practice before it becomes final.",
            },
            {
                "q": "Which maturity level comes after draft standard?",
                "options": ["Proposed standard", "Internet standard", "Experimental", "Historic"],
                "answer": 1,
                "why": "The sequence runs proposed, then draft, then Internet standard.",
            },
            {
                "q": "Why do standards matter most?",
                "options": ["They make equipment cheaper to manufacture", "They give interoperability between products from different vendors", "They reduce the number of protocols", "They make the Internet faster"],
                "answer": 1,
                "why": "Interoperability is why a browser and a server written by different teams can communicate.",
            },
        ],
        "examTip": "Define RFC, give the roles of IETF, W3C, ISO and IEEE, and list the maturity levels in order.",
    },

    "CSCA512-MI-T02": {
        "explanation": "The web is an information system of linked hypertext documents reached over the Internet. A web page is one document, a website is a collection of related pages, and hyperlinks connect them. The browser requests and renders content, while the web server stores it and sends it when asked. Pages may be static, stored ready made and sent unchanged, or dynamic, built for each request. The web has moved through three broad stages: read only pages, then social and interactive applications, then semantic and decentralised ideas.",
        "example": "A college notice page that never changes is static. The same site's results page, built when you enter a roll number, is dynamic.",
        "quiz": [
            {
                "q": "What is the difference between a web page and a website?",
                "options": ["They are the same", "A page is one document, a site is a collection of related pages", "A site is one file", "A page contains many sites"],
                "answer": 1,
                "why": "The site is the container and each page is a document inside it.",
            },
            {
                "q": "Which statement about static pages is NOT correct?",
                "options": ["They are stored ready made", "They are sent unchanged to every visitor", "They are generated separately for each request", "They suit content that rarely changes"],
                "answer": 2,
                "why": "Building a page for each request is what a dynamic page does.",
            },
            {
                "q": "What is the role of a web server?",
                "options": ["To display pages to the user", "To store content and deliver it when requested", "To connect the user to the Internet", "To write the HTML"],
                "answer": 1,
                "why": "The server waits for requests, and the browser is what renders the response.",
            },
            {
                "q": "Which describes Web 2.0?",
                "options": ["Read only pages", "Social and interactive applications", "Semantic and decentralised ideas", "Static HTML only"],
                "answer": 1,
                "why": "Web 2.0 is the stage where users create content as well as read it.",
            },
            {
                "q": "What connects one document to another on the web?",
                "options": ["A server", "A hyperlink", "A browser tab", "A cookie"],
                "answer": 1,
                "why": "Hyperlinks are what make the web a web rather than a pile of documents.",
            },
        ],
        "examTip": "Define web page, website and hyperlink, contrast static and dynamic pages, and name the three web stages.",
    },

    "CSCA512-MI-T03": {
        "explanation": "Web architecture describes how browsers, servers and the network cooperate to deliver content. The web uses the client server model: the browser is the client and the web server is the server. HTTP carries the requests and responses between them. Larger applications add a three tier structure, with a presentation tier, an application logic tier and a data tier. Common server software includes Apache, Nginx and IIS, all serving files from a document root with configuration for virtual hosts. Caching shortens the journey: forward and reverse proxies and content delivery networks keep copies closer to the user.",
        "example": "A news site uses a CDN so that a reader in Chennai loads images from a nearby server rather than one in another country.",
        "quiz": [
            {
                "q": "What are the three tiers of web architecture?",
                "options": ["Client, server, network", "Presentation, application logic and data", "Browser, router, database", "HTML, CSS, JavaScript"],
                "answer": 1,
                "why": "Separating interface, rules and storage lets each tier be changed alone.",
            },
            {
                "q": "Which is a web server?",
                "options": ["Chrome", "Nginx", "Windows", "MySQL"],
                "answer": 1,
                "why": "Nginx, Apache and IIS are server software; the others are a browser, an operating system and a database.",
            },
            {
                "q": "Which statement about web architecture is NOT correct?",
                "options": ["The browser acts as the client", "HTTP carries requests and responses", "A reverse proxy sits in front of the servers", "A CDN makes the origin server unnecessary"],
                "answer": 3,
                "why": "A CDN caches copies, but the origin server still holds the authoritative content.",
            },
            {
                "q": "What is the document root?",
                "options": ["The folder the server serves files from", "The user's home directory", "The browser cache", "The database folder"],
                "answer": 0,
                "why": "A URL path is mapped to a file inside that directory on the server.",
            },
            {
                "q": "What does a forward proxy do?",
                "options": ["Hides the server from clients", "Acts on behalf of clients, often for caching and filtering", "Stores the database", "Encrypts the disk"],
                "answer": 1,
                "why": "It stands between users and the Internet, which lets an organisation cache and control traffic.",
            },
        ],
        "examTip": "Draw the client server model, name the three tiers, two servers and two caching mechanisms.",
    },

    "CSCA512-MI-T04": {
        "explanation": "Email is delivered by push protocols and retrieved by pull protocols. SMTP is the push protocol: it runs on port 25 and moves mail from a client to a server and between servers. POP3 is a pull protocol on port 110 that downloads messages and usually deletes them from the server. IMAP, on port 143, keeps the mail on the server, supports folders and synchronises across devices. A message itself has headers and a body defined by RFC 822, and MIME extends it so that attachments and non-ASCII content can travel.",
        "example": "Reading office mail on a phone and a laptop with the same folders is IMAP at work. POP3 would have emptied the server on the first device.",
        "quiz": [
            {
                "q": "Which protocol sends mail from a client to a server?",
                "options": ["POP3", "IMAP", "SMTP", "HTTP"],
                "answer": 2,
                "why": "SMTP pushes the message onward, which is why it is called a push protocol.",
            },
            {
                "q": "Which protocol keeps mail on the server and synchronises across devices?",
                "options": ["POP3", "IMAP", "SMTP", "FTP"],
                "answer": 1,
                "why": "IMAP manages folders on the server, so every device sees the same state.",
            },
            {
                "q": "Which statement about email protocols is NOT correct?",
                "options": ["SMTP uses port 25", "POP3 uses port 110", "IMAP uses port 143", "POP3 is the best choice for reading mail on several devices"],
                "answer": 3,
                "why": "POP3 downloads and often deletes, which leaves other devices without the messages.",
            },
            {
                "q": "What does MIME add to email?",
                "options": ["Faster delivery", "Support for attachments and non-ASCII content", "Encryption by default", "Spam filtering"],
                "answer": 1,
                "why": "MIME extends the plain text format of RFC 822 with multipart bodies and encodings.",
            },
            {
                "q": "Which port does IMAP use?",
                "options": ["25", "110", "143", "21"],
                "answer": 2,
                "why": "Port 143 is the standard IMAP port, with 993 used for IMAP over TLS.",
            },
        ],
        "examTip": "Compare SMTP, POP3 and IMAP with port numbers and one behaviour each, and mention MIME.",
    },

    "CSCA512-MI-T05": {
        "explanation": "FTP moves files between a client and a server using two separate connections. The control connection on port 21 carries the commands, and a second data connection carries the file itself. In active mode the server opens the data connection back to the client, which firewalls often block. In passive mode the client opens the data connection instead, which works through most firewalls. The commands are simple: USER, PASS, RETR, STOR, LIST and QUIT, each answered with a three digit reply code. Because FTP sends everything in the clear, SFTP over SSH and FTPS over TLS are used where the transfer must stay private.",
        "example": "A designer uploads a site with an FTP client. When the client sits behind a firewall, switching to passive mode usually fixes a stalled transfer.",
        "quiz": [
            {
                "q": "Which port carries FTP commands?",
                "options": ["20", "21", "25", "110"],
                "answer": 1,
                "why": "Port 21 is the control connection, while the data connection uses another port.",
            },
            {
                "q": "Which mode works better through a firewall?",
                "options": ["Active mode", "Passive mode", "Both work equally well", "Neither works at all"],
                "answer": 1,
                "why": "Passive mode has the client open the data connection, which outbound rules usually allow.",
            },
            {
                "q": "Which statement about FTP is NOT correct?",
                "options": ["It uses two connections", "RETR downloads a file", "STOR uploads a file", "FTP encrypts the data by default"],
                "answer": 3,
                "why": "Plain FTP sends credentials and files unencrypted, which is why SFTP and FTPS exist.",
            },
            {
                "q": "What does the FTP command LIST do?",
                "options": ["Downloads a file", "Lists the files in the current directory", "Deletes a file", "Renames a file"],
                "answer": 1,
                "why": "It returns a directory listing over the data connection.",
            },
            {
                "q": "What is FTPS?",
                "options": ["FTP over SSH", "FTP over TLS", "A faster version of FTP", "A file type"],
                "answer": 1,
                "why": "FTPS adds TLS encryption to FTP, while SFTP runs over SSH instead.",
            },
        ],
        "examTip": "Describe the two FTP connections, compare active and passive mode, and name two secure alternatives.",
    },

    "CSCA512-MI-T06": {
        "explanation": "HTTP is the request response protocol of the web, and it is stateless: the server keeps no memory of earlier requests. A request has a request line with the method and URL, headers, a blank line and an optional body. A response has a status line, headers such as content type and length, a blank line and the body. The common methods are GET, POST, PUT, DELETE, PATCH, HEAD and OPTIONS, and status codes fall into classes from 1xx to 5xx. Headers carry metadata, and cookies let a stateful session be built on a stateless protocol. Keep alive lets many requests share one TCP connection, and HTTPS puts the whole exchange inside TLS.",
        "example": "A 404 means the page was not found and a 500 means the server failed. Both are three digit codes in the status line.",
        "quiz": [
            {
                "q": "What does HTTP status code 404 mean?",
                "options": ["The request succeeded", "The resource was not found", "The server had an error", "The request was redirected"],
                "answer": 1,
                "why": "Codes in the 4xx class report a problem with the request, and 404 is the familiar one.",
            },
            {
                "q": "Which method asks the server for a resource without changing anything?",
                "options": ["POST", "PUT", "GET", "DELETE"],
                "answer": 2,
                "why": "GET retrieves, while POST, PUT and DELETE are meant to change something.",
            },
            {
                "q": "Which statement about HTTP is NOT correct?",
                "options": ["It is a request response protocol", "A request has a request line, headers and an optional body", "Cookies make the protocol stateful by themselves", "HTTPS runs HTTP over TLS"],
                "answer": 2,
                "why": "HTTP stays stateless; cookies are data the client returns so a session can be rebuilt.",
            },
            {
                "q": "What is the purpose of the Keep Alive header?",
                "options": ["To keep the server running", "To reuse one TCP connection for several requests", "To store cookies", "To compress the body"],
                "answer": 1,
                "why": "Reusing the connection avoids the cost of a new handshake for every resource.",
            },
            {
                "q": "Which status class indicates a server error?",
                "options": ["2xx", "3xx", "4xx", "5xx"],
                "answer": 3,
                "why": "5xx codes mean the server failed, while 4xx codes mean the request was at fault.",
            },
        ],
        "examTip": "Sketch a request and a response, name five methods and the five status classes, and explain cookies and HTTPS.",
    },

    "CSCA512-MI-T07": {
        "explanation": "Dynamic pages are built when the request arrives, on the server, on the client or on both. The oldest approach is the Common Gateway Interface, where the server starts a separate program for each request, which is simple but slow. Server side scripting is the usual answer now. PHP, JSP, ASP.NET, Python or Node.js builds the HTML on the server before it is sent. Client side scripting works the other way, with JavaScript in the browser updating the page without a full reload. Templating and server side includes tie it together, combining reusable fragments with data to produce the final page.",
        "example": "A weather page built by PHP on the server shows fresh data on every load. The same page can then update one number with JavaScript, without reloading.",
        "quiz": [
            {
                "q": "What is the main drawback of CGI?",
                "options": ["It is too secure", "A new process starts for every request, which is slow", "It cannot produce HTML", "It works only on Windows"],
                "answer": 1,
                "why": "Process creation costs time and memory, so CGI scales poorly.",
            },
            {
                "q": "Which runs on the server and is invisible to the user?",
                "options": ["JavaScript", "PHP", "CSS", "HTML"],
                "answer": 1,
                "why": "The server executes PHP and sends only the resulting HTML, so the source never reaches the browser.",
            },
            {
                "q": "Which statement about dynamic pages is NOT correct?",
                "options": ["They can be built on the server", "They can be built in the browser", "Templates combine fragments with data", "Every dynamic page needs a database"],
                "answer": 3,
                "why": "A page can be dynamic from a clock, a file or an API, not only from a database.",
            },
            {
                "q": "What does client side scripting avoid?",
                "options": ["Using a server", "A full page reload", "Writing JavaScript", "Sending any request"],
                "answer": 1,
                "why": "JavaScript updates part of the page, so the user does not wait for a new document.",
            },
            {
                "q": "Which of these is a server side technology?",
                "options": ["ASP.NET", "CSS", "The DOM", "Cookies"],
                "answer": 0,
                "why": "ASP.NET, PHP, JSP and Node.js all run on the server before the response is sent.",
            },
        ],
        "examTip": "Define a dynamic page, describe CGI and its drawback, and contrast server side and client side scripting.",
    },
}
