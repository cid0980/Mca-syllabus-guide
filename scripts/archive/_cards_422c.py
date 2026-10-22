# CSCA 422 Operating Systems - Modules IV and V
# Disk scheduling, file systems, and case studies.

CODE = "CSCA422"

CARDS = {
    "CSCA422-MIV-T01": {
        "explanation": "A disk holds data on spinning platters divided into tracks, and each track into sectors. Reading a block costs three things: seek time to move the head, rotational latency to wait for the sector, and transfer time to read it. Seek time usually dominates, so the order requests are served in matters a great deal. First come first served is fair but lets the head wander. Shortest seek time first picks the nearest request, which is fast but can starve a far one. SCAN sweeps the head back and forth like an elevator, and C-SCAN returns without serving to even out the wait.",
        "example": "With requests at cylinders 98, 183, 37 and 122 starting from 53, FCFS moves the head a long way. SSTF would serve 37 first, cutting the total head movement sharply.",
        "quiz": [
            {
                "q": "Which component of disk access time usually dominates?",
                "options": ["Transfer time", "Rotational latency", "Seek time", "Interrupt handling"],
                "answer": 2,
                "why": "Moving the arm mechanically is far slower than spinning or transferring, so seek decides the order.",
            },
            {
                "q": "How does C-SCAN differ from SCAN?",
                "options": ["C-SCAN serves in both directions", "C-SCAN serves in one direction and returns without serving", "C-SCAN is always slower", "C-SCAN only works on solid state drives"],
                "answer": 1,
                "why": "Serving in one direction only makes the waiting time more even for requests at the edges.",
            },
            {
                "q": "Which statement about disk scheduling is NOT correct?",
                "options": ["SSTF can starve a request far from the head", "LOOK reverses at the last request instead of the disk edge", "FCFS gives the shortest total head movement", "SCAN works like an elevator sweeping back and forth"],
                "answer": 2,
                "why": "FCFS is the fair but wasteful one; SSTF and SCAN cut head movement dramatically.",
            },
            {
                "q": "A disk queue has requests at 10, 90 and 30, and the head is at 50 moving upward. Which does SCAN serve first?",
                "options": ["10", "30", "90", "None of these"],
                "answer": 2,
                "why": "The head is moving up, so the next request above it, at 90, is served first.",
            },
            {
                "q": "What does LOOK do differently from SCAN?",
                "options": ["It reverses at the last request, not at the disk edge", "It serves every request twice", "It ignores far requests", "It sorts by sector instead of cylinder"],
                "answer": 0,
                "why": "Reversing at the last request saves the wasted sweep to the end of the disk.",
            },
        ],
        "examTip": "List seek time, latency and transfer time, then work one queue through FCFS, SSTF and SCAN and compare movement.",
    },

    "CSCA422-MIV-T02": {
        "explanation": "A file is a named collection of information stored on secondary storage. It carries attributes such as a name, an identifier, a type, a location, a size, protection and timestamps. The operations a program can ask for are create, open, read, write, seek, delete and truncate. Data can be reached sequentially, directly by block number, or through an index of keys. Directories hold the names and let them be organised as a single level list, a two level list, a tree or an acyclic graph. Protection decides who may read, write or execute.",
        "example": "Reading a database table record by record is sequential access. Jumping straight to the row with a known key, as an index allows, is direct access.",
        "quiz": [
            {
                "q": "Which of these is NOT a file operation?",
                "options": ["create", "truncate", "seek", "route"],
                "answer": 3,
                "why": "The operations are create, open, read, write, seek, delete and truncate; routing is a network idea.",
            },
            {
                "q": "Which access method jumps straight to a record with a known key?",
                "options": ["Sequential access", "Direct access", "Indexed access", "Serial access"],
                "answer": 2,
                "why": "Indexed access keeps an index of keys pointing at blocks, which is how a database finds one row.",
            },
            {
                "q": "Which statement about directories is NOT correct?",
                "options": ["A single level directory holds all files in one list", "A tree directory allows subdirectories", "An acyclic graph directory allows sharing", "A two level directory gives every user the same directory"],
                "answer": 3,
                "why": "Two level directories give each user their own directory, which is the point of the scheme.",
            },
            {
                "q": "Which file attribute records when the file was last changed?",
                "options": ["Identifier", "Type", "Timestamp", "Location"],
                "answer": 2,
                "why": "Timestamps record creation, last modification and last access, which backup tools rely on.",
            },
            {
                "q": "What does the protection attribute control?",
                "options": ["The file size", "Who may read, write or execute the file", "The file location on disk", "The file name length"],
                "answer": 1,
                "why": "Access rights, permission bits and access control lists are all ways of expressing it.",
            },
        ],
        "examTip": "List the seven attributes and the seven operations, then give the three access methods with an example each.",
    },

    "CSCA422-MIV-T03": {
        "explanation": "On disk a file system needs a boot control block, a volume control block, the directory structure and a control block for each file. In memory it keeps a mount table, a directory cache, a system wide open file table and a per process table. Three allocation methods exist. Contiguous allocation is fast and simple but cannot grow and fragments the disk. Linked allocation removes external fragmentation but only supports slow sequential access. Indexed allocation keeps an index block of pointers, which supports direct access at the cost of the index.",
        "example": "Unix inodes are indexed allocation: one block holds the attributes and a list of pointers to the data blocks, with indirect blocks for large files.",
        "quiz": [
            {
                "q": "Which allocation method suffers external fragmentation and cannot grow a file easily?",
                "options": ["Contiguous", "Linked", "Indexed", "Hashed"],
                "answer": 0,
                "why": "A file needs one unbroken run of blocks, so it cannot grow past its neighbours.",
            },
            {
                "q": "What does an inode hold?",
                "options": ["Only the file name", "The file attributes and the pointers to its data blocks", "The free space map", "The directory tree"],
                "answer": 1,
                "why": "The name lives in the directory entry, which points at the inode holding everything else.",
            },
            {
                "q": "Which statement about implementation is NOT correct?",
                "options": ["A bit vector is one way to track free space", "A directory can be a linear list or a hash table", "Indexed allocation supports direct access", "Linked allocation gives the fastest random access"],
                "answer": 3,
                "why": "Following a chain of pointers means sequential access only, which is its main weakness.",
            },
            {
                "q": "What is a mount table used for?",
                "options": ["Listing the open files", "Recording which file systems are mounted where", "Storing the free blocks", "Caching directory names"],
                "answer": 1,
                "why": "It ties each mounted volume to its mount point in the directory tree.",
            },
            {
                "q": "Which method tracks free space with one bit per block?",
                "options": ["A linked list", "A bit vector", "Grouping", "Counting"],
                "answer": 1,
                "why": "A bit vector is compact and makes finding a run of free blocks easy.",
            },
        ],
        "examTip": "Draw the on disk and in memory structures, then compare contiguous, linked and indexed allocation in a table.",
    },

    "CSCA422-MIV-T04": {
        "explanation": "A distributed file system makes files on other machines look local. Naming turns a name into a location. Location transparency hides where the file sits, and location independence lets it move without the name changing. Access is either remote service, where every request goes to the server, or caching, where a copy is held locally and consistency must be managed. A stateful server remembers clients between requests, which is faster but needs crash recovery. A stateless server keeps nothing, so a restart is cheap. Replication copies files for availability, at the price of update propagation.",
        "example": "A lab mounts the department file server over NFS, so every machine sees the same home directories. The server is stateless enough that a reboot loses no client state.",
        "quiz": [
            {
                "q": "What does location transparency mean?",
                "options": ["The file has no name", "The user need not know where the file physically is", "The file never moves", "The file is encrypted"],
                "answer": 1,
                "why": "The name stays the same whatever machine the file is actually stored on.",
            },
            {
                "q": "Which statement about distributed file systems is NOT correct?",
                "options": ["Caching keeps a local copy for speed", "A stateless server keeps no client state between requests", "Replication needs update propagation", "A stateful server needs no crash recovery at all"],
                "answer": 3,
                "why": "Remembering client state is exactly what makes recovery necessary after a crash.",
            },
            {
                "q": "What is the main cost of file replication?",
                "options": ["More disk space and the need to propagate updates", "Slower reads", "No gain in availability", "Longer file names"],
                "answer": 0,
                "why": "Every copy has to be kept in step, and that is the hard part of replication.",
            },
            {
                "q": "Which is a distributed file system named in the syllabus?",
                "options": ["NTFS", "NFS", "ext4", "FAT32"],
                "answer": 1,
                "why": "NFS, the network file system, and AFS, the Andrew file system, are the two case studies.",
            },
            {
                "q": "Why might a stateless design be preferred?",
                "options": ["It is always faster", "A server crash loses no client state, so recovery is simple", "It uses less bandwidth", "It supports larger files"],
                "answer": 1,
                "why": "With nothing remembered, the server restarts and the clients carry on.",
            },
        ],
        "examTip": "Define transparency, contrast stateful and stateless service, then name NFS and AFS with one line each.",
    },

    "CSCA422-MV-T01": {
        "explanation": "Linux is a free, open source, UNIX like kernel that is monolithic but modular. Loadable kernel modules let drivers be added while the system runs, so the kernel grows without a rebuild. Processes are created with fork and exec, and the scheduler uses a fair priority scheme. Its virtual file system layer supports many file systems such as ext4 and XFS through one interface, with inodes, directories, links and mount points underneath. Memory uses demand paging with swap space, and devices appear as special files. Users, groups and permission bits control access, with sudo for privilege.",
        "example": "A driver for a new webcam can be inserted while the machine runs, and removed again without a reboot. That is what loadable kernel modules make possible.",
        "quiz": [
            {
                "q": "How does Linux create a new process?",
                "options": ["With CreateProcess only", "With fork followed by exec", "With a single spawn call", "With a boot loader"],
                "answer": 1,
                "why": "Fork copies the process and exec replaces its program, which is the classic UNIX pair.",
            },
            {
                "q": "What does the virtual file system layer do?",
                "options": ["Encrypts all files", "Gives one interface over several different file systems", "Manages the swap space", "Loads kernel modules"],
                "answer": 1,
                "why": "Programs use one set of calls whether the disk holds ext4, XFS or something else.",
            },
            {
                "q": "Which statement about Linux is NOT correct?",
                "options": ["Kernel modules can be loaded at run time", "Devices appear as special files", "It uses demand paging with swap", "It is a microkernel with everything running as a user process"],
                "answer": 3,
                "why": "Linux is monolithic; it only borrows modular loading from microkernel designs.",
            },
            {
                "q": "What does sudo do?",
                "options": ["Shuts the system down", "Runs one command with root privilege", "Creates a new user", "Formats a disk"],
                "answer": 1,
                "why": "It grants a single command the rights of root without logging in as root.",
            },
            {
                "q": "Which file system is commonly used on Linux today?",
                "options": ["NTFS", "ext4", "FAT32", "HFS"],
                "answer": 1,
                "why": "ext4 is the standard Linux file system, and XFS and Btrfs are also supported.",
            },
        ],
        "examTip": "Write the design principles, then one line each on processes, the VFS layer, memory and permissions.",
    },

    "CSCA422-MV-T02": {
        "explanation": "Windows is a commercial system built around a layered, object oriented design with a hybrid kernel. At the bottom sits a hardware abstraction layer, then the kernel, then executive services, then device drivers and subsystems, with the user environment on top. The executive works with objects, and programs reach them through handles rather than names. Configuration lives in the registry instead of in scattered text files. Processes are containers for threads, and the dispatcher schedules threads by priority with preemption. NTFS provides journaling, compression and encryption, and security uses access tokens.",
        "example": "A Windows program opens a file and receives a handle. Every later read and write passes that handle, so the object it points at can be renamed without breaking the program.",
        "quiz": [
            {
                "q": "What does the hardware abstraction layer do?",
                "options": ["Runs applications", "Hides differences between hardware platforms from the kernel above", "Manages the registry", "Formats disks"],
                "answer": 1,
                "why": "The rest of the system sees one machine, which is what makes Windows portable across hardware.",
            },
            {
                "q": "How do Windows programs refer to executive objects?",
                "options": ["By name every time", "Through handles", "By memory address", "By process id"],
                "answer": 1,
                "why": "A handle is an indirect reference the kernel resolves, so objects can be moved or renamed.",
            },
            {
                "q": "Which statement about Windows is NOT correct?",
                "options": ["The scheduler works on threads, not processes", "The registry holds system configuration", "NTFS supports journaling and encryption", "Windows uses a pure microkernel with no kernel mode services"],
                "answer": 3,
                "why": "Windows has a hybrid kernel, with many services still running in kernel mode.",
            },
            {
                "q": "What is an access token used for?",
                "options": ["Logging in to a website", "Carrying the security identity and privileges of a user or process", "Encrypting files", "Naming a handle"],
                "answer": 1,
                "why": "Every process carries a token, and the system checks it against the object's access rules.",
            },
            {
                "q": "Which file system does Windows use by default today?",
                "options": ["ext4", "FAT32", "NTFS", "XFS"],
                "answer": 2,
                "why": "NTFS adds journaling, compression, encryption and access control to the older FAT designs.",
            },
        ],
        "examTip": "Draw the layer stack from the hardware abstraction layer up, then add a line on handles, the registry and NTFS.",
    },

    "CSCA422-MV-T03": {
        "explanation": "Android is a mobile system built on a modified Linux kernel. Its layers are the kernel, a hardware abstraction layer, native libraries with the runtime, the application framework and the applications themselves. An app is built from four kinds of component: activities, services, broadcast receivers and content providers. An activity moves through a life cycle of callbacks: onCreate, onStart, onResume, onPause, onStop and onDestroy. That lets the system reclaim memory at any point. Old versions ran Dalvik, which compiled during execution, while ART compiles ahead of time.",
        "example": "Rotating the phone destroys and recreates the activity, so onCreate runs again. Saving state in onPause is what keeps the user's place from being lost.",
        "quiz": [
            {
                "q": "Which of these is NOT an Android application component?",
                "options": ["Activity", "Service", "Broadcast Receiver", "Servlet"],
                "answer": 3,
                "why": "The four components are Activity, Service, Broadcast Receiver and Content Provider.",
            },
            {
                "q": "What replaced Dalvik in later Android versions?",
                "options": ["ART", "JVM", "LLVM", "NTFS"],
                "answer": 0,
                "why": "The Android runtime compiles applications ahead of time instead of during execution.",
            },
            {
                "q": "Which statement about Android is NOT correct?",
                "options": ["It is built on a modified Linux kernel", "Each app runs in its own sandbox with a unique user id", "An activity has a life cycle the system controls", "Apps share one user id so they can read each other's files freely"],
                "answer": 3,
                "why": "Each app gets its own id, which is what keeps one app out of another's data.",
            },
            {
                "q": "Which callback runs when the activity becomes visible and interactive?",
                "options": ["onCreate", "onStart", "onResume", "onDestroy"],
                "answer": 2,
                "why": "onResume is where the activity is in the foreground and the user can interact with it.",
            },
            {
                "q": "How does an app get permission to use the camera?",
                "options": ["It asks the kernel directly", "It declares the permission and the user grants it at install or run time", "It edits the registry", "It opens a socket"],
                "answer": 1,
                "why": "Permissions are declared in the manifest and granted by the user, which is the sandbox model.",
            },
        ],
        "examTip": "Draw the five layers of the stack, list the four components, and give the activity life cycle in order.",
    },

    "CSCA422-MV-T04": {
        "explanation": "A virtual machine is software that looks like a complete computer to the operating system running inside it. The layer that does this is called a hypervisor. A type 1 hypervisor runs directly on the hardware, which is what data centres use. A type 2 hypervisor runs as an application on a host operating system. Three things must be virtualised. The processor is handled by trapping privileged instructions, and memory by mapping guest addresses through shadow or nested page tables. Devices are emulated or passed through. Containers are the lighter alternative, sharing the host kernel.",
        "example": "One physical server can host ten virtual machines. Each runs its own operating system and believes it owns the whole machine.",
        "quiz": [
            {
                "q": "Which type of hypervisor runs directly on the hardware?",
                "options": ["Type 1", "Type 2", "Type 3", "Type 4"],
                "answer": 0,
                "why": "A bare metal hypervisor sits on the hardware, and the guest systems run above it.",
            },
            {
                "q": "How is memory virtualised?",
                "options": ["By encrypting it", "By mapping guest addresses through shadow or nested page tables", "By swapping to disk", "By compressing pages"],
                "answer": 1,
                "why": "An extra level of address translation turns a guest physical address into a real one.",
            },
            {
                "q": "Which statement about virtualisation is NOT correct?",
                "options": ["Containers share the host kernel", "A type 2 hypervisor runs on a host operating system", "Snapshots make testing and rollback easy", "A virtual machine gives weaker isolation than a container"],
                "answer": 3,
                "why": "A virtual machine isolates at the hardware boundary, which is stronger than a shared kernel.",
            },
            {
                "q": "What happens when a guest runs a privileged instruction?",
                "options": ["It is ignored", "It is trapped and handled by the hypervisor", "It reboots the guest", "It always runs at full speed"],
                "answer": 1,
                "why": "Trapping is what lets the hypervisor keep control of the real hardware.",
            },
            {
                "q": "Why are containers lighter than virtual machines?",
                "options": ["They share the host kernel and carry no full guest operating system", "They run slower", "They cannot be networked", "They need more memory"],
                "answer": 0,
                "why": "No full guest operating system means faster start up and far less overhead.",
            },
        ],
        "examTip": "Contrast type 1 and type 2 hypervisors, name the three things virtualised, then compare containers with virtual machines.",
    },
}
