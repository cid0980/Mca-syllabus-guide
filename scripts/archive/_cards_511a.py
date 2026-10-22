# CSCA 511 Software Engineering - Modules I and II
# Process models, agile, requirements engineering, design concepts and UI design.

CODE = "CSCA511"

CARDS = {
    "CSCA511-MI-T01": {
        "explanation": "A software process is the set of activities and results needed to build a software product. Its framework activities are communication, planning, modelling, construction and deployment, in that broad order. Umbrella activities run alongside all of them for the whole project: tracking, risk management, quality assurance, configuration management and reviews. A generic framework is made specific by choosing task sets, the work products each task produces and the quality checkpoints it must pass. Process patterns then capture solutions to problems that recur from project to project. Process assessment, often against CMMI, asks how mature and repeatable the process actually is.",
        "example": "Two teams can build the same app. The one that tracks risk and holds reviews from the first week usually ships with fewer surprises.",
        "quiz": [
            {
                "q": "Which is a framework activity?",
                "options": ["Risk management", "Configuration management", "Construction", "Quality assurance"],
                "answer": 2,
                "why": "Construction is one of the five framework activities, while the others listed are umbrella activities.",
            },
            {
                "q": "Which is an umbrella activity?",
                "options": ["Deployment", "Modelling", "Software quality assurance", "Communication"],
                "answer": 2,
                "why": "Umbrella activities run across the whole project rather than belonging to one phase.",
            },
            {
                "q": "Which statement about the software process is NOT correct?",
                "options": ["Framework activities include planning and modelling", "Umbrella activities run throughout the project", "Task sets tailor the framework to a project", "A process pattern is a design pattern for code"],
                "answer": 3,
                "why": "Process patterns solve recurring process problems, while design patterns solve code structure problems.",
            },
            {
                "q": "What does CMMI assess?",
                "options": ["The speed of the compiler", "The maturity of an organisation's processes", "The size of the team", "The price of the product"],
                "answer": 1,
                "why": "Maturity levels describe how well defined, managed and improved the process is.",
            },
            {
                "q": "What does a task set define?",
                "options": ["The team's salaries", "The tasks, work products and quality checkpoints for a project", "The office layout", "The marketing plan"],
                "answer": 1,
                "why": "Choosing a task set is how a generic framework is fitted to a real project.",
            },
        ],
        "examTip": "Name the five framework activities, five umbrella activities, and define task sets and process patterns.",
    },

    "CSCA511-MI-T02": {
        "explanation": "A process model is a strategy for arranging the framework activities across the life of a project. The waterfall model moves through requirements, design, code, test and maintenance in order, which is clear but poor at handling change. The incremental model delivers the product in parts, each part adding working functionality and giving early feedback. The prototyping model builds a quick version first, either thrown away or evolved, to settle unclear requirements. The spiral model is risk driven, cycling through planning, risk analysis, engineering and evaluation. The V model pairs each development phase with the test that checks it, and the concurrent model shows activities running in parallel states.",
        "example": "A government form processing system with fixed rules suits waterfall. A startup app whose requirements change weekly does not.",
        "quiz": [
            {
                "q": "Which model is risk driven and iterative?",
                "options": ["Waterfall", "Spiral", "RAD", "V model"],
                "answer": 1,
                "why": "Each loop of the spiral begins with risk analysis, which decides what happens next.",
            },
            {
                "q": "What does the V model pair?",
                "options": ["Each developer with a tester", "Each development phase with its matching test phase", "Each requirement with a budget", "Each module with a document"],
                "answer": 1,
                "why": "Requirements match acceptance testing, design matches system testing, and so on down the V.",
            },
            {
                "q": "Which statement about process models is NOT correct?",
                "options": ["Waterfall handles change poorly", "Incremental delivery gives early feedback", "Prototyping helps clarify unclear requirements", "RAD is slow and needs no user involvement"],
                "answer": 3,
                "why": "RAD is built for speed through components and short cycles, and it needs heavy user involvement.",
            },
            {
                "q": "Which model delivers working functionality in parts?",
                "options": ["Waterfall", "Incremental model", "Prototyping model", "Spiral model"],
                "answer": 1,
                "why": "Each increment is a usable slice of the product, not another document.",
            },
            {
                "q": "What is a throwaway prototype?",
                "options": ["A prototype rewritten in another language", "A quick model built to learn the requirements, then discarded", "The final product", "A test harness"],
                "answer": 1,
                "why": "Its value is the understanding it produces, not the code itself.",
            },
        ],
        "examTip": "Compare waterfall, incremental, prototyping and spiral with one strength and one weakness each.",
    },

    "CSCA511-MI-T03": {
        "explanation": "Agile development delivers working software in short iterations, with the customer involved throughout. The manifesto values individuals and interactions, working software, customer collaboration and response to change over the opposite four. Extreme Programming is one agile method, built on planning games, small releases, simple design, test first development, pair programming and continuous integration. Scrum works in sprints of two to four weeks, with a product backlog, a sprint backlog, a daily stand up, a review and a retrospective. Kanban visualises the work and limits work in progress, and DevOps joins development to operations for continuous delivery. Agile suits changing requirements and small teams.",
        "example": "A team releases a working build every two weeks and shows it to the client. The client's reaction becomes the next sprint's plan.",
        "quiz": [
            {
                "q": "How long is a Scrum sprint?",
                "options": ["One day", "Two to four weeks", "Six months", "One year"],
                "answer": 1,
                "why": "The sprint is short enough to keep feedback frequent and long enough to finish real work.",
            },
            {
                "q": "Which is an Extreme Programming practice?",
                "options": ["Pair programming", "Monthly releases", "Big design up front", "A separate test team only"],
                "answer": 0,
                "why": "Two people work at one machine, which spreads knowledge and catches defects early.",
            },
            {
                "q": "Which statement about agile is NOT correct?",
                "options": ["It welcomes changing requirements", "It values working software over documents", "It suits small co-located teams", "It forbids any documentation or planning"],
                "answer": 3,
                "why": "The manifesto prefers working software, it does not ban documents or plans.",
            },
            {
                "q": "What does Kanban limit?",
                "options": ["Team size", "Work in progress", "Number of meetings", "Lines of code"],
                "answer": 1,
                "why": "Capping unfinished work exposes bottlenecks and keeps the flow steady.",
            },
            {
                "q": "What happens in a sprint retrospective?",
                "options": ["The product is shipped", "The team reviews how it worked and what to improve", "Requirements are frozen", "The budget is set"],
                "answer": 1,
                "why": "It is the team's own review of its process, held after the review of the product.",
            },
        ],
        "examTip": "State the four agile values, name three XP practices and the five Scrum events.",
    },

    "CSCA511-MI-T04": {
        "explanation": "Requirements engineering establishes what the system must do, and writes it so it can be checked and used for design. Requirements come in three kinds: functional, non functional and domain. Functional requirements describe services, and non functional ones describe qualities such as speed or security. Elicitation gathers them through interviews, questionnaires, observation, document study, brainstorming, prototyping and joint application development. Conflict between stakeholders is then resolved by negotiation and prioritisation, using schemes such as MoSCoW. The results go into the Software Requirements Specification, which is then validated for completeness, consistency, feasibility and testability.",
        "example": "The system must respond within two seconds is a non functional requirement. The system must issue a library card describes a function.",
        "quiz": [
            {
                "q": "Which requirement states a quality such as speed or security?",
                "options": ["Functional", "Non functional", "Domain", "Interface"],
                "answer": 1,
                "why": "Non functional requirements constrain how the system behaves rather than what it does.",
            },
            {
                "q": "What is the SRS?",
                "options": ["The source code", "The Software Requirements Specification document", "The test plan", "The project schedule"],
                "answer": 1,
                "why": "It records functional and non functional requirements, interfaces and constraints.",
            },
            {
                "q": "Which statement about requirements is NOT correct?",
                "options": ["Elicitation uses interviews and observation", "Requirements must be testable", "Conflicts between stakeholders are negotiated", "Requirements are frozen the day they are written"],
                "answer": 3,
                "why": "Change is expected, which is why baselines and change control exist.",
            },
            {
                "q": "What does MoSCoW stand for?",
                "options": ["A city", "Must, should, could, won't have this time", "Most, some, certain, others", "Money, scope, cost, work"],
                "answer": 1,
                "why": "It is a prioritisation scheme that forces a decision on every requirement.",
            },
            {
                "q": "What is requirements traceability?",
                "options": ["Tracking each requirement to its source and to the tests that check it", "Counting the requirements", "Sorting them by date", "Sending them by email"],
                "answer": 0,
                "why": "Traceability shows that every requirement is tested and every test serves a requirement.",
            },
        ],
        "examTip": "Define the three requirement types, list four elicitation techniques and four validation checks.",
    },

    "CSCA511-MII-T01": {
        "explanation": "Design concepts are the principles that make a design understandable, changeable and reliable. Abstraction hides detail at a chosen level, and stepwise refinement adds that detail back gradually. Modularity splits the system into parts, and information hiding keeps each part's internals private so that a change stays local. Two measures show whether the split was good. Coupling between modules should be low, and cohesion inside a module should be high. Refactoring improves the internal structure without changing what the software does. The design model itself has four parts: data design, architectural design, interface design and component level design.",
        "example": "A module that reads a file, formats it and emails it has low cohesion. Splitting it into three modules raises cohesion and lowers coupling.",
        "quiz": [
            {
                "q": "What combination gives a maintainable design?",
                "options": ["High coupling, low cohesion", "Low coupling, high cohesion", "High coupling, high cohesion", "Low coupling, low cohesion"],
                "answer": 1,
                "why": "Modules that depend little on each other can be changed one at a time without surprises.",
            },
            {
                "q": "What is information hiding?",
                "options": ["Encrypting the database", "Keeping a module's internals private behind its interface", "Hiding the source code from users", "Removing comments"],
                "answer": 1,
                "why": "Callers depend on the interface, so the internals can change without breaking them.",
            },
            {
                "q": "Which statement about design is NOT correct?",
                "options": ["Abstraction hides detail at a level", "Stepwise refinement adds detail gradually", "Refactoring changes the external behaviour", "Design has data, architectural, interface and component parts"],
                "answer": 2,
                "why": "Refactoring improves internal structure while the behaviour stays exactly the same.",
            },
            {
                "q": "What is cohesion?",
                "options": ["How many modules exist", "How closely the parts inside one module belong together", "How fast the module runs", "How many lines it has"],
                "answer": 1,
                "why": "High cohesion means the module does one coherent job and does it completely.",
            },
            {
                "q": "What is stepwise refinement?",
                "options": ["Adding detail to a design a level at a time", "Rewriting the whole program", "Removing unused code", "Compiling in stages"],
                "answer": 0,
                "why": "Each pass adds a layer of detail until the design can be implemented directly.",
            },
        ],
        "examTip": "Define abstraction, modularity, coupling and cohesion, and give the four parts of the design model.",
    },

    "CSCA511-MII-T02": {
        "explanation": "Architectural design defines the overall structure of the software: the components and how they relate. It matters because it fixes the early decisions that are expensive to change later, and it lets everyone discuss the system. Common styles include layered architecture, where services are stacked, and client server, where requesters are separated from providers. Model View Controller splits a system into the data, the display and the control logic so each can change alone. Other styles are pipe and filter, where data passes through a chain of transformations, and the repository style, where components share stored data. Microservices go further, with independent services on defined interfaces.",
        "example": "A banking app keeps its account data in a model, shows it in several views, and routes every user action through a controller.",
        "quiz": [
            {
                "q": "What does MVC separate?",
                "options": ["Client and server", "The model, the view and the controller", "The database and the network", "Compiling and running"],
                "answer": 1,
                "why": "Data, presentation and control can then be changed without affecting the other two.",
            },
            {
                "q": "Which architecture style stacks services in levels?",
                "options": ["Pipe and filter", "Layered architecture", "Repository", "Microservices"],
                "answer": 1,
                "why": "Each layer offers services to the one above and uses the one below.",
            },
            {
                "q": "Which statement about architecture is NOT correct?",
                "options": ["It supports communication among stakeholders", "It is cheap and easy to change late in the project", "It enables reuse", "It allows early risk analysis"],
                "answer": 1,
                "why": "Architecture fixes the early decisions, which is why mistakes there are expensive.",
            },
            {
                "q": "In the pipe and filter style, what does a filter do?",
                "options": ["Deletes records", "Transforms the data passing through it", "Stores the data", "Draws the interface"],
                "answer": 1,
                "why": "Each filter takes input from a pipe, changes it and sends it on.",
            },
            {
                "q": "What is the main benefit of microservices?",
                "options": ["A single codebase", "Independent deployment and scaling of each service", "No need for interfaces", "Fewer servers"],
                "answer": 1,
                "why": "Teams can release and scale one service without touching the others.",
            },
        ],
        "examTip": "List four architectural styles with a one line description, and say why architecture matters.",
    },

    "CSCA511-MII-T03": {
        "explanation": "Component level design describes each part of the system closely enough for someone to implement it. A component is a modular, deployable and replaceable part with well defined interfaces. The open-closed principle says a component is open for extension but closed for modification. Dependency inversion says depend on abstractions rather than on details. Cohesion is graded from functional, the best, down to coincidental, the worst. Coupling is graded from content coupling, the worst, through common, control and stamp, to data coupling, which is acceptable. Good interfaces are simple and documented, so other teams and tests can use them.",
        "example": "A payment component that takes an amount and returns a receipt can be swapped for another provider. The rest of the system never notices the change.",
        "quiz": [
            {
                "q": "What does the open-closed principle say?",
                "options": ["Open for modification, closed for extension", "Open for extension, closed for modification", "Open source only", "Closed to all change"],
                "answer": 1,
                "why": "New behaviour is added by extension, so working code is not edited and broken.",
            },
            {
                "q": "Which is the weakest form of cohesion?",
                "options": ["Functional", "Sequential", "Communicational", "Coincidental"],
                "answer": 3,
                "why": "Coincidental cohesion means the parts have no meaningful relationship at all.",
            },
            {
                "q": "Which statement about components is NOT correct?",
                "options": ["A component is deployable and replaceable", "Interfaces should be simple and documented", "Data coupling is the most acceptable form", "Content coupling is the preferred form"],
                "answer": 3,
                "why": "Content coupling, where one module reaches into another's internals, is the worst kind.",
            },
            {
                "q": "What does dependency inversion recommend?",
                "options": ["Depend on abstractions rather than details", "Depend on the database directly", "Depend on the user interface", "Avoid all dependencies"],
                "answer": 0,
                "why": "Depending on abstractions lets the details be replaced without changing the caller.",
            },
            {
                "q": "Which principle says a client should not depend on methods it does not use?",
                "options": ["Open-closed", "Interface segregation", "Single responsibility", "Liskov substitution"],
                "answer": 1,
                "why": "Interface segregation splits a fat interface into the narrow ones each client needs.",
            },
        ],
        "examTip": "Define a component, state the open-closed and dependency inversion principles, and rank the coupling types.",
    },

    "CSCA511-MII-T04": {
        "explanation": "User interface design creates screens that let people work with the system effectively. Three golden rules guide it: keep the user in control, reduce the load on their memory, and make the interface consistent. Usability is judged on learnability, efficiency, error handling, memorability and satisfaction. The design process studies the users, their tasks and their environment first, then builds and evaluates a prototype with real users. Recurring issues are response time, help facilities, error messages, menu design, labelling and accessibility. Evaluation uses heuristic evaluation, usability testing, questionnaires such as QUIS and think aloud protocols.",
        "example": "An error message that says something went wrong tells the user nothing. One that says enter the date as DD/MM/YYYY tells them what to do.",
        "quiz": [
            {
                "q": "Which is one of the three golden rules of interface design?",
                "options": ["Use as many colours as possible", "Place the user in control", "Hide the system state", "Require training"],
                "answer": 1,
                "why": "Users need to feel they are driving, with the ability to undo and to interrupt.",
            },
            {
                "q": "Which quality measures how easily a new user learns the interface?",
                "options": ["Efficiency", "Learnability", "Memorability", "Satisfaction"],
                "answer": 1,
                "why": "Learnability is about the first encounter, while memorability is about returning after a gap.",
            },
            {
                "q": "Which statement about interface design is NOT correct?",
                "options": ["Consistency helps users predict behaviour", "Reducing memory load helps users", "Error messages should be vague to avoid blame", "Accessibility must be considered"],
                "answer": 2,
                "why": "Error messages must say what happened and what the user should do next.",
            },
            {
                "q": "What is heuristic evaluation?",
                "options": ["Timing the user", "Experts judge the interface against known usability rules", "Counting the colours", "Asking the developers"],
                "answer": 1,
                "why": "A small group of evaluators checks the design against established heuristics.",
            },
            {
                "q": "What is the think aloud protocol?",
                "options": ["Users read the manual aloud", "Users say what they are thinking while doing a task", "The developer explains the code", "The tester reads the test plan"],
                "answer": 1,
                "why": "Hearing the user's reasoning shows exactly where the interface misleads them.",
            },
        ],
        "examTip": "State the three golden rules, five usability qualities and two evaluation methods.",
    },

    "CSCA511-MII-T05": {
        "explanation": "A web application has to be designed on five fronts at once: content, aesthetics, architecture, navigation and interface. Its quality attributes include security, availability, scalability, maintainability, time to market and usability. Aesthetic design covers layout, colour, typography and graphics, and it should produce a clear visual hierarchy. Content design organises text, images, audio and video into content objects and shows how they relate. Architecture and navigation design decide how the pages are built and how people move between them, using menus, links, sitemaps and breadcrumbs. The interface layer adds consistent templates, responsive layout, usable forms and clear error handling.",
        "example": "Breadcrumbs on a shopping site show the path back to the category. Without them, a user who lands deep in a catalogue has to start again.",
        "quiz": [
            {
                "q": "Which of these is a web application quality attribute?",
                "options": ["Number of colours used", "Scalability", "Font size", "Page count"],
                "answer": 1,
                "why": "Scalability decides whether the application still responds when traffic grows.",
            },
            {
                "q": "What is the purpose of breadcrumbs?",
                "options": ["To decorate the page", "To show where the user is and give a path back", "To speed up loading", "To store cookies"],
                "answer": 1,
                "why": "They make the location visible within the site hierarchy, which supports navigation.",
            },
            {
                "q": "Which statement about web design is NOT correct?",
                "options": ["Content, aesthetics and navigation are designed together", "Visual hierarchy guides the eye", "Responsive design adapts to screen size", "Security is handled only after launch"],
                "answer": 3,
                "why": "Security is a design-time quality attribute, not an afterthought.",
            },
            {
                "q": "What does content design produce?",
                "options": ["The colour palette", "Content objects and the relationships between them", "The server configuration", "The navigation menu only"],
                "answer": 1,
                "why": "Modelling content as objects makes it reusable across pages and devices.",
            },
            {
                "q": "Which is an interface design concern for the web?",
                "options": ["Choosing a hosting provider", "Designing usable forms and clear error handling", "Buying a domain", "Writing the server log"],
                "answer": 1,
                "why": "Forms and error messages are where most users either succeed or give up.",
            },
        ],
        "examTip": "Name the five design dimensions of a web app and four quality attributes.",
    },
}
