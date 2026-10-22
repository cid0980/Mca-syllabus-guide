# CSCA 511 Software Engineering - Modules III and IV
# Quality management, testing, configuration management, metrics and project management.

CODE = "CSCA511"

CARDS = {
    "CSCA511-MIII-T01": {
        "explanation": "Reviews find defects early by having other people examine a work product against agreed criteria. The cheapest kind is the desk check, where the author reads their own work before anyone else sees it. Informal reviews are quick peer looks, while a walkthrough is led by the author, who presents the work and collects comments. An inspection is more rigorous: a trained moderator leads it, reviewers prepare in advance, and defects are recorded and counted. A formal technical review assigns roles of producer, reviewer, recorder and moderator and works from a checklist. Useful metrics come out of it: defect density, preparation time, rework time and review rate.",
        "example": "Finding a wrong formula in the design document costs an hour. Finding the same error after release costs a patch and a customer call.",
        "quiz": [
            {
                "q": "Who leads an inspection?",
                "options": ["The author", "A trained moderator", "The project manager", "The customer"],
                "answer": 1,
                "why": "The moderator is not the author, which keeps the review independent and measured.",
            },
            {
                "q": "What is a desk check?",
                "options": ["A review by the quality department", "The author examining their own work before review", "A hardware test", "A budget audit"],
                "answer": 1,
                "why": "It is the cheapest filter, and it removes obvious errors before others spend time on them.",
            },
            {
                "q": "Which statement about reviews is NOT correct?",
                "options": ["Walkthroughs are led by the author", "Inspections record and count defects", "Reviews find defects earlier than testing", "Reviews should examine unfinished work to save time"],
                "answer": 3,
                "why": "Reviewing unfinished work wastes everyone's time, which is a standard review guideline.",
            },
            {
                "q": "What does defect density measure?",
                "options": ["Defects per unit of product size", "The time spent in review", "The number of reviewers", "The cost of the project"],
                "answer": 0,
                "why": "Defects per thousand lines or per page lets two products be compared fairly.",
            },
            {
                "q": "Which review type is the most formal and measured?",
                "options": ["Desk check", "Informal review", "Walkthrough", "Inspection"],
                "answer": 3,
                "why": "Inspections have defined roles, preparation, checklists and recorded defect data.",
            },
        ],
        "examTip": "Compare desk check, walkthrough and inspection, name the four FTR roles and three review metrics.",
    },

    "CSCA511-MIII-T02": {
        "explanation": "Software quality assurance is the set of planned activities that give confidence the product meets its quality requirements. Quality has two faces: design and conformance. Quality of design is what the specification asks for, and conformance is how faithfully the product meets it. SQA work includes standards, reviews, audits, a test strategy, defect tracking and measurement, all written into an SQA plan. Standards come from bodies such as ISO and IEEE: ISO 9001 covers quality management systems and ISO 25010 describes product quality. Process maturity is graded by CMMI across five levels, from initial to optimising. Six Sigma is a related improvement programme built on the DMAIC cycle.",
        "example": "Two products can both work. The one that meets its specification exactly shows better quality of conformance.",
        "quiz": [
            {
                "q": "What is the difference between quality of design and quality of conformance?",
                "options": ["They are the same thing", "Design is what is specified, conformance is how faithfully it is met", "Conformance is about the user interface", "Design is about testing"],
                "answer": 1,
                "why": "A product can be well made and still be the wrong product, or right but badly made.",
            },
            {
                "q": "What does ISO 9001 cover?",
                "options": ["Programming languages", "Quality management systems", "Network protocols", "Database design"],
                "answer": 1,
                "why": "It certifies the management system behind the work, not the product itself.",
            },
            {
                "q": "Which statement about SQA is NOT correct?",
                "options": ["An SQA plan defines the activities", "Reviews and audits are SQA activities", "CMMI has five maturity levels", "Six Sigma uses the PDCA cycle"],
                "answer": 3,
                "why": "Six Sigma uses DMAIC: define, measure, analyse, improve and control.",
            },
            {
                "q": "What is the highest CMMI maturity level?",
                "options": ["Initial", "Managed", "Defined", "Optimising"],
                "answer": 3,
                "why": "At level five the organisation improves its own process using measured data.",
            },
            {
                "q": "What makes up the cost of quality?",
                "options": ["The price of the software", "Prevention, appraisal and failure costs together", "The salary of the testers", "The licence fee of the tools"],
                "answer": 1,
                "why": "Spending on prevention usually lowers the far larger failure costs.",
            },
        ],
        "examTip": "Define SQA, distinguish the two kinds of quality, and name two standards and one maturity model.",
    },

    "CSCA511-MIII-T03": {
        "explanation": "A testing strategy organises the levels of testing, from single units up to the whole system. Two questions drive it: verification asks whether the product was built right, and validation asks whether the right product was built. Unit testing checks one module in isolation, and integration testing then joins them, top down, bottom up, sandwich or all at once. System testing checks the product against its requirements, and alpha and beta testing put it in front of real users. White box testing uses the internal structure, while black box testing uses only inputs and outputs. Equivalence partitioning and boundary value analysis are the black box techniques used most often.",
        "example": "For a field that accepts ages 18 to 60, boundary value analysis tests 17, 18, 60 and 61 rather than every number.",
        "quiz": [
            {
                "q": "What is the difference between verification and validation?",
                "options": ["They are identical", "Verification checks the product was built right, validation checks the right product was built", "Validation happens only in testing", "Verification happens only at release"],
                "answer": 1,
                "why": "Reviews and unit tests verify, while user acceptance work validates.",
            },
            {
                "q": "Which integration approach needs stubs?",
                "options": ["Bottom up", "Top down", "Big bang", "Regression"],
                "answer": 1,
                "why": "Top down integration calls lower modules that are not ready, so stubs stand in for them.",
            },
            {
                "q": "Which statement about testing is NOT correct?",
                "options": ["Unit testing checks a module in isolation", "Alpha testing happens at the developer's site", "Regression testing checks that changes broke nothing", "Smoke testing is a full test of every function"],
                "answer": 3,
                "why": "A smoke test is a shallow check that the build is stable enough to test properly.",
            },
            {
                "q": "Which technique tests values at the edges of a range?",
                "options": ["Equivalence partitioning", "Boundary value analysis", "Basis path testing", "Condition testing"],
                "answer": 1,
                "why": "Errors collect at the edges of ranges, so 17, 18, 60 and 61 catch most of them.",
            },
            {
                "q": "Which of these is a white box technique?",
                "options": ["Equivalence partitioning", "Boundary value analysis", "Basis path testing", "Beta testing"],
                "answer": 2,
                "why": "Basis path testing uses the control flow graph of the code to design the tests.",
            },
        ],
        "examTip": "Define verification and validation, list four integration approaches, and give two black box and two white box techniques.",
    },

    "CSCA511-MIII-T04": {
        "explanation": "Software configuration management controls changes to every work product for the whole life of the project. A configuration item is any product or document placed under control, and a baseline is a reviewed, approved state of one. Version control records every change through a repository, with check in, check out, branching and merging. Change control then decides what gets in. A change request is assessed for impact and cost, and a change control board approves or rejects it. Release management builds, packages and ships consistent versions, with release notes and a way to roll back. Good configuration management gives identification, control, status accounting and audit.",
        "example": "A team keeps release 2.1 as a tagged baseline. When a bug appears in the field, they can rebuild exactly that version.",
        "quiz": [
            {
                "q": "What is a baseline?",
                "options": ["The project plan", "A reviewed and approved state of a work product", "The first draft of code", "The final release"],
                "answer": 1,
                "why": "Once baselined, any change must go through change control rather than being made freely.",
            },
            {
                "q": "What does a change control board do?",
                "options": ["Writes the code", "Approves or rejects change requests after assessing impact", "Tests the release", "Hires the team"],
                "answer": 1,
                "why": "It weighs the cost and risk of the change against the benefit before deciding.",
            },
            {
                "q": "Which statement about configuration management is NOT correct?",
                "options": ["Version control tracks every change", "Branching lets two lines of work proceed together", "A baseline changes freely at any time", "Status accounting records the state of configuration items"],
                "answer": 2,
                "why": "A baseline is fixed on purpose, and changing it requires formal approval.",
            },
            {
                "q": "What is the purpose of a rollback plan?",
                "options": ["To delete old code", "To restore the previous version if a release fails", "To undo a merge", "To close the repository"],
                "answer": 1,
                "why": "If a release misbehaves, the fastest safe action is to return to the known good version.",
            },
            {
                "q": "Which activity confirms that a baseline contains what it should?",
                "options": ["Version control", "Configuration audit", "Change control", "Release management"],
                "answer": 1,
                "why": "The audit compares the documented configuration with what is actually in the baseline.",
            },
        ],
        "examTip": "Define configuration item and baseline, and list the four SCM activities with one line each.",
    },

    "CSCA511-MIII-T05": {
        "explanation": "Product metrics measure the software itself rather than the way it was built. A measure is a raw value, and a metric relates two or more measures. An indicator is a metric used to take a decision. Size is counted in lines of code or in function points. Function points are built from inputs, outputs, enquiries, files and interfaces with complexity weights. Cyclomatic complexity counts the decision points in a module and gives the number of independent paths that tests must cover. Halstead metrics use the counts of operators and operands to estimate length and difficulty. Quality is then tracked with defect density, mean time between failures and maintainability indices.",
        "example": "A function with six if statements has cyclomatic complexity seven, so at least seven test paths are needed to cover it.",
        "quiz": [
            {
                "q": "What is the difference between a measure and a metric?",
                "options": ["They are identical", "A measure is a raw value, a metric relates measures", "A metric is always larger", "A measure is always a percentage"],
                "answer": 1,
                "why": "Lines of code is a measure, and defects per thousand lines is a metric.",
            },
            {
                "q": "What does cyclomatic complexity indicate?",
                "options": ["The number of lines", "The number of independent paths that tests should cover", "The number of developers", "The cost of the project"],
                "answer": 1,
                "why": "Each decision point adds a path, so complexity and required testing rise together.",
            },
            {
                "q": "Which statement about function points is NOT correct?",
                "options": ["They count inputs, outputs and enquiries", "They use complexity weights", "They depend on the programming language used", "They are an indirect measure of size"],
                "answer": 2,
                "why": "Function points are language independent, unlike lines of code, which is their main advantage.",
            },
            {
                "q": "Which of these is an object oriented metric?",
                "options": ["Cyclomatic complexity", "Depth of inheritance tree", "Boundary value analysis", "Defect density"],
                "answer": 1,
                "why": "It counts how deep a class sits in the inheritance hierarchy, and deep trees raise complexity.",
            },
            {
                "q": "What does defect density measure?",
                "options": ["Defects per unit of product size", "The time taken to fix a defect", "The number of testers", "The severity of a defect"],
                "answer": 0,
                "why": "Normalising by size lets teams compare quality across components of different sizes.",
            },
        ],
        "examTip": "Define measure, metric and indicator, give the function point components, and state what cyclomatic complexity means.",
    },

    "CSCA511-MIV-T01": {
        "explanation": "Software project management plans, organises and controls the people, the process and the product. It is often summarised as the four Ps: people, product, process and project, with people the most important of them. Stakeholders must be identified early: the users, the customers, the developers and the management who fund the work. Team structures vary too, from a closed team with a clear hierarchy to an open or random team that suits research work. The W5HH principle gives a compact plan outline: why, what, when, who, where, how and how much. Most failures trace back to the same causes: unrealistic deadlines, changing requirements, weak estimation and poor communication.",
        "example": "A manager who can answer why, what, when, who, where, how and how much has a plan others can follow.",
        "quiz": [
            {
                "q": "Which of the four Ps is considered the most important?",
                "options": ["Product", "Process", "Project", "People"],
                "answer": 3,
                "why": "Skilled, motivated people are what make the other three work at all.",
            },
            {
                "q": "What does the W5HH principle provide?",
                "options": ["A testing method", "A compact outline of a project plan", "A coding standard", "A hiring process"],
                "answer": 1,
                "why": "Answering why, what, when, who, where, how and how much leaves little unplanned.",
            },
            {
                "q": "Which statement about project management is NOT correct?",
                "options": ["Stakeholders include users and customers", "A closed team has a clear hierarchy", "Unrealistic deadlines cause project failure", "Changing requirements have no effect on a project"],
                "answer": 3,
                "why": "Changing requirements is one of the four standard causes of software project failure.",
            },
            {
                "q": "Which team structure suits research style work?",
                "options": ["Closed", "Random", "Chief programmer", "Hierarchical"],
                "answer": 1,
                "why": "A random team relies on individual initiative and works well when the problem is open ended.",
            },
            {
                "q": "In the chief programmer team, what does the backup programmer do?",
                "options": ["Tests the code", "Supports the chief programmer and can take over", "Writes the documentation", "Manages the budget"],
                "answer": 1,
                "why": "The backup programmer is second in command, ready to replace the chief if needed.",
            },
        ],
        "examTip": "Name the four Ps, list four stakeholders, write out W5HH and give three causes of project failure.",
    },

    "CSCA511-MIV-T02": {
        "explanation": "Process metrics describe how well the development process works, while project metrics track one project at a time. Both rest on the same chain: raw measures become metrics, and metrics that guide a decision are called indicators. Direct measures are counted straight from the work, such as lines of code, cost and elapsed time. Indirect measures are derived, such as functionality, quality and complexity, and they are usually more useful to managers. Process metrics are averaged across many projects, so private individual data must be aggregated carefully and never used to judge a person. Quality metrics before delivery cover correctness, maintainability, integrity and usability.",
        "example": "Counting each developer's defects sounds useful. Used to compare people, it stops them reporting defects at all.",
        "quiz": [
            {
                "q": "What is an indicator?",
                "options": ["A raw count", "A metric used to take a decision", "A test result", "A project plan"],
                "answer": 1,
                "why": "The chain runs measure to metric to indicator, and only the last informs action.",
            },
            {
                "q": "Which is an indirect measure?",
                "options": ["Lines of code", "Cost", "Elapsed time", "Complexity"],
                "answer": 3,
                "why": "Complexity is derived from other counts rather than measured directly.",
            },
            {
                "q": "Which statement about metrics is NOT correct?",
                "options": ["Direct measures include cost and time", "Indirect measures include quality", "Individual metrics should never be used to judge people", "Process metrics describe a single project only"],
                "answer": 3,
                "why": "Process metrics are computed across many projects, while project metrics track one.",
            },
            {
                "q": "Which quality metric is measured before delivery?",
                "options": ["Mean time between failures", "Correctness", "Number of users", "Server cost"],
                "answer": 1,
                "why": "Correctness, maintainability, integrity and usability are the four pre-delivery quality metrics.",
            },
            {
                "q": "Why must private individual data be aggregated carefully?",
                "options": ["It takes too long to collect", "Misuse makes people game the numbers and destroys trust", "It is illegal to store", "It is always wrong"],
                "answer": 1,
                "why": "Metrics used against individuals stop being measurements and become targets.",
            },
        ],
        "examTip": "Define measure, metric and indicator, give two direct and two indirect measures, and name the four quality metrics.",
    },

    "CSCA511-MIV-T03": {
        "explanation": "Estimation predicts the effort, cost and duration a project will need. Common techniques include expert judgement, estimation by analogy and the Delphi method. Two techniques to avoid are Parkinson's law and price to win. Size based estimation starts from lines of code and converts them to effort using historical productivity, but the answer depends on the language. Function point estimation counts unadjusted function points, adjusts for complexity and converts to code using a language factor. Use case point estimation weights actors and use cases and adjusts for technical and environmental factors. COCOMO estimates effort from size across organic, semi-detached and embedded modes with cost driver multipliers.",
        "example": "Estimating a house by its floor area and a local rate per square foot is analogous to function point estimation.",
        "quiz": [
            {
                "q": "What is the Delphi method of estimation?",
                "options": ["One expert decides", "Experts estimate in rounds and converge towards agreement", "The manager sets the number", "The customer chooses the cost"],
                "answer": 1,
                "why": "Each round feeds back a summary, which narrows the spread without group pressure.",
            },
            {
                "q": "What is price to win estimation?",
                "options": ["The cheapest possible estimate", "Estimating what it takes to win the contract, not what the work costs", "The market price", "The cost plus profit"],
                "answer": 1,
                "why": "It is a technique to avoid, because the number is set by the bid rather than the work.",
            },
            {
                "q": "Which statement about estimation is NOT correct?",
                "options": ["Function points allow for complexity", "Lines of code estimation depends on the language", "COCOMO has organic, semi-detached and embedded modes", "Estimation is exact once the project has started"],
                "answer": 3,
                "why": "Estimates are refined as the project proceeds, so ranges and confidence limits are used.",
            },
            {
                "q": "What does a function point count?",
                "options": ["Lines of code", "Inputs, outputs, enquiries, files and interfaces", "Number of developers", "Number of test cases"],
                "answer": 1,
                "why": "These five components are weighted by complexity to give the unadjusted count.",
            },
            {
                "q": "What is the main weakness of lines of code based estimation?",
                "options": ["It takes too long", "The same function gives different counts in different languages", "It needs a computer", "It cannot be measured"],
                "answer": 1,
                "why": "A line is not a fixed unit of work, so the estimate depends on the language chosen.",
            },
        ],
        "examTip": "Name three estimation techniques, describe function point estimation, and name the three COCOMO modes.",
    },

    "CSCA511-MIV-T04": {
        "explanation": "Scheduling allocates work to people over time and shows how the tasks depend on one another. It begins with a work breakdown structure, which breaks the total work into tasks small enough to estimate and assign. Tasks are then linked in a task network by finish to start, start to start and finish to finish relationships. A Gantt chart shows the same plan against a calendar, making overlap and progress easy to see. The critical path is the longest chain of dependent tasks, and it fixes the earliest finish date for the whole project. PERT uses optimistic, likely and pessimistic estimates, and earned value analysis tracks schedule and cost together.",
        "example": "If testing cannot start until coding finishes, and coding cannot start until design finishes, that chain sets the shortest possible duration.",
        "quiz": [
            {
                "q": "What is the critical path?",
                "options": ["The shortest route through the plan", "The longest chain of dependent tasks, which fixes project duration", "The most expensive task", "The first task in the plan"],
                "answer": 1,
                "why": "Any delay on the critical path delays the whole project, which is why it is watched closely.",
            },
            {
                "q": "What is slack or float?",
                "options": ["The budget reserve", "Spare time in a non critical task", "The number of workers", "The project end date"],
                "answer": 1,
                "why": "A task with slack can slip by that much without moving the finish date.",
            },
            {
                "q": "Which statement about scheduling is NOT correct?",
                "options": ["A work breakdown structure decomposes the work", "A Gantt chart shows tasks against a calendar", "PERT uses three time estimates", "Finish to start means both tasks finish together"],
                "answer": 3,
                "why": "Finish to start means the second task cannot start until the first has finished.",
            },
            {
                "q": "What does PERT stand for?",
                "options": ["Program evaluation and review technique", "Project effort and resource tracking", "Planned evaluation of real time", "Program error reporting tool"],
                "answer": 0,
                "why": "It uses three estimates per task and works out an expected duration from them.",
            },
            {
                "q": "What is time boxing in agile scheduling?",
                "options": ["Working overtime near a deadline", "Fixing the iteration length and letting the scope adjust", "Extending the deadline", "Measuring the team's time"],
                "answer": 1,
                "why": "The date is fixed and the scope flexes, which is the opposite of the traditional approach.",
            },
        ],
        "examTip": "Define work breakdown structure, critical path and slack, and explain PERT and earned value analysis.",
    },

    "CSCA511-MIV-T05": {
        "explanation": "Risk management identifies what could go wrong and decides in advance what to do about it. Risks fall into project risks, technical risks and business risks, and some are predictable while others are unknown. Identification uses brainstorming, checklists and the record of past projects, and the results go into a risk table. Each row lists the risk, its probability, its impact and the risk factor that combines them. Risk projection then estimates the exposure, the expected loss if the risk occurs. Risk mitigation, monitoring and management, shortened to RMMM, plans how to reduce each significant risk and how to watch it. Exposure is highest early, so risky parts are built first.",
        "example": "A team unsure whether a new library can handle the load builds a small test with it in week one rather than week ten.",
        "quiz": [
            {
                "q": "What is risk exposure?",
                "options": ["The number of risks", "The expected loss, combining probability and impact", "The project budget", "The time spent in risk meetings"],
                "answer": 1,
                "why": "A likely risk with small impact and a rare one with huge impact can have equal exposure.",
            },
            {
                "q": "What does RMMM stand for?",
                "options": ["Risk measurement, modelling and management", "Risk mitigation, monitoring and management", "Resource, method and money management", "Review, modify, measure, maintain"],
                "answer": 1,
                "why": "It is the plan for what to do about each significant risk, not only the list of risks.",
            },
            {
                "q": "Which statement about risk is NOT correct?",
                "options": ["Brainstorming helps identify risks", "A risk table lists probability and impact", "Risk exposure is highest early in the project", "Unknown risks can be fully planned for in advance"],
                "answer": 3,
                "why": "Unknown risks cannot be planned in detail, which is why contingency reserves exist.",
            },
            {
                "q": "Why are risky components often built first?",
                "options": ["They are the easiest", "To discover early whether the approach works at all", "Because the team prefers them", "To use up the budget"],
                "answer": 1,
                "why": "Failing early is cheap, while failing late can sink the schedule.",
            },
            {
                "q": "Which category covers the risk that the chosen technology will not perform?",
                "options": ["Project risk", "Technical risk", "Business risk", "Legal risk"],
                "answer": 1,
                "why": "Technical risks concern design, implementation, interfaces and performance.",
            },
        ],
        "examTip": "Define risk, list the three categories, describe the risk table and explain RMMM.",
    },
}
