# CSCA 511 Software Engineering - Module V
# Reliability engineering, reliability testing and secure engineering.

CODE = "CSCA511"

CARDS = {
    "CSCA511-MV-T01": {
        "explanation": "Reliability is the probability that software runs without failure for a stated time in a stated environment. Availability is different: it is the fraction of time the system is usable, and it equals MTTF divided by MTTF plus MTTR. Three terms must be kept apart. A fault is a defect in the code. An error is a wrong internal state. A failure is the wrong behaviour a user sees. Hardware and software fail differently. Hardware wears out with age, while software does not wear out at all but degrades each time it is changed. Reliability growth models describe the other direction: as defects are found and removed, failure intensity falls.",
        "example": "A payment gateway that is up 99.9 percent of the time is down for about 43 minutes a month.",
        "quiz": [
            {
                "q": "How is availability calculated from MTTF and MTTR?",
                "options": ["MTTF plus MTTR", "MTTF divided by MTTF plus MTTR", "MTTR divided by MTTF", "MTTF multiplied by MTTR"],
                "answer": 1,
                "why": "The fraction of total time the system is running gives the availability figure.",
            },
            {
                "q": "What is the difference between a fault and a failure?",
                "options": ["They are identical", "A fault is a defect in the code, a failure is the wrong behaviour observed", "A failure is always worse than a fault", "A fault is found by users"],
                "answer": 1,
                "why": "A fault that is never executed stays a fault and never becomes a failure.",
            },
            {
                "q": "Which statement about reliability is NOT correct?",
                "options": ["Software does not wear out with age", "Software reliability can degrade when the code is changed", "Hardware reliability falls with age because of wear", "Reliability and availability mean the same thing"],
                "answer": 3,
                "why": "Availability includes repair time, so a system can be unreliable yet highly available.",
            },
            {
                "q": "What does MTTR measure?",
                "options": ["Mean time to failure", "Mean time to repair", "Mean time between releases", "Mean time to release"],
                "answer": 1,
                "why": "It is the average time needed to restore service after a failure occurs.",
            },
            {
                "q": "What does a reliability growth model show?",
                "options": ["Errors growing over time", "Failure intensity falling as defects are found and removed", "Cost rising over time", "Staff numbers growing over time"],
                "answer": 1,
                "why": "The curve is measured during testing and used to predict when a target will be reached.",
            },
        ],
        "examTip": "Define reliability and availability, distinguish fault, error and failure, and give the availability formula.",
    },

    "CSCA511-MV-T02": {
        "explanation": "Reliability testing measures failure intensity and shows whether reliability is improving. Failure intensity counts failures per unit of time or per transaction. A specification fixes a target, such as failures per thousand hours. Common metrics are probability of failure on demand, rate of occurrence of failures and mean time to failure. Statistical testing draws its test cases from an operational profile, which describes how the software is really used. That matters, because a rare path tested as often as a common one gives a misleading answer. Fault injection adds known defects on purpose to see how many the tests catch. Improvement then runs in cycles: measure, fix the worst faults, and measure again.",
        "example": "If 80 percent of users place an order and 2 percent refund one, the test suite should spend most of its effort on placing orders.",
        "quiz": [
            {
                "q": "What is an operational profile?",
                "options": ["A list of developers", "A description of how the software is used, which drives test selection", "The system architecture", "The test schedule"],
                "answer": 1,
                "why": "Testing in proportion to real usage makes the reliability figure meaningful.",
            },
            {
                "q": "What is probability of failure on demand?",
                "options": ["The chance that a request fails when it is made", "The number of users", "The uptime percentage", "The repair time"],
                "answer": 0,
                "why": "It suits systems that act on requests rather than running continuously.",
            },
            {
                "q": "Which statement about reliability testing is NOT correct?",
                "options": ["It measures failure intensity", "Test cases should follow real usage", "Fault injection checks how many faults the tests detect", "Testing every path equally gives the best reliability estimate"],
                "answer": 3,
                "why": "Equal effort on every path overstates rare paths and skews the result.",
            },
            {
                "q": "What is fault injection?",
                "options": ["Introducing known defects to check whether the tests find them", "Removing all bugs", "Adding users to the system", "Deleting test cases"],
                "answer": 0,
                "why": "The proportion of injected faults that are caught measures the strength of the test set.",
            },
            {
                "q": "How does reliability improvement proceed?",
                "options": ["One large final test", "Cycles of measuring, fixing the worst faults and measuring again", "By adding more servers", "By rewriting the requirements"],
                "answer": 1,
                "why": "Each cycle removes the most damaging faults first, which raises reliability fastest.",
            },
        ],
        "examTip": "Define failure intensity, name three reliability metrics, and explain operational profiles and fault injection.",
    },

    "CSCA511-MV-T03": {
        "explanation": "Secure engineering builds security in at the requirements and design stage rather than bolting it on later. Requirements fall into categories: confidentiality, integrity, availability, authentication, authorisation, non-repudiation and auditing. Elicitation starts by listing the assets, the threats, the attackers and the attack surfaces, and misuse cases record what must be defended against. STRIDE is a useful checklist: spoofing, tampering, repudiation, information disclosure, denial of service and elevation of privilege, often worked through with attack trees. Design then applies principles such as least privilege, fail safe defaults, defence in depth and complete mediation. Testing finishes the job with static analysis, penetration testing, fuzzing and secure code review.",
        "example": "A password reset page that reveals whether an account exists is an information disclosure problem, the I in STRIDE.",
        "quiz": [
            {
                "q": "What does the S in STRIDE stand for?",
                "options": ["Security", "Spoofing", "Storage", "Session"],
                "answer": 1,
                "why": "Spoofing means pretending to be another user or system, which authentication defends against.",
            },
            {
                "q": "What is a misuse case?",
                "options": ["A wrongly written use case", "A scenario showing how an attacker might abuse the system", "A test that fails", "A bug report"],
                "answer": 1,
                "why": "Writing attacks as scenarios forces the team to design a defence for each one.",
            },
            {
                "q": "Which statement about secure design is NOT correct?",
                "options": ["Least privilege gives each part the minimum access it needs", "Fail safe defaults deny access when something goes wrong", "Defence in depth uses several layers of control", "Security testing can wait until after release"],
                "answer": 3,
                "why": "Static analysis, penetration testing and code review all run before release.",
            },
            {
                "q": "What does non-repudiation provide?",
                "options": ["Faster logins", "Proof that a party cannot deny having performed an action", "Data encryption at rest", "Backup of the database"],
                "answer": 1,
                "why": "Digital signatures and audit logs are the usual mechanisms behind it.",
            },
            {
                "q": "What does complete mediation require?",
                "options": ["Checking every access request, every time", "Checking access only at login", "Checking access once a day", "Checking access only for administrators"],
                "answer": 0,
                "why": "Caching an authorisation decision can leave a revoked user still able to act.",
            },
        ],
        "examTip": "List the seven security requirement categories, expand STRIDE, and give four secure design principles.",
    },
}
