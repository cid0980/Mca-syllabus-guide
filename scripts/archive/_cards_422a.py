# CSCA 422 Operating Systems - Modules I and II
# Introduction, processes, CPU scheduling, synchronisation and deadlocks.

CODE = "CSCA422"

CARDS = {
    "CSCA422-MI-T01": {
        "explanation": "Operating systems are grouped by how they handle jobs, users and deadlines. A batch system collects similar jobs and runs them with no interaction, which leaves the processor idle during input and output. Multiprogramming keeps several jobs in memory so the processor switches to another while one waits, which raises utilisation. Time sharing switches fast enough that each user feels they have the machine, which is what interactive terminals needed. Real time systems must meet deadlines, hard ones strictly and soft ones usually. Distributed systems present many machines as one, while embedded and mobile systems fit into phones and appliances.",
        "example": "A college exam result job that runs overnight with no one watching is batch work. The lab terminals that must answer every keystroke at once are time sharing.",
        "quiz": [
            {
                "q": "Which system keeps several jobs in memory so the CPU switches while one waits for I/O?",
                "options": ["Batch", "Multiprogramming", "Real time", "Embedded"],
                "answer": 1,
                "why": "Keeping more than one job ready is what stops the processor idling during input and output.",
            },
            {
                "q": "Which system must meet strict deadlines?",
                "options": ["Batch system", "Time sharing system", "Real time system", "Network operating system"],
                "answer": 2,
                "why": "Hard real time systems must never miss a deadline, as in aircraft or medical control.",
            },
            {
                "q": "Which statement about OS types is NOT correct?",
                "options": ["Batch systems run without user interaction", "Time sharing gives each user a slice of time", "Multiprogramming keeps only one job in memory at a time", "Distributed systems present many machines as one"],
                "answer": 2,
                "why": "Holding several jobs in memory at once is the whole point of multiprogramming.",
            },
            {
                "q": "Android is an example of which kind of operating system?",
                "options": ["Batch", "Real time", "Mobile and embedded", "Network"],
                "answer": 2,
                "why": "Android is built for phones, which means a small footprint and tight power limits.",
            },
            {
                "q": "What is the difference between hard and soft real time?",
                "options": ["Hard real time is slower", "Hard real time must never miss a deadline, soft may occasionally", "Soft real time is used in aircraft", "There is no difference"],
                "answer": 1,
                "why": "Missing a hard deadline is a system failure, while missing a soft one only degrades quality.",
            },
        ],
        "examTip": "List the six types with one line each, and underline the difference between multiprogramming and time sharing.",
    },

    "CSCA422-MI-T02": {
        "explanation": "Structure is how the pieces of an operating system are arranged. A monolithic kernel is one large program in which any procedure can call any other, which is fast but hard to maintain. A layered system is built in levels, each using only the level below, which is easier to debug and slower in practice. A microkernel keeps only the essentials in the kernel and runs the rest as user processes. That improves reliability, because a failed service can be restarted. Modular and hybrid designs load parts of the kernel at run time, and a virtual machine layer offers several copies of the hardware.",
        "example": "Linux is monolithic but modular, so drivers can be loaded while it runs. A microkernel system runs the file system and the drivers outside the kernel as ordinary processes.",
        "quiz": [
            {
                "q": "Which structure keeps only essential services in the kernel?",
                "options": ["Monolithic", "Layered", "Microkernel", "Virtual machine"],
                "answer": 2,
                "why": "Everything else runs as a user process, so a crash there does not bring down the kernel.",
            },
            {
                "q": "What is the main advantage of a layered structure?",
                "options": ["It is the fastest", "It is easier to debug and verify", "It uses the least memory", "It needs no hardware support"],
                "answer": 1,
                "why": "Each level uses only the one below, so a fault can usually be traced to one layer.",
            },
            {
                "q": "Which statement about structures is NOT correct?",
                "options": ["A monolithic kernel is fast but hard to maintain", "A microkernel improves reliability", "Loadable modules let a kernel grow at run time", "A monolithic kernel cannot support device drivers"],
                "answer": 3,
                "why": "Monolithic kernels hold the drivers inside the kernel, which is why they are large.",
            },
            {
                "q": "What does a virtual machine structure present to the guest?",
                "options": ["A copy of the source code", "An illusion of complete hardware", "A new file system", "A faster processor"],
                "answer": 1,
                "why": "Each guest operating system believes it owns the machine, which is the point of the layer.",
            },
            {
                "q": "Why is a microkernel considered more secure?",
                "options": ["It uses encryption", "Fewer services run with full privilege, so the trusted core is smaller", "It is written in a safer language", "It has more lines of code"],
                "answer": 1,
                "why": "A smaller privileged core means less code that could damage the whole system.",
            },
        ],
        "examTip": "Draw the four structures in a row and write one advantage and one disadvantage under each.",
    },

    "CSCA422-MI-T03": {
        "explanation": "An operating system is best understood by the components it holds. Process management creates, schedules, synchronises and terminates processes and threads. Memory management tracks what memory is used, allocates and frees it and runs virtual memory. File and storage management organises files and directories on disk and decides who may reach them. Input output is handled through device drivers with buffering, caching and spooling, and networking adds the protocols. Protection and security run across all of them, controlling who may use what.",
        "example": "Printing a project report uses spooling. The file is queued to disk so the program finishes at once, and the printer takes it at its own pace.",
        "quiz": [
            {
                "q": "Which component decides which process runs on the CPU next?",
                "options": ["Memory management", "Process management", "File management", "Device management"],
                "answer": 1,
                "why": "Creating, scheduling and terminating processes and threads is the process manager's work.",
            },
            {
                "q": "What is spooling used for?",
                "options": ["Faster memory access", "Holding output for a slow device such as a printer", "Encrypting files", "Routing packets"],
                "answer": 1,
                "why": "The queue on disk frees the program at once instead of making it wait for the device.",
            },
            {
                "q": "Which statement about components is NOT correct?",
                "options": ["Memory management handles virtual memory", "File management organises directories", "Device drivers are part of I/O management", "Networking is handled entirely by the application layer"],
                "answer": 3,
                "why": "The operating system implements the protocol stack, and applications reach it through sockets.",
            },
            {
                "q": "Which of these is a user service rather than a system service?",
                "options": ["Resource allocation", "Accounting", "Program execution", "Error detection"],
                "answer": 2,
                "why": "Program execution, I/O and file operations are offered to users; allocation and accounting run behind them.",
            },
            {
                "q": "Which component decides who may read a file?",
                "options": ["Protection and security", "Process management", "Memory management", "Networking"],
                "answer": 0,
                "why": "Access control is a protection duty, and it applies to files, memory and devices alike.",
            },
        ],
        "examTip": "List the six components with one duty each, then split the services into the user and system groups.",
    },

    "CSCA422-MI-T04": {
        "explanation": "A system call is the doorway through which a program asks the kernel to do something for it. The call traps, which switches the processor to kernel mode, the service routine runs, and control returns with a result. Calls fall into groups: process control, file management, device management, information maintenance, communication and protection. Privileged instructions may run only in kernel mode, which is what keeps a user program from damaging the system. System programs such as compilers, editors and shells sit above the calls, and the design goal is to separate mechanism from policy.",
        "example": "A program calling open on a file does not read the disk itself. It traps into the kernel, which checks the permission and returns a file descriptor.",
        "quiz": [
            {
                "q": "What switches the processor from user mode to kernel mode?",
                "options": ["A function call inside the program", "A trap or software interrupt", "A page fault only", "A device driver"],
                "answer": 1,
                "why": "The trap raises the privilege level so the kernel routine can run safely.",
            },
            {
                "q": "Why are privileged instructions restricted to kernel mode?",
                "options": ["They are slower", "They could change the state of the whole machine", "They need more memory", "They are rarely used"],
                "answer": 1,
                "why": "Instructions that touch the hardware or the memory map must not be reachable by user code.",
            },
            {
                "q": "Which of these is NOT a category of system calls?",
                "options": ["Process control", "File management", "Device management", "Routing table design"],
                "answer": 3,
                "why": "The categories are process control, file, device, information, communication and protection.",
            },
            {
                "q": "Which is a system program rather than a system call?",
                "options": ["fork", "open", "A shell", "read"],
                "answer": 2,
                "why": "A shell is a program built on top of the calls, while fork, open and read are calls themselves.",
            },
            {
                "q": "What does separating mechanism from policy mean?",
                "options": ["Writing the kernel twice", "Providing the tool in the kernel but leaving the decision to higher levels", "Hiding the API", "Running two kernels"],
                "answer": 1,
                "why": "The kernel supplies how something can be done, and policy decides when it should be done.",
            },
        ],
        "examTip": "Describe the trap sequence in three steps, list the call categories, and state the kernel and user mode rule.",
    },

    "CSCA422-MI-T05": {
        "explanation": "A program is passive code on disk, while a process is that program in execution with a program counter and data. Everything the kernel knows about a process is kept in its process control block. That holds the identifier, the state, the registers, the memory limits and the open files. A process moves through the states new, ready, running, waiting and terminated. Queues hold the processes at each stage, and the long term, short term and medium term schedulers move them along. Switching from one running process to another is a context switch, which does no useful work.",
        "example": "Opening a browser and a text editor gives two processes. The kernel keeps a control block for each and swaps between them, saving the registers of one and loading the other.",
        "quiz": [
            {
                "q": "What is the difference between a program and a process?",
                "options": ["They are the same", "A program is passive code, a process is that code in execution", "A process is stored on disk", "A program has a program counter"],
                "answer": 1,
                "why": "Only the running instance has a program counter, registers and a current state.",
            },
            {
                "q": "What does the process control block hold?",
                "options": ["Only the process id", "State, program counter, registers, memory limits and open files", "Only the memory limits", "Only the open files"],
                "answer": 1,
                "why": "It is the complete description the kernel needs to stop and restart the process.",
            },
            {
                "q": "Which statement about processes is NOT correct?",
                "options": ["A context switch saves and restores process state", "The short term scheduler picks the next process to run", "A context switch does useful work for the user", "Processes may be new, ready, running, waiting or terminated"],
                "answer": 2,
                "why": "A context switch is pure overhead, because no application work happens while it runs.",
            },
            {
                "q": "Which scheduler decides which process is admitted to memory first?",
                "options": ["Short term scheduler", "Long term scheduler", "Medium term scheduler", "Dispatcher"],
                "answer": 1,
                "why": "The long term scheduler controls the degree of multiprogramming by admitting jobs.",
            },
            {
                "q": "Which mechanism lets two processes exchange data through the kernel?",
                "options": ["A context switch", "Message passing", "A page fault", "A system boot"],
                "answer": 1,
                "why": "Shared memory and message passing, including pipes and sockets, are the two classic ways.",
            },
        ],
        "examTip": "Draw the five state diagram with the transition labels, then list what the process control block stores.",
    },

    "CSCA422-MI-T06": {
        "explanation": "Scheduling is judged on utilisation, throughput, turnaround time, waiting time and response time. First come first served runs jobs in arrival order, which is fair but lets one long job hold up the rest, the convoy effect. Shortest job first picks the smallest burst and gives the lowest average waiting time, but the burst length has to be predicted. Round robin gives each process a quantum in turn, which suits time sharing and makes the quantum size matter. Priority scheduling risks starvation, which ageing prevents, and multilevel feedback queues move jobs between queues.",
        "example": "With a quantum of 20 ms, five processes each get a turn within 100 ms, which feels instant to a user. With a quantum of 1 ms, most of the time goes into switching instead of working.",
        "quiz": [
            {
                "q": "Which scheduling algorithm gives the lowest average waiting time?",
                "options": ["FCFS", "SJF", "Round Robin", "Priority"],
                "answer": 1,
                "why": "Running the shortest burst first is provably optimal for average waiting time.",
            },
            {
                "q": "What problem does a long job at the front of the queue cause in FCFS?",
                "options": ["Starvation", "The convoy effect", "Deadlock", "Thrashing"],
                "answer": 1,
                "why": "Short jobs queue behind one long job, so all their waiting times rise together.",
            },
            {
                "q": "Which statement about scheduling is NOT correct?",
                "options": ["Round robin gives each process a time quantum", "SJF needs the burst length to be known or predicted", "A very small quantum increases context switch overhead", "Priority scheduling cannot cause starvation"],
                "answer": 3,
                "why": "A low priority process can wait indefinitely, which is why ageing raises its priority over time.",
            },
            {
                "q": "What does a multilevel feedback queue allow?",
                "options": ["Only one queue of jobs", "A job to move between queues based on its behaviour", "Unlimited priority", "No preemption"],
                "answer": 1,
                "why": "Jobs that use up their whole quantum drop to a lower queue, which favours interactive work.",
            },
            {
                "q": "Which is the preemptive version of shortest job first?",
                "options": ["FCFS", "SRTF", "Round Robin", "Priority"],
                "answer": 1,
                "why": "Shortest remaining time first takes the processor away when a shorter job arrives.",
            },
        ],
        "examTip": "Write the five criteria, then give each algorithm in one line with its advantage and its weakness.",
    },

    "CSCA422-MII-T01": {
        "explanation": "When two processes share data, the part of each that touches that data is its critical section. If both run at once the result depends on the timing, which is a race condition. A correct solution must guarantee three things. Mutual exclusion means only one process is inside at a time, and progress means the system is not stuck. Bounded waiting puts a limit on how long a process may wait to enter. Peterson's solution meets all three for two processes using a flag array and a turn variable. Hardware helps with atomic instructions such as test and set and compare and swap.",
        "example": "Two processes both add one to a shared counter. The result can be one less than it should be, because both read the old value before either writes the new one.",
        "quiz": [
            {
                "q": "What is a race condition?",
                "options": ["Two processes finishing at the same time", "A result that depends on the timing of unsynchronised access to shared data", "A process that never gets the CPU", "A deadlock caused by semaphores"],
                "answer": 1,
                "why": "The outcome changes with the interleaving, which is exactly what synchronisation removes.",
            },
            {
                "q": "Which is NOT one of the three requirements of a solution?",
                "options": ["Mutual exclusion", "Progress", "Bounded waiting", "Preemption"],
                "answer": 3,
                "why": "The three are mutual exclusion, progress and bounded waiting; preemption is a different idea.",
            },
            {
                "q": "Which statement about the critical section problem is NOT correct?",
                "options": ["The critical section is the code that touches shared data", "Mutual exclusion allows one process at a time", "Peterson's solution handles two processes", "Disabling interrupts is a safe solution on a multiprocessor"],
                "answer": 3,
                "why": "Disabling interrupts stops only the local processor, so it fails when several share memory.",
            },
            {
                "q": "Which hardware instruction tests a value and sets it in one atomic step?",
                "options": ["test and set", "fetch and add", "compare and store", "load and clear"],
                "answer": 0,
                "why": "Test and set is the classic atomic primitive, and compare and swap is the other.",
            },
            {
                "q": "What does bounded waiting guarantee?",
                "options": ["The process finishes quickly", "There is a limit on how long a process waits to enter the section", "The system never deadlocks", "Only one process may wait"],
                "answer": 1,
                "why": "It stops a process being overtaken forever by others, which is what starvation means.",
            },
        ],
        "examTip": "State the three requirements in one line each, then give Peterson's solution or a hardware primitive as the example.",
    },

    "CSCA422-MII-T02": {
        "explanation": "A semaphore is an integer that may only be changed through two atomic operations, wait and signal. Wait decrements the value and blocks the process if the result would be negative, and signal increments it and wakes one waiting process. A binary semaphore takes only zero and one, so it works as a lock. A counting semaphore tracks how many units of a resource are free. The first implementations used busy waiting, so blocking implementations put waiting processes in a queue instead. Used wrongly they still cause trouble: waits in the wrong order deadlock, and an unfair wake policy starves.",
        "example": "A printing pool with three printers is a counting semaphore starting at 3. Each job waits before printing and signals when it finishes, so the fourth job waits its turn.",
        "quiz": [
            {
                "q": "What does the wait operation do?",
                "options": ["Increments the value", "Decrements the value and blocks if it would go negative", "Resets the semaphore", "Wakes a waiting process"],
                "answer": 1,
                "why": "Wait is the request side of the pair, and it blocks when the resource is not available.",
            },
            {
                "q": "What is a binary semaphore used as?",
                "options": ["A counter of free resources", "A lock with values 0 and 1", "A message queue", "A page table entry"],
                "answer": 1,
                "why": "Two values are enough to say locked or unlocked, which is what mutual exclusion needs.",
            },
            {
                "q": "Which statement about semaphores is NOT correct?",
                "options": ["wait and signal must be atomic", "A counting semaphore tracks a pool of resources", "Busy waiting wastes processor time", "Semaphores remove the possibility of deadlock entirely"],
                "answer": 3,
                "why": "Two processes waiting on each other's semaphore still deadlock, so the ordering must be right.",
            },
            {
                "q": "Why is a blocking semaphore better than a busy waiting one?",
                "options": ["It is easier to write", "Waiting processes use no processor time", "It never deadlocks", "It works without a queue"],
                "answer": 1,
                "why": "A blocked process is put in a queue and woken later, instead of spinning in a loop.",
            },
            {
                "q": "A semaphore starts at 3. After five waits and two signals, what is its value?",
                "options": ["0", "-2", "2", "-3"],
                "answer": 1,
                "why": "Three minus five plus two gives zero, and two processes are blocked waiting.",
            },
        ],
        "examTip": "Write wait and signal in pseudo code, then give one binary and one counting example.",
    },

    "CSCA422-MII-T03": {
        "explanation": "Three problems are used to test any synchronisation tool. In the bounded buffer problem producers wait when the buffer is full and consumers when it is empty. Three semaphores do the work: empty, full and mutex. In the readers writers problem many readers may share the data, but a writer needs it alone; a solution either favours readers or writers. In the dining philosophers problem five philosophers share five forks, and taking one fork each deadlocks everyone. The fixes are asymmetry, a limit on how many may sit, or a waiter who grants permission.",
        "example": "A canteen counter is a bounded buffer: the cooks stop when the tray rack is full and the students wait when it is empty. The rack itself needs a mutex so two hands do not take the same tray.",
        "quiz": [
            {
                "q": "In the bounded buffer problem, which semaphore makes a producer wait?",
                "options": ["full", "empty", "mutex", "count"],
                "answer": 1,
                "why": "The producer waits on empty, because there is no slot left to put a new item into.",
            },
            {
                "q": "What happens if every philosopher picks up the left fork at once?",
                "options": ["Everyone eats", "Deadlock, because each waits for the right fork", "One philosopher starves only", "Nothing, the problem is solved"],
                "answer": 1,
                "why": "Each holds one resource and waits for another, which is the circular wait condition.",
            },
            {
                "q": "Which statement about the classical problems is NOT correct?",
                "options": ["A writer needs exclusive access to the shared data", "Several readers may read at the same time", "The bounded buffer uses empty, full and mutex semaphores", "The dining philosophers problem has no workable solution"],
                "answer": 3,
                "why": "Several solutions exist, including asymmetry, limiting the number at the table and a waiter.",
            },
            {
                "q": "What does the mutex semaphore protect in the bounded buffer?",
                "options": ["The empty slots", "The buffer itself, so only one process touches it at a time", "The consumer", "The producer"],
                "answer": 1,
                "why": "Empty and full count the slots, while mutex guards the shared structure itself.",
            },
            {
                "q": "Which variant of the readers writers problem can starve a writer?",
                "options": ["The readers preference solution", "The writers preference solution", "Neither variant", "Both variants equally"],
                "answer": 0,
                "why": "If readers keep arriving, a waiting writer may never get exclusive access.",
            },
        ],
        "examTip": "Give the semaphore solution to the bounded buffer, then state the deadlock in dining philosophers and two fixes.",
    },

    "CSCA422-MII-T04": {
        "explanation": "Semaphores are flexible but easy to get wrong, so languages offer higher level tools. A conditional critical region declares the shared variable and the condition under which it may be touched, and the compiler adds the mutual exclusion. A monitor goes further. It is a module holding shared data and the procedures that work on it. Only one process may be inside at a time. Condition variables inside a monitor give the wait and signal operations, so a process can wait for a condition without holding the lock. Message passing is the alternative for systems without shared memory.",
        "example": "A monitor for a bank account holds the balance and the deposit and withdraw procedures. Only one caller can be inside either procedure, so the balance is never read half updated.",
        "quiz": [
            {
                "q": "What does a monitor guarantee automatically?",
                "options": ["Deadlock freedom", "Mutual exclusion, because only one process may be inside at a time", "Fast execution", "Message delivery"],
                "answer": 1,
                "why": "The compiler or runtime enforces the single entry rule, so the programmer cannot forget it.",
            },
            {
                "q": "What are condition variables used for inside a monitor?",
                "options": ["Storing the shared data", "Waiting for a condition without holding the lock", "Choosing which process runs next", "Counting the procedures"],
                "answer": 1,
                "why": "Wait releases the monitor so another process can enter, and signal wakes a waiter later.",
            },
            {
                "q": "Which statement about monitors is NOT correct?",
                "options": ["A monitor holds shared data and its procedures", "Only one process may be active inside a monitor", "Condition variables provide wait and signal", "Monitors remove the need to think about synchronisation at all"],
                "answer": 3,
                "why": "The exclusion is automatic, but which conditions to wait on is still the programmer's job.",
            },
            {
                "q": "When is message passing preferred over shared memory?",
                "options": ["On a single processor only", "When processes run on different machines with no shared memory", "When speed matters most", "When there is only one process"],
                "answer": 1,
                "why": "Without shared memory, sending a message through the kernel or the network is the only option.",
            },
            {
                "q": "What does a conditional critical region add to a plain critical region?",
                "options": ["A condition that must hold before the region may be entered", "A faster lock", "A second lock", "A message queue"],
                "answer": 0,
                "why": "The process waits until the condition is true, which is what the bounded buffer needs.",
            },
        ],
        "examTip": "Contrast semaphores and monitors in two lines, then give wait and signal on a condition variable.",
    },

    "CSCA422-MII-T05": {
        "explanation": "A deadlock needs four conditions at once: mutual exclusion, hold and wait, no preemption and circular wait. Break any one of them and deadlock cannot occur, which is the prevention approach. A resource allocation graph draws processes and resources as nodes, and a cycle in the graph means deadlock is possible. Avoidance refuses an allocation that would leave the system in an unsafe state, and the Banker's algorithm is the standard test for that. Detection lets deadlocks happen, finds them with a wait for graph, then recovers by aborting a process or taking a resource back.",
        "example": "Two processes each hold a printer and ask for the scanner the other holds. The resource allocation graph has a cycle, and neither process can finish.",
        "quiz": [
            {
                "q": "Which of the following is NOT a necessary condition for deadlock?",
                "options": ["Mutual exclusion", "Hold and wait", "Preemption of resources", "Circular wait"],
                "answer": 2,
                "why": "The condition is no preemption, so allowing resources to be taken away is a prevention method.",
            },
            {
                "q": "What does the Banker's algorithm test?",
                "options": ["Whether a deadlock has already happened", "Whether granting a request leaves the system in a safe state", "Which process to abort", "How much memory is free"],
                "answer": 1,
                "why": "A safe state is one in which some order lets every process still finish.",
            },
            {
                "q": "Which statement about deadlocks is NOT correct?",
                "options": ["A cycle in the resource allocation graph signals possible deadlock", "Prevention breaks one of the four conditions", "Imposing a resource ordering prevents circular wait", "Detection is impossible once a deadlock has occurred"],
                "answer": 3,
                "why": "Detection works with a wait for graph, and recovery then aborts or preempts to break it.",
            },
            {
                "q": "How can circular wait be prevented?",
                "options": ["By allowing preemption", "By imposing a total ordering on resource types", "By ignoring the problem", "By adding more processes"],
                "answer": 1,
                "why": "If every process asks in the same order, no cycle can form in the graph.",
            },
            {
                "q": "What is a safe state?",
                "options": ["One in which no process is running", "One in which some sequence lets every process finish", "One with no shared resources", "One with a single process"],
                "answer": 1,
                "why": "Safety is about the existence of a completion order, which is what the Banker's algorithm checks.",
            },
        ],
        "examTip": "List the four conditions, then give one handling method for each: prevention, avoidance, detection and recovery.",
    },
}
