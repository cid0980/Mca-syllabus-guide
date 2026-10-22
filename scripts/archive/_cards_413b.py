# CSCA 413 Database Management Systems - Module III
# Transaction processing, concurrency control, recovery and security.

CODE = "CSCA413"

CARDS = {
    "CSCA413-MIII-T01": {
        "explanation": "A transaction is one logical unit of work, such as transferring money between two accounts. Its basic operations are read item and write item, and it ends with commit or rollback. Four properties are required: atomicity, consistency, isolation and durability, remembered as ACID. Atomicity means all or nothing, and consistency means the database still obeys its rules at the end. Isolation means a transaction never sees another's partial work, and durability means committed work survives a crash. A transaction moves through the states active, partially committed, committed, failed and aborted.",
        "example": "Transferring 500 rupees between two accounts needs a debit and a credit. If the power fails after the debit, atomicity rolls the half done work back so the money is not lost.",
        "quiz": [
            {
                "q": "Which ACID property says that a transaction is all or nothing?",
                "options": ["Atomicity", "Consistency", "Isolation", "Durability"],
                "answer": 0,
                "why": "Atomicity means every operation of the transaction happens, or none of them does.",
            },
            {
                "q": "Which ACID property guarantees that committed work survives a crash?",
                "options": ["Atomicity", "Consistency", "Isolation", "Durability"],
                "answer": 3,
                "why": "Durability is what keeps a committed transaction on stable storage after a failure.",
            },
            {
                "q": "A transaction has written its last statement but the system has not confirmed it yet. Which state is it in?",
                "options": ["Active", "Partially committed", "Aborted", "Failed"],
                "answer": 1,
                "why": "The partially committed state sits between the final write and the commit record.",
            },
            {
                "q": "Which statement about transactions is NOT correct?",
                "options": ["Read item and write item are the basic operations", "Rollback undoes the work of the current transaction", "Isolation lets a transaction read another's uncommitted changes", "A transaction moves the database from one consistent state to another"],
                "answer": 2,
                "why": "Isolation hides uncommitted work from other transactions; reading it is the dirty read problem.",
            },
            {
                "q": "Which pair of operations marks the two ways a transaction can end?",
                "options": ["Read item and write item", "Commit and rollback", "Checkpoint and shadow paging", "Shared lock and exclusive lock"],
                "answer": 1,
                "why": "Commit makes the changes permanent and rollback undoes them; the others are internal steps.",
            },
        ],
        "examTip": "Expand ACID one word at a time with a line each, then draw the five states with arrows into committed and aborted.",
    },

    "CSCA413-MIII-T02": {
        "explanation": "A schedule is the order in which the operations of several transactions actually run. A serial schedule runs one transaction to the end before starting the next, which is correct but slow, so systems interleave them instead. An interleaved schedule is conflict serializable when it can be swapped into some serial order by exchanging non conflicting operations. The test is the precedence graph: if it has no cycle, the schedule is conflict serializable. View serializability is a weaker test that compares who read what and who wrote the final value. A schedule is recoverable if a transaction commits only after every transaction it read from has committed.",
        "example": "T1 reads an account and T2 writes it, so T1 must come before T2 in the precedence graph. If T2 also reads something T1 writes, the graph has a cycle and the schedule is not serializable.",
        "quiz": [
            {
                "q": "What is a schedule called when transactions run one after another with no interleaving?",
                "options": ["Serial schedule", "Conflict schedule", "Strict schedule", "Recoverable schedule"],
                "answer": 0,
                "why": "A serial schedule runs each transaction to completion before the next begins, so it is always correct.",
            },
            {
                "q": "How is conflict serializability tested?",
                "options": ["By counting the reads and writes in the schedule", "By checking the precedence graph for a cycle", "By comparing the final values only", "By locking every item until commit"],
                "answer": 1,
                "why": "An acyclic precedence graph means the operations can be reordered into some serial schedule.",
            },
            {
                "q": "Which statement about serializability is NOT correct?",
                "options": ["Every conflict serializable schedule is also view serializable", "View serializability is the weaker of the two conditions", "A cyclic precedence graph rules out conflict serializability", "A serial schedule interleaves operations from several transactions"],
                "answer": 3,
                "why": "Interleaving is what a non serial schedule does; a serial schedule keeps the transactions apart.",
            },
            {
                "q": "T1 reads a value written by T2 and commits before T2 commits. Which property is missing?",
                "options": ["Conflict serializability", "View serializability", "Recoverability", "Atomicity"],
                "answer": 2,
                "why": "A recoverable schedule makes a transaction wait to commit until everything it read from has committed.",
            },
            {
                "q": "Which schedule avoids cascading rollback by forbidding reads of uncommitted writes?",
                "options": ["Recoverable schedule", "Cascadeless schedule", "Serial schedule", "View serializable schedule"],
                "answer": 1,
                "why": "A cascadeless schedule allows a read only after the transaction that wrote the value has committed.",
            },
        ],
        "examTip": "Draw the precedence graph for the given schedule, list the edges, then state the verdict from the cycle.",
    },

    "CSCA413-MIII-T03": {
        "explanation": "SQL lets a programmer control a transaction directly instead of leaving it to the system. COMMIT makes the changes permanent and ROLLBACK undoes them, taking the database back to where the transaction began. SAVEPOINT marks a point inside the transaction, so a rollback can return there and keep the earlier work. Four isolation levels trade correctness for concurrency: read uncommitted, read committed, repeatable read and serializable. The lower levels allow dirty reads, non repeatable reads and phantom rows, which the higher levels prevent at the cost of waiting.",
        "example": "A batch job inserts 500 rows and fails at row 480. A savepoint placed every 100 rows lets the job roll back to row 400 and carry on instead of losing everything.",
        "quiz": [
            {
                "q": "Which statement undoes the work of the current transaction?",
                "options": ["COMMIT", "ROLLBACK", "SAVEPOINT", "GRANT"],
                "answer": 1,
                "why": "ROLLBACK returns the database to the state before the transaction began; COMMIT makes the work permanent.",
            },
            {
                "q": "What is a SAVEPOINT used for?",
                "options": ["To commit part of the transaction permanently", "To mark a point that a rollback can return to", "To lock a table until commit", "To raise the isolation level"],
                "answer": 1,
                "why": "A rollback to a savepoint keeps the work done before the mark and discards only what came after it.",
            },
            {
                "q": "Which isolation level is the strictest?",
                "options": ["Read uncommitted", "Read committed", "Repeatable read", "Serializable"],
                "answer": 3,
                "why": "Serializable gives the effect of running transactions one at a time, which costs the most concurrency.",
            },
            {
                "q": "A transaction reads a row, and a second read in the same transaction returns a different value. What is this called?",
                "options": ["Dirty read", "Non repeatable read", "Phantom read", "Lost update"],
                "answer": 1,
                "why": "A non repeatable read happens when another transaction commits an update between the two reads.",
            },
            {
                "q": "Which statement about isolation levels is NOT correct?",
                "options": ["Read uncommitted allows a dirty read", "Repeatable read stops a value changing between two reads", "Serializable permits phantom rows to appear", "Higher levels reduce the amount of concurrency"],
                "answer": 2,
                "why": "Serializable is the level that prevents phantom rows; the lower levels are the ones that allow them.",
            },
        ],
        "examTip": "List the four levels in order and name the problem each one removes: dirty read, non repeatable read, phantom read.",
    },

    "CSCA413-MIII-T04": {
        "explanation": "Locking makes a transaction ask permission before it touches a data item. A shared lock allows many readers at once, while an exclusive lock gives one writer the item and blocks everyone else. Two phase locking is the rule that guarantees conflict serializability. It has a growing phase that takes locks and a shrinking phase that releases them, and no lock is taken after the first release. Strict two phase locking holds exclusive locks until commit, which keeps recovery simple. Two problems remain: deadlock, where transactions wait for each other in a circle, and starvation, where one transaction keeps losing the competition.",
        "example": "Two clerks edit the same row at once, and the first takes an exclusive lock so the second waits. If each then waits for the item the other holds, the system must abort one of them.",
        "quiz": [
            {
                "q": "Which lock allows many transactions to read the same item at once?",
                "options": ["Exclusive lock", "Shared lock", "Intention exclusive lock", "Binary lock"],
                "answer": 1,
                "why": "A shared lock is for reading, so several transactions may hold it together; an exclusive lock is for one writer.",
            },
            {
                "q": "What does two phase locking guarantee?",
                "options": ["Deadlock freedom", "Conflict serializability", "Recoverability on its own", "Freedom from starvation"],
                "answer": 1,
                "why": "Growing then shrinking, with no new lock after the first release, gives a serializable order.",
            },
            {
                "q": "Which statement about two phase locking is NOT correct?",
                "options": ["The growing phase only acquires locks", "The shrinking phase only releases locks", "Strict 2PL holds exclusive locks until commit", "Two phase locking can never produce a deadlock"],
                "answer": 3,
                "why": "Two phase locking guarantees serializability, not deadlock freedom; waiting for locks can still form a cycle.",
            },
            {
                "q": "T1 holds a lock on A and wants B, while T2 holds B and wants A. What has happened?",
                "options": ["Starvation", "Deadlock", "Lost update", "Phantom read"],
                "answer": 1,
                "why": "A circular wait for locks is a deadlock, and one of the transactions must be rolled back.",
            },
            {
                "q": "Upgrading a shared lock to an exclusive one is called:",
                "options": ["Lock conversion", "Lock escalation", "Lock granularity", "Lock compatibility"],
                "answer": 0,
                "why": "Conversion changes the mode of a lock, and it may only happen during the growing phase.",
            },
        ],
        "examTip": "State the two phase rule, then draw a transaction with an up arrow for growing and a down arrow for shrinking, marking the lock point.",
    },

    "CSCA413-MIII-T05": {
        "explanation": "Timestamp ordering gives every transaction a start time and forces conflicting operations to obey that order. Each item remembers who last read and wrote it, and an operation that arrives too late is refused and its transaction restarted. The Thomas write rule is a saving: an obsolete write is ignored instead of causing a restart. Validation based control is optimistic, because transactions run freely and are checked only at commit, in the read, validation and write phases. The gain over locking is that neither method makes a transaction wait, so no deadlock can form.",
        "example": "Two transactions start together and the one with the smaller timestamp is treated as older. If a younger transaction has already overwritten the item, the older transaction's late write is ignored rather than forced to restart.",
        "quiz": [
            {
                "q": "What happens to a transaction whose operation arrives after a younger one has already used the item?",
                "options": ["It waits for the younger one to finish", "It is restarted with a new timestamp", "It is allowed to proceed", "It downgrades its lock"],
                "answer": 1,
                "why": "Timestamp ordering never waits; the late transaction is rolled back and started again.",
            },
            {
                "q": "What does the Thomas write rule do?",
                "options": ["Ignores an obsolete write instead of restarting the transaction", "Rejects every late read", "Forces all writes to wait for a lock", "Converts a shared lock into an exclusive lock"],
                "answer": 0,
                "why": "If a younger transaction has already overwritten the value, the older write is obsolete and can be skipped.",
            },
            {
                "q": "Which statement about concurrency methods is NOT correct?",
                "options": ["Timestamp ordering can cause restarts but not deadlock", "Validation methods check for conflicts at commit time", "Optimistic control has read, validation and write phases", "Locking methods are free of deadlock because they never wait"],
                "answer": 3,
                "why": "Locking is the method that waits for locks, and that waiting is exactly what allows a deadlock to form.",
            },
            {
                "q": "What are the three phases of validation based concurrency control?",
                "options": ["Grow, shrink, commit", "Read, validation, write", "Parse, optimise, execute", "Analysis, redo, undo"],
                "answer": 1,
                "why": "The transaction reads freely, is validated against the others at commit, then writes if it passes.",
            },
            {
                "q": "Which method never makes a transaction wait for another?",
                "options": ["Two phase locking", "Timestamp ordering", "Strict two phase locking", "Multiple granularity locking"],
                "answer": 1,
                "why": "Timestamp and validation methods refuse and restart instead of blocking, so no waiting cycle appears.",
            },
        ],
        "examTip": "Compare locking, timestamp ordering and validation in one table with the columns waiting, deadlock, restarts and when the check happens.",
    },

    "CSCA413-MIII-T06": {
        "explanation": "Granularity is how big the piece is that a lock covers. A small unit such as one row lets many transactions work at once, but the system must track a great many locks. A large unit such as a whole table is cheap to track and blocks almost everything, so concurrency suffers. Multiple granularity locking lets a transaction lock at the level it needs, using a hierarchy from database down to record. Intention locks mark the ancestors of the item being locked: IS means a descendant will be read, IX means one will be written. A compatibility matrix then decides which combinations may be granted together.",
        "example": "Updating one row out of ten thousand should lock that row, not the table. Reading a whole report may lock the table once, which is cheaper than ten thousand row locks.",
        "quiz": [
            {
                "q": "What does a coarse granularity give?",
                "options": ["High concurrency and high lock overhead", "Low lock overhead and low concurrency", "High concurrency and low overhead", "No locking at all"],
                "answer": 1,
                "why": "One big lock is cheap to track, but it blocks transactions that only wanted a different part of the data.",
            },
            {
                "q": "What does an intention shared (IS) lock signal?",
                "options": ["The item itself is locked for writing", "A descendant of this item will be locked in shared mode", "The whole database is locked exclusively", "The lock has been released already"],
                "answer": 1,
                "why": "Intention locks are taken on ancestors to announce what is going to be locked below them.",
            },
            {
                "q": "Which statement about granularity is NOT correct?",
                "options": ["Fine granularity increases concurrency", "Fine granularity increases the number of locks to track", "Intention locks are taken on the ancestors of an item", "The database level is the finest granularity available"],
                "answer": 3,
                "why": "The whole database is the coarsest unit; a single field or one record is the finest.",
            },
            {
                "q": "A transaction wants to update a few rows deep inside one table. Which choice is best?",
                "options": ["Lock the whole database for reading", "Take an IX lock on the table and X locks on the rows", "Take a shared lock on the whole table", "Take no locks and rely on timestamps"],
                "answer": 1,
                "why": "The intention exclusive lock on the table announces the writes, and the row locks keep the rest available.",
            },
        ],
        "examTip": "Draw the hierarchy database, table, page, record as a tree, and write IS, IX, S and X at the levels involved.",
    },

    "CSCA413-MIII-T07": {
        "explanation": "Recovery brings the database back to a consistent state after something goes wrong. Failures fall into four kinds: the transaction itself fails, the system crashes, the media is lost, or the site is destroyed. The log is the main tool, because it records before images, after images and the events of each transaction. With it, undo rolls back a transaction that never committed and redo repeats one that did. Checkpoints shorten recovery, because work before the checkpoint is already known to be safe. ARIES is the common algorithm, using write ahead logging, repeating history and fuzzy checkpoints in three passes: analysis, redo and undo.",
        "example": "A power cut during a fee payment leaves some rows half updated. The log tells recovery which transactions had committed, so their writes are repeated and the others are undone.",
        "quiz": [
            {
                "q": "Which pass of ARIES repeats the writes of committed transactions?",
                "options": ["Analysis", "Redo", "Undo", "Checkpoint"],
                "answer": 1,
                "why": "Redo repeats history so that every committed write is on disk, whatever happened before the crash.",
            },
            {
                "q": "What is the purpose of a checkpoint?",
                "options": ["To stop deadlocks from forming", "To shorten recovery by flushing the log and buffers", "To encrypt the log", "To convert shared locks to exclusive locks"],
                "answer": 1,
                "why": "Everything before the checkpoint is already safe, so recovery starts from there instead of from the beginning.",
            },
            {
                "q": "Which statement about recovery is NOT correct?",
                "options": ["Shadow paging avoids a log but fragments storage", "Write ahead logging puts the log record on disk before the data page", "A media failure is handled in the same way as a transaction failure", "Stable storage is meant to survive any single failure"],
                "answer": 2,
                "why": "Media loss needs the last backup plus the archived log, while a transaction failure only needs undo.",
            },
            {
                "q": "Which technique keeps a current and a shadow page table and switches between them on commit?",
                "options": ["Checkpointing", "Shadow paging", "Write ahead logging", "Deferred update"],
                "answer": 1,
                "why": "Shadow paging makes commit atomic by switching page tables, at the cost of scattered pages on disk.",
            },
            {
                "q": "In deferred update, when are changes written to the database?",
                "options": ["Immediately, before the log record is written", "Only after the transaction commits", "At every checkpoint", "Only when the buffer is full"],
                "answer": 1,
                "why": "Deferred update keeps changes in the log until commit, so an aborted transaction needs no undo at all.",
            },
        ],
        "examTip": "Name the four failure types, then say what each needs: undo, redo, or the backup plus archived log.",
    },

    "CSCA413-MIII-T08": {
        "explanation": "Database security keeps data away from people who should not read or change it. Discretionary access control lets the owner of an object grant privileges to others, while mandatory access control assigns security levels and compares them. A view is a simple tool: give a user only the view, and they see only the rows and columns it holds. Encryption protects data in storage and while it travels across a network, and an audit trail records who did what and when. Statistical databases need their own care, because averages and counts can be combined to reveal one person's value.",
        "example": "A clerk is given a view showing only customer names and cities, never the account balances. Running one query on five people and another on four can reveal the fifth person's salary, which is the inference problem.",
        "quiz": [
            {
                "q": "Which control model lets the owner of a table grant privileges to other users?",
                "options": ["Mandatory access control", "Discretionary access control", "Role based encryption", "Audit based control"],
                "answer": 1,
                "why": "Discretionary control is based on the owner's decision to grant or revoke a privilege.",
            },
            {
                "q": "How does a view improve security?",
                "options": ["It encrypts the underlying table", "It exposes only the rows and columns the view contains", "It makes the table read faster", "It removes the need for an audit trail"],
                "answer": 1,
                "why": "The user queries the view and never reaches the columns that were left out of it.",
            },
            {
                "q": "Which statement about database security is NOT correct?",
                "options": ["An audit trail records who accessed what and when", "Encryption protects data in storage and in transit", "Statistical queries can leak an individual value by inference", "Mandatory access control lets any owner grant away their privileges"],
                "answer": 3,
                "why": "Granting privileges at the owner's discretion is discretionary control; mandatory control compares fixed security levels.",
            },
            {
                "q": "A user counts all employees, then counts all but one, and works out the missing salary. What is this called?",
                "options": ["A brute force attack", "An inference attack on a statistical database", "A denial of service attack", "A replay attack"],
                "answer": 1,
                "why": "Query restriction, perturbation and output auditing are the usual defences against this kind of leak.",
            },
            {
                "q": "Which of these is NOT a usual defence for statistical database security?",
                "options": ["Query restriction", "Data perturbation", "Auditing the queries that were answered", "Granting every user full read access"],
                "answer": 3,
                "why": "The three defences limit what may be asked, add noise to the answer, or watch what has been released.",
            },
        ],
        "examTip": "Write the four headings access control, views, encryption and auditing, then add the inference problem with its three defences.",
    },
}
