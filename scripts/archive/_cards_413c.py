# CSCA 413 Database Management Systems - Modules IV and V
# File organisation, hashing, indexing, and the special purpose databases.

CODE = "CSCA413"

CARDS = {
    "CSCA413-MIV-T01": {
        "explanation": "A file is a collection of records held in blocks on disk, and the organisation decides what is fast and what is slow. The four operations are insertion, deletion, modification and retrieval of a record found by its search key. In a heap file records go wherever there is free space, so insertion is quick and search is slow. A sequential file keeps the records ordered by the search key, so search and ordered listing are fast while insertion needs the file rearranged. Hashing and indexing compute the location instead, trading extra space and maintenance for speed.",
        "example": "Mark sheets pinned into a folder in the order they arrive make a heap file. Sorted by roll number they become a sequential file, and finding one student becomes quick.",
        "quiz": [
            {
                "q": "Which file organisation gives fast insertion but slow search?",
                "options": ["Sequential file", "Heap file", "Indexed file", "Hashed file"],
                "answer": 1,
                "why": "A heap file places each new record wherever there is room, so there is no order to search on.",
            },
            {
                "q": "What is the blocking factor?",
                "options": ["The number of records that fit in one block", "The number of blocks in the file", "The size of the search key", "The time taken to read one record"],
                "answer": 0,
                "why": "Blocking factor is records per block, and it decides how many disk accesses a full scan needs.",
            },
            {
                "q": "Which statement about file organisation is NOT correct?",
                "options": ["Heap files keep no order among the records", "Sequential files keep records ordered by the search key", "Hashed files find a record by computing its address", "Sequential files make insertion cheap because no order is kept"],
                "answer": 3,
                "why": "Keeping the order is what makes insertion expensive in a sequential file, since records must be moved.",
            },
            {
                "q": "A file holds 10,000 records of 100 bytes each in blocks of 1,000 bytes. What is the blocking factor?",
                "options": ["10", "100", "1,000", "10,000"],
                "answer": 0,
                "why": "Blocking factor is the block size divided by the record size, so 1,000 divided by 100 gives 10.",
            },
            {
                "q": "Which key is used to identify the record being searched for?",
                "options": ["Primary key", "Search key", "Candidate key", "Sort key"],
                "answer": 1,
                "why": "Any field used to locate a record is a search key, whether or not its values are unique.",
            },
        ],
        "examTip": "List the four operations, then give one line each on heap, sequential, hashed and indexed with what is fast and what is slow.",
    },

    "CSCA413-MIV-T02": {
        "explanation": "Hashing runs the search key through a function and uses the answer as a bucket address. In static hashing the number of buckets is fixed in advance, so a growing file develops long overflow chains. A collision is when a record lands in a bucket that is already full, handled by open addressing, chaining or a second hash function. Extendible hashing lets the directory grow and shrink, splitting one bucket at a time as the file grows. Hashing is excellent for finding one exact record, but it cannot answer a range query at all, which is where an index wins.",
        "example": "A library hashes the book accession number to a shelf number, so one book is found directly. Asking for every book added last month cannot use the hash, because the buckets hold books in no useful order.",
        "quiz": [
            {
                "q": "What happens in static hashing as the file keeps growing?",
                "options": ["The buckets split automatically", "The overflow chains get longer", "The hash function changes", "The records are sorted inside each bucket"],
                "answer": 1,
                "why": "The bucket count is fixed, so extra records pile into overflow and searches slow down.",
            },
            {
                "q": "Which of these is NOT a way of handling a collision?",
                "options": ["Open addressing", "Chaining within the bucket", "Multiple hashing", "Sorting the whole file again"],
                "answer": 3,
                "why": "Open addressing, chaining and a second hash function resolve collisions; sorting does not.",
            },
            {
                "q": "Why is hashing unsuitable for a range query?",
                "options": ["The hash function is too slow", "Buckets hold records in no order that matches the key", "Hash tables cannot hold many records", "The directory would grow too large"],
                "answer": 1,
                "why": "The hash scatters keys across buckets, so nearby keys are not stored near each other.",
            },
            {
                "q": "What does extendible hashing do when a bucket overflows?",
                "options": ["It rebuilds the whole table with more buckets", "It splits that bucket and grows the directory", "It moves the record to overflow and leaves it there", "It switches over to a B+ tree"],
                "answer": 1,
                "why": "Only the overflowing bucket is split, and the directory uses one more bit for that part.",
            },
            {
                "q": "Which operation is hashing best at?",
                "options": ["Finding every record in a key range", "Finding one record with a known exact key", "Listing the records in sorted order", "Finding the smallest key in the file"],
                "answer": 1,
                "why": "An exact match goes straight to one bucket, which is usually a single disk access.",
            },
        ],
        "examTip": "Draw a bucket directory with two bits of the hash, then show one split. Finish with the line that hashing cannot do range queries.",
    },

    "CSCA413-MIV-T03": {
        "explanation": "An index is a small auxiliary file holding key and pointer pairs, so a record can be found without scanning the whole data file. A primary index is built on the ordering key field of a sequential file and holds one entry per block. A clustering index is built on an ordering field that is not a key, so several records may share one index entry. A secondary index is built on a field with no order at all, and it needs one entry per distinct value. A dense index has an entry for every search key value, while a sparse index has entries for only some of them. When an index itself grows too large to scan, it is indexed again, which gives a multilevel structure such as an ISAM tree.",
        "example": "The index at the back of a book is a secondary index. It maps each term to page numbers, and the pages themselves are not ordered by that term.",
        "quiz": [
            {
                "q": "Which index is built on the ordering key field of a sequential file?",
                "options": ["Secondary index", "Primary index", "Clustering index", "Dense index"],
                "answer": 1,
                "why": "A primary index follows the ordering key of the file and holds one entry for each block.",
            },
            {
                "q": "How does a dense index differ from a sparse index?",
                "options": ["A dense index has an entry for every search key value", "A dense index is stored on disk and a sparse one in memory", "A sparse index holds more entries than a dense one", "A dense index can only be built on a primary key"],
                "answer": 0,
                "why": "A sparse index saves space by holding entries for only some key values, one per block.",
            },
            {
                "q": "Which statement about indexes is NOT correct?",
                "options": ["A clustering index is built on an ordering non key field", "A secondary index needs one entry per distinct value", "A primary index can only be built on an unordered file", "A multilevel index puts an index on the index"],
                "answer": 2,
                "why": "A primary index needs the file to be ordered on that key; an unordered file needs a secondary index.",
            },
            {
                "q": "An index has grown so large that scanning it is slow. What is the usual answer?",
                "options": ["Sort the data file again", "Build an index on the index", "Convert the file into a hash file", "Split the data file into two"],
                "answer": 1,
                "why": "Indexing the index gives a multilevel structure, which is how ISAM and tree indexes work.",
            },
            {
                "q": "Which index suits a field where many records share the same value and the file is ordered on it?",
                "options": ["Primary index", "Clustering index", "Secondary index", "Dense index"],
                "answer": 1,
                "why": "A clustering index is built on an ordering field that is not unique, so one entry points at a cluster.",
            },
        ],
        "examTip": "Give one line each on primary, clustering and secondary, then add dense versus sparse. Sketch the multilevel index if the question carries marks for a diagram.",
    },

    "CSCA413-MIV-T04": {
        "explanation": "A B tree is a balanced search tree built for disk, where every leaf sits at the same level. Each node holds many keys, and one node is sized to fill a disk block. One read then brings in a whole set of comparisons. A node with k keys has k plus one children, and every node except the root must be at least half full. A B+ tree keeps data pointers only in the leaves and joins those leaves in a linked list. That makes the fan-out higher and the range scan a straight walk along the list, which is why databases use B+ trees.",
        "example": "With a fan-out of 100, a B+ tree of three levels already holds a million keys. Finding one record then costs three disk reads instead of scanning a million rows.",
        "quiz": [
            {
                "q": "Where does a B+ tree keep the pointers to the actual records?",
                "options": ["In the root node only", "In both the internal nodes and the leaves", "Only in the leaves", "In a separate hash directory"],
                "answer": 2,
                "why": "Internal nodes hold only keys and pointers to lower nodes, so all data pointers sit in the linked leaves.",
            },
            {
                "q": "A node in a B tree holds k keys. How many children does it have?",
                "options": ["k", "k plus one", "k minus one", "2k"],
                "answer": 1,
                "why": "Keys separate the children, so k keys split the node into k plus one subtrees.",
            },
            {
                "q": "Which statement about B+ trees is NOT correct?",
                "options": ["All the leaves are at the same level", "The leaves are linked for fast range scans", "Every node except the root is at least half full", "A B+ tree stores record pointers in its internal nodes"],
                "answer": 3,
                "why": "Keeping internal nodes free of data pointers is what raises the fan-out and keeps the tree shallow.",
            },
            {
                "q": "A leaf is full and a new key must go into it. What happens?",
                "options": ["The key is placed in an overflow area", "The leaf is split and the middle key moves up", "The whole tree is rebuilt", "The key is rejected"],
                "answer": 1,
                "why": "Splitting can cascade upwards, and splitting the root is how the tree gains a level.",
            },
            {
                "q": "What happens when a deletion leaves a node below the minimum occupancy?",
                "options": ["The tree is rebuilt from scratch", "Keys are shared with a sibling, or the nodes are merged", "The key is put back where it was", "The tree switches to a hash file"],
                "answer": 1,
                "why": "Redistribution is tried first, and merging two nodes is the fallback when a sibling cannot spare a key.",
            },
        ],
        "examTip": "Sketch a B+ tree with linked leaves, then note the two reasons it wins: higher fan-out and a straight walk along the leaves.",
    },

    "CSCA413-MV-T01": {
        "explanation": "An object oriented database stores objects, with their state and their methods, instead of rows in tables. It exists because applications such as computer aided design, multimedia and geographic systems hold data too complex to flatten. The mismatch between program objects and table rows is called the impedance mismatch, and an OODBMS removes it. Object identity, encapsulation, inheritance, polymorphism and persistence are all supported directly by the database. The cost is weaker support for ad hoc queries and the absence of one common standard, which kept these systems out of the mainstream.",
        "example": "A circuit design holds thousands of connected parts, each with its own behaviour. Storing it as objects keeps the connections and the code together, while flattening it into tables would need dozens of joined tables.",
        "quiz": [
            {
                "q": "What is the impedance mismatch?",
                "options": ["The delay between two disks", "The gap between program objects and table rows", "A fault in the network cable", "The extra cost of a licence"],
                "answer": 1,
                "why": "Objects carry identity, nesting and methods, which do not map cleanly onto flat rows and columns.",
            },
            {
                "q": "Which of these is NOT a feature of an object oriented database?",
                "options": ["Object identity", "Inheritance and polymorphism", "Encapsulation of state and methods", "One query standard agreed by every vendor"],
                "answer": 3,
                "why": "The features are native, but the lack of a common standard is the main weakness of these systems.",
            },
            {
                "q": "Which application area pushed the need for object oriented databases?",
                "options": ["Simple payroll processing", "Computer aided design and geographic systems", "A single table stock list", "Plain text storage"],
                "answer": 1,
                "why": "Complex, deeply connected data is hard to flatten into tables, which is where these systems help.",
            },
            {
                "q": "Which statement about an OODBMS is NOT correct?",
                "options": ["It stores objects together with their methods", "It suits navigational access through references", "It is weaker than a relational system for ad hoc queries", "It replaced the relational model in most commercial products"],
                "answer": 3,
                "why": "Relational systems stayed dominant, and object relational features were added to them instead.",
            },
        ],
        "examTip": "Define OODBMS, give the impedance mismatch as the reason, list five features, then write two advantages and two disadvantages.",
    },

    "CSCA413-MV-T02": {
        "explanation": "An object relational system keeps the relational model and adds object features to it. Tables can use user defined types, hold collections such as arrays and nested tables, and carry references and object identifiers. Methods can be attached to a type, so a value knows what it can do. This lets a program's objects be stored as rows without throwing away SQL, which is what object relational mapping does. It is the middle way: relational systems flatten complex data, object oriented systems lose SQL, and object relational systems keep both.",
        "example": "An address can be one user defined type holding street, city and pin code. It sits in a customer row as one column, and reports still run plain SQL.",
        "quiz": [
            {
                "q": "What does an object relational DBMS add to the relational model?",
                "options": ["Nothing, it is only a new name", "User defined types, collections, references and methods", "A replacement for SQL", "A hash based storage engine only"],
                "answer": 1,
                "why": "These additions let complex values sit inside a row while SQL still works on the table.",
            },
            {
                "q": "What is object relational mapping?",
                "options": ["Drawing an ER diagram for an object model", "Persisting program objects as rows and columns", "Converting a table into a hash file", "Splitting a table into two for normalisation"],
                "answer": 1,
                "why": "The mapping layer moves data between the objects a program uses and the rows a database stores.",
            },
            {
                "q": "Which statement about the three approaches is NOT correct?",
                "options": ["Relational systems flatten complex data into tables", "Object oriented systems give up the simplicity of SQL", "Object relational systems keep tables and add object features", "Object relational systems cannot run SQL at all"],
                "answer": 3,
                "why": "Keeping SQL is the whole point of the object relational route, which is why vendors followed it.",
            },
            {
                "q": "Which kind of value can be stored as one column in an object relational table?",
                "options": ["A nested table or an array", "An integer only", "A fixed length string only", "A date only"],
                "answer": 0,
                "why": "Collections such as arrays and nested tables are part of what the object relational model added.",
            },
        ],
        "examTip": "Compare RDBMS, OODBMS and ORDBMS in one table with the columns storage unit, query language, complex data and typical use.",
    },

    "CSCA413-MV-T03": {
        "explanation": "XML is a text format where the tags travel with the data, so a document describes itself. A well formed document has a prolog, one root element and properly nested elements with attributes and text. A DTD or an XML Schema says which elements and attributes are allowed, so a document can be checked before it is used. Programs read a document with a DOM parser, which builds a tree in memory, or a SAX parser, which reports events as it reads. XPath and XQuery select parts of a document, and XSLT transforms it. A database may store the document whole, shred it into tables or keep it in a native XML column.",
        "example": "A college sends a student list to the university as XML, with one element per student and an attribute for the roll number. The receiving system reads it even though it runs different software.",
        "quiz": [
            {
                "q": "Which part of an XML document declares which elements and attributes are allowed?",
                "options": ["The prolog", "A DTD or an XML Schema", "The root element", "An XSLT stylesheet"],
                "answer": 1,
                "why": "A DTD or a schema is the grammar of the document, and it is what validation is checked against.",
            },
            {
                "q": "Which parser builds a full tree of the document in memory?",
                "options": ["SAX", "DOM", "XPath", "XSLT"],
                "answer": 1,
                "why": "DOM holds the whole tree so any node can be revisited; SAX reports events once and keeps nothing.",
            },
            {
                "q": "Which statement about storing XML is NOT correct?",
                "options": ["A document can be stored whole as a large character object", "A document can be shredded into relational tables", "A document can be kept in a native XML column", "A document must be shredded, because no other option exists"],
                "answer": 3,
                "why": "All three storage choices exist, and the right one depends on how the data will be queried.",
            },
            {
                "q": "Which language is used to select nodes from an XML document?",
                "options": ["XPath", "HTML", "SQL on its own", "DTD"],
                "answer": 0,
                "why": "XPath addresses nodes by path and condition; XQuery extends it and XSLT transforms the result.",
            },
            {
                "q": "What makes XML self describing?",
                "options": ["It is stored in binary form", "The tags travel with the data", "Only one program can read it", "It needs a schema before it can be read"],
                "answer": 1,
                "why": "The element names sit inside the file, so a reader understands the structure without outside help.",
            },
        ],
        "examTip": "Show a four line XML sample, then name the DTD or schema for validation, the two parsers, and the query languages.",
    },

    "CSCA413-MV-T04": {
        "explanation": "A conventional database keeps only the current value, so an old value is lost the moment it is overwritten. A temporal database keeps time with the data and answers questions about the past. Valid time is when a fact was true in the real world, and transaction time is when the database recorded it. A bitemporal database keeps both, so it can say what was true on a date and what the system believed at the time. Queries then use interval operators such as overlaps, contains, precedes and during. Typical uses are banking audit trails, medical records, insurance history and employee service records.",
        "example": "A salary changed in April but the record was corrected in June. Valid time says April and transaction time says June, so the database can show both what was true and when it was learned.",
        "quiz": [
            {
                "q": "What is valid time?",
                "options": ["When the database stored the record", "When the fact was true in the real world", "When the user logged in", "When the record was deleted"],
                "answer": 1,
                "why": "Valid time is about the real world; transaction time is about when the system recorded it.",
            },
            {
                "q": "What does a bitemporal database keep?",
                "options": ["Valid time only", "Transaction time only", "Both valid time and transaction time", "The current value only"],
                "answer": 2,
                "why": "Keeping both lets a query ask what was true and what the system knew, as two separate questions.",
            },
            {
                "q": "Which statement about temporal databases is NOT correct?",
                "options": ["They answer questions about past states of the data", "Banking audit trails are a typical use", "Interval operators include overlaps and during", "They store only the latest value of every fact"],
                "answer": 3,
                "why": "Storing only the latest value is what a conventional database does; a temporal one keeps the history.",
            },
            {
                "q": "Which operator tests whether two time intervals share any period?",
                "options": ["Precedes", "Overlaps", "Contains", "Equals"],
                "answer": 1,
                "why": "Overlaps is true when the two intervals have at least one instant in common.",
            },
            {
                "q": "A correction is made in June to a salary that changed in April. Which times differ?",
                "options": ["Both stay the same", "Valid time is April, transaction time is June", "Valid time is June, transaction time is April", "Neither can be recorded"],
                "answer": 1,
                "why": "The real world change and the moment the system learned of it are two separate facts.",
            },
        ],
        "examTip": "Define valid time and transaction time with one example each, then say that a bitemporal database keeps both and give two applications.",
    },

    "CSCA413-MV-T05": {
        "explanation": "A mobile database lives on a portable device and syncs with a central server over a wireless link. The assumptions of a fixed network no longer hold. The device is often disconnected, the bandwidth is limited, the battery is small and the memory is tight. Changes are therefore made on the device and reconciled with the server later, which is what synchronisation and replication do. That reconciliation can produce conflicts, so rules are needed to decide which change wins. Mobile transactions are long lived and location dependent, and some systems relax the ACID rules to let them finish.",
        "example": "A sales representative records orders on a tablet with no signal. At the office the orders are reconciled with the central database, and a rule settles any clash with a newer price.",
        "quiz": [
            {
                "q": "Which is NOT listed as a challenge for mobile databases?",
                "options": ["Frequent disconnection", "Limited bandwidth", "Low battery and small memory", "Too many indexes on the server"],
                "answer": 3,
                "why": "The challenges come from the device and the link: disconnection, bandwidth, battery and memory.",
            },
            {
                "q": "What happens when a device reconnects after working offline?",
                "options": ["Its changes are discarded", "Its changes are reconciled with the central database", "The server is rebuilt from the device", "Nothing, because the two stay separate"],
                "answer": 1,
                "why": "Synchronisation compares the two copies, applies the differences and resolves conflicts as it goes.",
            },
            {
                "q": "Why are mobile transactions described as long lived?",
                "options": ["They run on older hardware", "They may stay open across disconnections and movement between cells", "They always take more than an hour", "They are never committed"],
                "answer": 1,
                "why": "A transaction can span a journey and several network cells, so it runs far longer than a desktop one.",
            },
            {
                "q": "Which statement about mobile databases is NOT correct?",
                "options": ["Conflicts need resolution rules during synchronisation", "Some systems relax the ACID properties for mobile work", "Replication keeps a copy of the data on the device", "A mobile database needs a constant wired connection to work"],
                "answer": 3,
                "why": "Working while disconnected is the whole point, and it is what makes synchronisation necessary.",
            },
        ],
        "examTip": "List the four challenges, then explain synchronisation and conflict resolution, then add why ACID is sometimes relaxed.",
    },

    "CSCA413-MV-T06": {
        "explanation": "A spatial database stores geometric objects and answers questions about where things are. The basic types are point, line and region, and the queries ask things like finding every hospital within five kilometres. Ordinary indexes do not help, because they order values along one dimension while spatial data covers two. Spatial indexes such as R trees, quad trees and grid files organise the data by area. A region query then visits only the blocks it overlaps. Typical uses are geographic information systems, maps, navigation, urban planning and location based services.",
        "example": "A delivery app asks for every driver within three kilometres of a pickup point. An R tree groups nearby drivers into rectangles, so the search reads only a few blocks instead of every row.",
        "quiz": [
            {
                "q": "Which is NOT a basic spatial data type?",
                "options": ["Point", "Line", "Region", "Integer"],
                "answer": 3,
                "why": "Point, line and region are the geometric types; integer is a plain relational type.",
            },
            {
                "q": "Why does a normal B+ tree index work poorly for spatial data?",
                "options": ["It cannot hold numbers", "It orders values along one dimension only", "It is too slow to build", "It cannot be stored on disk"],
                "answer": 1,
                "why": "Spatial data covers two dimensions, so an index that sorts along one axis loses the neighbour information.",
            },
            {
                "q": "Which index organises spatial objects by grouping nearby ones into rectangles?",
                "options": ["B+ tree", "R tree", "Hash table", "Bitmap index"],
                "answer": 1,
                "why": "An R tree groups objects by their bounding rectangles, which suits area and nearest neighbour queries.",
            },
            {
                "q": "Which statement about spatial databases is NOT correct?",
                "options": ["They answer location based queries", "Navigation apps are a typical use", "Quad trees and grid files are spatial indexes", "They store only text descriptions of places"],
                "answer": 3,
                "why": "They store real geometry, which is what makes distance and containment queries possible.",
            },
            {
                "q": "Which application is least likely to need a spatial database?",
                "options": ["A city map service", "A flood risk model for a district", "A payroll system for office staff", "A bus route planner"],
                "answer": 2,
                "why": "Payroll has no geometry in it, so a plain relational design is enough.",
            },
        ],
        "examTip": "Name the three spatial types, one example query, three index structures and three applications.",
    },

    "CSCA413-MV-T07": {
        "explanation": "A case study runs one application through every stage the syllabus has covered. Requirement analysis lists the entities, attributes, relationships, constraints and the reports the users expect. Conceptual design turns that list into an ER diagram. Logical design maps the diagram into relations, picks the keys and normalises up to 3NF or BCNF. Physical design chooses the file organisation, the indexes, the constraints, the views, the triggers and the privileges each role needs. After release the work continues: watch the performance, rebuild the indexes, back up on a schedule and manage changes to the schema.",
        "example": "A college library project starts from the list of books, members and loans. It ends with normalised tables, an index on the accession number, a view for the student portal and a weekly backup.",
        "quiz": [
            {
                "q": "What is produced during conceptual design?",
                "options": ["The file organisation and the indexes", "An ER diagram of entities and relationships", "The backup schedule", "The user privileges"],
                "answer": 1,
                "why": "Conceptual design is the diagram; physical design is what chooses indexes, files and privileges.",
            },
            {
                "q": "At which stage are the tables normalised up to 3NF or BCNF?",
                "options": ["Requirement analysis", "Logical design", "Physical design", "Maintenance"],
                "answer": 1,
                "why": "Logical design maps the ER diagram into relations, chooses the keys and removes the anomalies.",
            },
            {
                "q": "Which statement about the stages is NOT correct?",
                "options": ["Requirement analysis lists the entities and the reports needed", "Physical design chooses indexes and file organisation", "Maintenance includes rebuilding indexes and backing up", "Conceptual design decides the storage layout on disk"],
                "answer": 3,
                "why": "Storage layout belongs to physical design; conceptual design is still a diagram of entities.",
            },
            {
                "q": "Which of these belongs to maintenance rather than to initial implementation?",
                "options": ["Choosing the primary key", "Drawing the ER diagram", "Rebuilding an index after heavy updates", "Deciding the privileges of a role"],
                "answer": 2,
                "why": "Rebuilding indexes and monitoring performance are ongoing jobs that start after release.",
            },
            {
                "q": "What is the usual order of the stages in a database project?",
                "options": ["Physical, logical, conceptual, requirements", "Requirements, conceptual, logical, physical", "Logical, physical, requirements, conceptual", "Conceptual, requirements, physical, logical"],
                "answer": 1,
                "why": "Each stage feeds the next: what is needed, what it looks like, how it is stored, how it is tuned.",
            },
        ],
        "examTip": "Write the four stages as headings and put two bullet points under each. Case study marks usually come from showing the order.",
    },
}
