# CSCA 413 Database Management Systems - Modules I and II
# Written from skills/CONTENT-STYLE.md: short sentences, one idea per question,
# four or five questions per card, one scenario and one "which is NOT" among them.

CODE = "CSCA413"

CARDS = {
    "CSCA413-MI-T01": {
        "explanation": "In the file processing approach every application owns its own files. The same student address then sits in the library file and again in the accounts file. That copying is redundancy, and when one copy is edited and the other is not, the data becomes inconsistent. Two users editing one file at the same time can overwrite each other, and access is granted for the whole file or not at all. A DBMS keeps the data in one place, lets many programs share it under rules called integrity constraints, and handles backup and recovery. The gain is smaller for a small program used by one person with fixed data, where a DBMS costs more than it returns.",
        "example": "A college stores fees in one spreadsheet and exam marks in another, and both hold the student phone number. When a student changes the number, only one sheet gets edited, and the office rings the old one.",
        "quiz": [
            {
                "q": "In file processing, what makes the same address appear differently in two files?",
                "options": ["Two users opening the file at once", "Program data independence", "Editing one copy and leaving the other alone", "The absence of a search key"],
                "answer": 2,
                "why": "Redundancy means several copies exist, and updating only one of them is what produces inconsistency.",
            },
            {
                "q": "Which of these is an advantage a DBMS brings over file processing?",
                "options": ["Controlled redundancy with integrity constraints", "Faster programs because no software layer sits between", "No need for any backup procedure", "Every user keeping a private copy of the data"],
                "answer": 0,
                "why": "A DBMS permits redundancy only where it is needed and enforces rules so the copies stay consistent.",
            },
            {
                "q": "A shopkeeper keeps one file of items on a single computer that nothing else reads. What does the card advise?",
                "options": ["Move to a three schema architecture", "Appoint a database administrator to control access", "Add a foreign key to every item", "A DBMS may not be worth the cost here"],
                "answer": 3,
                "why": "Small single user applications with simple fixed data usually cost less to run on plain files.",
            },
            {
                "q": "Which statement about file processing is NOT correct?",
                "options": ["Concurrent access is difficult to control", "Files give data independence from the program code", "Security is applied at the whole file level", "The same data is often stored in several files"],
                "answer": 1,
                "why": "Program data dependence is the drawback: change the file layout and every program reading it must change too.",
            },
        ],
        "examTip": "Write the five drawbacks of file processing in one line each, then the six DBMS advantages opposite them; this comparison is a repeated question.",
    },

    "CSCA413-MI-T02": {
        "explanation": "A data model is the set of ideas used to describe data before it is stored. The hierarchical model arranges records as a tree where every child has one parent, so one to many data is fast. The network model allows several parents through sets and pointers, but programs must navigate the links step by step. The relational model puts everything in tables whose rows are linked by matching key values, which is why it replaced both. Object based and object relational models add classes and inheritance, and the ER model is the diagram drawn before any of them is implemented.",
        "example": "A library keeps one member and many books borrowed by that member, which fits the hierarchical model neatly. A university where one student belongs to two departments does not, which is where the network model was used.",
        "quiz": [
            {
                "q": "Which model organises data as a tree where each child has exactly one parent?",
                "options": ["Network model", "Hierarchical model", "Relational model", "Entity relationship model"],
                "answer": 1,
                "why": "The hierarchical model is a tree of parent and child records with a single parent for each child.",
            },
            {
                "q": "Which model is drawn as a diagram of entities and relationships before implementation?",
                "options": ["Hierarchical model", "Network model", "Object relational model", "Entity relationship model"],
                "answer": 3,
                "why": "The ER model is the conceptual, diagrammatic model used at design time, before any table is created.",
            },
            {
                "q": "Why did the relational model replace the hierarchical and network models?",
                "options": ["Rows are linked by matching key values instead of pointers", "It stores data as a single tree", "It allows a child record to have several parents", "It uses classes and inheritance"],
                "answer": 0,
                "why": "Matching values in columns replace the pointers of the older models, so queries no longer have to follow links.",
            },
            {
                "q": "Which statement about data models is NOT correct?",
                "options": ["The network model uses sets and pointers", "The hierarchical model struggles with many to many data", "The ER model is implemented directly as the stored records", "Object relational models add inheritance to tables"],
                "answer": 2,
                "why": "The ER model is a conceptual design diagram, not a storage structure; it is mapped into tables later.",
            },
        ],
        "examTip": "Draw the three classic models side by side and name one structure each: tree, graph and table. Add the line that the ER model is conceptual.",
    },

    "CSCA413-MI-T03": {
        "explanation": "A DBMS is built in three levels so that a change in one place does not spread everywhere. The external or view level is what one user or one application sees. The conceptual level holds the logical design, the tables and the constraints for the whole organisation. The internal level describes how the records are actually laid out on disk. The database administrator, or DBA, owns the schema and the access rights, and four language groups let each role work at its own level.",
        "example": "A student sees only her own marks in the college portal, while the office sees every student's marks. Both are views over one conceptual table, and neither knows whether the file is hashed or indexed.",
        "quiz": [
            {
                "q": "Which level of the three schema architecture describes physical storage on disk?",
                "options": ["External level", "View level", "Conceptual level", "Internal level"],
                "answer": 3,
                "why": "The internal level is the physical schema, describing record layout, indexes and storage structures.",
            },
            {
                "q": "Which language group is used to grant and revoke privileges?",
                "options": ["DDL", "DML", "DCL", "TCL"],
                "answer": 2,
                "why": "DCL is the data control language used for GRANT and REVOKE; TCL carries COMMIT and ROLLBACK.",
            },
            {
                "q": "Who designs the schema and controls access in an organisation?",
                "options": ["End user", "Database administrator", "Application programmer", "System analyst"],
                "answer": 1,
                "why": "The DBA defines the schema, sets the access rights and looks after backup and recovery.",
            },
            {
                "q": "Which statement about DBMS architecture is NOT correct?",
                "options": ["Every user sees the whole conceptual schema", "Data abstraction hides storage detail from the user", "The external level holds individual user views", "DDL is used to define the schema"],
                "answer": 0,
                "why": "Abstraction means each user sees only their own view, never the entire conceptual schema.",
            },
        ],
        "examTip": "Sketch the three boxes external, conceptual and internal with the two mappings between them, and write one line on each level.",
    },

    "CSCA413-MI-T04": {
        "explanation": "Data independence is the reason a database can be changed without rewriting every program. Logical independence means the conceptual schema can change, for example by adding a column, while the existing views keep working. Physical independence means the storage can change, for example by adding an index, without touching the conceptual schema. Both work because each level is defined separately and a mapping connects it to the next. Physical independence is the easier of the two, because storage details are already hidden from the design.",
        "example": "The college adds an Aadhaar column to the student table. The existing report programs keep running, because their views still ask only for the old columns.",
        "quiz": [
            {
                "q": "Adding a new column to the conceptual schema without changing existing applications is an example of:",
                "options": ["Logical data independence", "Physical data independence", "Referential integrity", "Concurrency control"],
                "answer": 0,
                "why": "Logical independence protects external views and programs when the conceptual schema changes.",
            },
            {
                "q": "Adding an index to speed up searches without altering the table design is an example of:",
                "options": ["Logical data independence", "Physical data independence", "Both kinds acting together", "No independence, because the schema changed"],
                "answer": 1,
                "why": "Physical independence means changes at the internal level do not reach the conceptual schema.",
            },
            {
                "q": "How is data independence actually achieved?",
                "options": ["By storing every table in one file", "By giving every user a private copy of the data", "By keeping separate schema levels and mapping each to the next", "By rewriting the applications after every change"],
                "answer": 2,
                "why": "The mappings between the external, conceptual and internal levels are what absorb the change.",
            },
            {
                "q": "Which statement about data independence is NOT correct?",
                "options": ["A view can hide a newly added column from an old program", "Physical independence means storage changes do not reach the conceptual schema", "Separate schema levels with mappings make independence possible", "Logical independence means the internal file layout can change freely"],
                "answer": 3,
                "why": "Changing the internal file layout is physical independence; logical independence is about the conceptual schema.",
            },
        ],
        "examTip": "Write two definitions, one for each kind, with one example each: adding a column is logical, adding an index is physical.",
    },

    "CSCA413-MI-T05": {
        "explanation": "The ER model is drawn before any table exists. An entity is a real object such as one student, and an entity set is the collection of all students. Attributes describe an entity and may be simple, composite, single valued, multivalued, derived or a key. A relationship such as enrols links two entity sets. Cardinality says whether it is one to one, one to many, many to one or many to many. Participation says whether every entity must take part. An entity set with no key of its own is a weak entity set, identified through its owner and a partial key.",
        "example": "In a college, Student and Course are entity sets and Enrols is a many to many relationship between them. A fee receipt means nothing without the student it belongs to, so it is a weak entity set.",
        "quiz": [
            {
                "q": "In an ER diagram, which shape is used to show a relationship?",
                "options": ["Rectangle", "Ellipse", "Diamond", "Double line"],
                "answer": 2,
                "why": "Rectangles are entities, ellipses are attributes, diamonds are relationships and double lines show total participation.",
            },
            {
                "q": "A fee receipt cannot be identified without the student it belongs to. What is it called?",
                "options": ["A composite attribute", "A derived attribute", "A multivalued attribute", "A weak entity set"],
                "answer": 3,
                "why": "A weak entity set has no key of its own and is identified through its owner plus a partial key.",
            },
            {
                "q": "Which attribute type is calculated from another attribute rather than stored?",
                "options": ["Derived attribute", "Composite attribute", "Multivalued attribute", "Key attribute"],
                "answer": 0,
                "why": "Age worked out from a date of birth is the usual example; it is computed, not kept on disk.",
            },
            {
                "q": "Which statement about ER modelling is NOT correct?",
                "options": ["Total participation means every entity of the set takes part", "Degree is the number of attributes an entity has", "A foreign key links one entity set to another", "Cardinality may be one to one, one to many, many to one or many to many"],
                "answer": 1,
                "why": "Degree counts the entity sets taking part in a relationship, not the attributes of an entity.",
            },
        ],
        "examTip": "Practise the notation: rectangle, ellipse, diamond, double rectangle, double ellipse, double line. Most questions ask for a full ER diagram.",
    },

    "CSCA413-MI-T06": {
        "explanation": "Enhanced ER adds ideas from object oriented thinking to the plain ER diagram. Specialisation splits a superclass into subclasses, while generalisation does the reverse and combines similar entities. A subclass inherits every attribute of its superclass and adds its own. The splitting can be constrained as disjoint or overlapping, and as total or partial. Aggregation treats a whole relationship as one higher level entity so it can join another relationship. A category collects its members from several different superclasses.",
        "example": "In a college, Person generalises Student and Teacher, and Student specialises into Undergraduate and Postgraduate. A student who also works as a lab assistant belongs to two subclasses at once, which makes the specialisation overlapping.",
        "quiz": [
            {
                "q": "Combining several similar entity sets into one higher level entity set is called:",
                "options": ["Specialisation", "Generalisation", "Aggregation", "Categorisation"],
                "answer": 1,
                "why": "Generalisation works bottom up, while specialisation works top down from a superclass to its subclasses.",
            },
            {
                "q": "What does a subclass receive from its superclass?",
                "options": ["All of its attributes, through attribute inheritance", "Only the key attribute", "Nothing, because subclasses are independent", "Only the relationships, never the attributes"],
                "answer": 0,
                "why": "Attribute inheritance gives the subclass every superclass attribute plus whatever it adds itself.",
            },
            {
                "q": "Treating a relationship as a higher level entity so it can take part in another relationship is called:",
                "options": ["Specialisation", "Generalisation", "Union type", "Aggregation"],
                "answer": 3,
                "why": "Aggregation lets a relationship such as Enrols become an entity that can join another relationship.",
            },
            {
                "q": "Which statement about enhanced ER is NOT correct?",
                "options": ["A subclass may be constrained as disjoint or overlapping", "A category is a union type drawn with a circle marked U", "Specialisation requires every superclass entity to sit in some subclass", "Generalisation moves from several entity sets to one superclass"],
                "answer": 2,
                "why": "Requiring every entity to belong is the total constraint, which is optional; partial specialisation allows an entity in no subclass.",
            },
        ],
        "examTip": "Draw the superclass with the ISA triangle, mark disjoint or overlapping, mark total or partial, then add one example.",
    },

    "CSCA413-MII-T01": {
        "explanation": "The relational model keeps everything in one structure, the relation, which looks like a table. A tuple is one row, an attribute is one named column and a domain is the set of values that column may hold. Degree counts the attributes and cardinality counts the tuples. Keys identify rows: a super key is any unique set of attributes, and a candidate key is a minimal super key. One candidate key is chosen as the primary key, and a foreign key points at a primary key in another relation. Two rules guard the data: entity integrity forbids a null primary key, and referential integrity forbids a foreign key with no matching primary key.",
        "example": "A Student table with four columns has degree 4, and with 900 rows it has cardinality 900. RollNo is the primary key, and DeptID in the same table is a foreign key pointing at Department.",
        "quiz": [
            {
                "q": "What is the term for one row of a relation?",
                "options": ["Attribute", "Tuple", "Domain", "Degree"],
                "answer": 1,
                "why": "A tuple is a row, an attribute is a column and a domain is the set of allowed values.",
            },
            {
                "q": "A relation has 6 columns and 240 rows. What are its degree and cardinality?",
                "options": ["Degree 240, cardinality 6", "Degree 6, cardinality 240", "Degree 6, cardinality 6", "Degree 240, cardinality 240"],
                "answer": 1,
                "why": "Degree counts the attributes or columns, and cardinality counts the tuples or rows.",
            },
            {
                "q": "Which rule is broken when a row holds a foreign key value that no primary key contains?",
                "options": ["Entity integrity", "Referential integrity", "Domain constraint", "The Codd rule on nulls"],
                "answer": 1,
                "why": "Referential integrity requires every non null foreign key to match a primary key that exists.",
            },
            {
                "q": "Which statement about keys is NOT correct?",
                "options": ["A candidate key is a minimal super key", "A relation may have more than one candidate key", "A foreign key must be unique within its own table", "One candidate key is chosen as the primary key"],
                "answer": 2,
                "why": "A foreign key is often repeated, because many rows may point at the same parent row.",
            },
            {
                "q": "How many rules did E F Codd describe for a full relational DBMS?",
                "options": ["6", "9", "12", "15"],
                "answer": 2,
                "why": "Codd gave twelve rules, sometimes numbered from zero, that a relational system should satisfy.",
            },
        ],
        "examTip": "Start with relation, tuple, attribute and domain, then give degree and cardinality, then the two integrity rules. Marks are usually split this way.",
    },

    "CSCA413-MII-T02": {
        "explanation": "Relational algebra is procedural, which means a query says which operators to apply and in what order. Selection, written sigma, keeps the rows that satisfy a condition, and projection, written pi, keeps only the columns named. Union, intersection, set difference and Cartesian product combine two relations whose schemas match. A join puts matching rows from two relations together. A theta join allows any comparison, an equi join uses equality, and a natural join drops the duplicate column. Outer joins keep unmatched rows and pad the missing side with null. Division answers the all questions, such as students who took every course, and the rho operator renames relations or attributes.",
        "example": "To list the names of students in the CSE department, first select the rows where Dept equals CSE, then project the Name column. To find students who took every course, divide the enrolment table by the course table.",
        "quiz": [
            {
                "q": "Which operator keeps only the rows that satisfy a condition?",
                "options": ["Projection", "Selection", "Union", "Division"],
                "answer": 1,
                "why": "Selection, written sigma, filters rows, while projection, written pi, picks columns.",
            },
            {
                "q": "Which operator answers the question students who enrolled in every course?",
                "options": ["Natural join", "Cartesian product", "Division", "Set difference"],
                "answer": 2,
                "why": "Division returns the tuples that match every tuple of a second relation.",
            },
            {
                "q": "What does a natural join do that an equi join does not?",
                "options": ["It allows comparisons other than equality", "It removes the duplicate join column", "It keeps unmatched rows padded with null", "It requires the two schemas to be identical"],
                "answer": 1,
                "why": "Both match on equality, but the natural join shows the shared column only once.",
            },
            {
                "q": "Which statement about relational algebra is NOT correct?",
                "options": ["Every operator takes relations and returns a relation", "Set operations need the two relations to be union compatible", "Projection always increases the number of rows", "An outer join keeps unmatched rows with null padding"],
                "answer": 2,
                "why": "Projection can reduce the row count, because duplicate rows are removed once columns are dropped.",
            },
            {
                "q": "Which operator gives a name to a relation or to one of its attributes?",
                "options": ["Rho", "Sigma", "Pi", "Delta"],
                "answer": 0,
                "why": "Rho is the rename operator; sigma selects and pi projects.",
            },
        ],
        "examTip": "Write the symbol for each operator first, then one line on what it returns. Questions usually ask for an expression, so keep the order of operations visible.",
    },

    "CSCA413-MII-T03": {
        "explanation": "SQL is declarative, so a query describes the result wanted and the system decides how to fetch it. The language has four parts: DDL defines structures, DML reads and changes rows, DCL grants privileges and TCL commits or rolls back work. A basic query names the columns to return, the table to read and a WHERE condition. DISTINCT, ORDER BY, BETWEEN, IN and LIKE shape the result. Aggregates such as COUNT and SUM work on groups made by GROUP BY, and HAVING filters the groups themselves. Joins bring rows from two tables together, and a subquery is a SELECT inside another SELECT. A view stores the query itself and acts as a virtual table for the user.",
        "example": "To find departments with more than 60 students, group by DeptID and count the rows. Put the condition on the count in HAVING, not in WHERE.",
        "quiz": [
            {
                "q": "Which clause filters the groups produced by GROUP BY?",
                "options": ["WHERE", "HAVING", "ORDER BY", "DISTINCT"],
                "answer": 1,
                "why": "WHERE filters individual rows before grouping, and HAVING filters the groups after counting.",
            },
            {
                "q": "GRANT and REVOKE belong to which part of SQL?",
                "options": ["DDL", "DML", "DCL", "TCL"],
                "answer": 2,
                "why": "DCL is the data control language; TCL holds COMMIT, ROLLBACK and SAVEPOINT.",
            },
            {
                "q": "Which statement about SQL is NOT correct?",
                "options": ["A view stores the query, not a separate copy of the rows", "HAVING is applied after GROUP BY", "WHERE is applied before any grouping takes place", "A subquery may appear only in the SELECT clause"],
                "answer": 3,
                "why": "A subquery can appear in SELECT, FROM, WHERE and HAVING clauses, and with EXISTS, ANY and ALL.",
            },
            {
                "q": "A report must list every department and show null where a department has no students. Which join is needed?",
                "options": ["Inner join", "Left outer join", "Right outer join", "Natural join"],
                "answer": 1,
                "why": "A left outer join keeps every row of the left table and pads the missing right side with null.",
            },
            {
                "q": "Which keyword removes duplicate rows from a result?",
                "options": ["UNIQUE", "DISTINCT", "ORDER BY", "DEFAULT"],
                "answer": 1,
                "why": "DISTINCT removes repeated rows from the result; UNIQUE is a constraint written on a column.",
            },
        ],
        "examTip": "For a query question, write the SELECT and FROM line first, then WHERE, then GROUP BY and HAVING, then ORDER BY. Note that HAVING needs GROUP BY.",
    },

    "CSCA413-MII-T04": {
        "explanation": "Relational calculus is non procedural, so a query states the condition the answer must satisfy instead of listing operators. Tuple relational calculus asks for the set of tuples t for which a predicate is true, written as t such that P of t. Domain relational calculus does the same by naming the domain variables for the columns and putting conditions on them. Both are equal in expressive power to relational algebra, so anything written in one can be written in the other. Safe expressions are required, because an unsafe one can produce an infinite set of tuples.",
        "example": "Ask for every student whose department is CSE, rather than saying filter the file and then pick the name column. The system chooses the operators itself.",
        "quiz": [
            {
                "q": "What kind of language is relational calculus?",
                "options": ["Procedural", "Non procedural", "Imperative", "Object oriented"],
                "answer": 1,
                "why": "It says what is wanted; relational algebra says which operators to apply and in what order.",
            },
            {
                "q": "Tuple relational calculus is written in which form?",
                "options": ["Pi followed by sigma", "t such that P of t", "SELECT FROM WHERE", "X determines Y"],
                "answer": 1,
                "why": "The result is the set of tuples t for which the predicate P is true.",
            },
            {
                "q": "Which statement about the two calculi is NOT correct?",
                "options": ["Tuple calculus and domain calculus have the same expressive power", "Both are equivalent in power to relational algebra", "An unsafe expression can return an infinite set of tuples", "A calculus query must list the operators used to reach the answer"],
                "answer": 3,
                "why": "Listing the operators is what relational algebra does; calculus states only the condition.",
            },
            {
                "q": "Why is the safety condition imposed on calculus expressions?",
                "options": ["To make the query run faster", "To stop the result from being an infinite set", "To allow null values in the answer", "To force the use of an index"],
                "answer": 1,
                "why": "A safe expression can only draw values from the database or from the constants written in it.",
            },
        ],
        "examTip": "Contrast the two in one table: algebra is procedural with operators, calculus is declarative with predicates. Add that both have equal expressive power.",
    },

    "CSCA413-MII-T05": {
        "explanation": "Every commercial system implements standard SQL and then adds its own extensions on top. Oracle and SQL Server are enterprise products with the PL/SQL and T-SQL procedural languages and a wide set of administration tools. MySQL and PostgreSQL are open source; MySQL is common behind web applications and PostgreSQL is known for following the standards closely. Choosing between them means comparing storage limits, concurrency control, recovery, partitioning, security, replication and licence cost. DB2 is IBM's system and is found mostly in large established installations.",
        "example": "A startup building a web application with no licence budget usually starts on MySQL or PostgreSQL. A bank replacing a mainframe system pays for Oracle or DB2 and expects the administration tools that come with it.",
        "quiz": [
            {
                "q": "Which procedural language belongs to Oracle?",
                "options": ["T-SQL", "PL/SQL", "PL/pgSQL", "Transact SQL"],
                "answer": 1,
                "why": "Oracle uses PL/SQL, while SQL Server uses T-SQL.",
            },
            {
                "q": "Which two of these systems are open source?",
                "options": ["Oracle and DB2", "SQL Server and Oracle", "MySQL and PostgreSQL", "DB2 and MySQL"],
                "answer": 2,
                "why": "MySQL and PostgreSQL are the widely used open source systems; the others carry licence costs.",
            },
            {
                "q": "Which statement about choosing an RDBMS is NOT correct?",
                "options": ["Licence cost is one of the features compared", "Replication and partitioning affect the choice", "Recovery and concurrency control affect the choice", "Every system behaves identically because all of them implement SQL"],
                "answer": 3,
                "why": "Vendor extensions, storage limits and administration tools differ, so the systems are not interchangeable in practice.",
            },
            {
                "q": "A team needs a standards compliant open source database for a college project with no budget. Which fits best?",
                "options": ["Oracle", "DB2", "PostgreSQL", "SQL Server"],
                "answer": 2,
                "why": "PostgreSQL is open source and is known for following the standards closely.",
            },
        ],
        "examTip": "Answer comparison questions with a table: system, vendor, licence, procedural language and one typical use.",
    },

    "CSCA413-MII-T06": {
        "explanation": "A functional dependency says that if two rows agree on X, they must also agree on Y, written X arrow Y. Finding the dependencies in a table shows where the same fact is stored more than once. A partial dependency uses only part of a composite key, and a transitive dependency reaches a non key attribute through another non key attribute. Armstrong's axioms of reflexivity, augmentation and transitivity generate every dependency that follows from a given set. The closure of an attribute set is everything it determines, and a minimal set whose closure covers the whole relation is a candidate key. Splitting a table is called decomposition, and a good one keeps the join lossless and the dependencies preserved.",
        "example": "In a table holding RollNo, StudentName and DeptHead, RollNo determines StudentName and DeptHead. RollNo also determines Dept, and Dept determines DeptHead, so DeptHead is transitively dependent on the key.",
        "quiz": [
            {
                "q": "What does the functional dependency X arrow Y mean?",
                "options": ["X and Y must always hold the same value", "Any two rows agreeing on X must also agree on Y", "Y determines X", "X and Y together form the primary key"],
                "answer": 1,
                "why": "The left side fixes the right side, so two rows with the same X cannot carry different Y values.",
            },
            {
                "q": "Which of these is a derived rule rather than one of Armstrong's basic axioms?",
                "options": ["Reflexivity", "Augmentation", "Transitivity", "Pseudotransitivity"],
                "answer": 3,
                "why": "Union, decomposition and pseudotransitivity are proved from the three basic axioms.",
            },
            {
                "q": "Which statement about dependencies is NOT correct?",
                "options": ["A partial dependency depends on part of a composite key", "A transitive dependency passes through a non key attribute", "The closure of a set is everything that set determines", "A candidate key must contain every attribute of the relation"],
                "answer": 3,
                "why": "A candidate key is a minimal attribute set whose closure covers the whole relation, not the relation itself.",
            },
            {
                "q": "A table is split into two. Which property says that joining them back returns exactly the original rows?",
                "options": ["Dependency preservation", "Lossless join", "Canonical cover", "Attribute closure"],
                "answer": 1,
                "why": "A lossless decomposition guarantees that no spurious rows appear when the tables are joined again.",
            },
            {
                "q": "What is a canonical cover?",
                "options": ["A cover containing every possible dependency", "A minimal equivalent set of dependencies with nothing redundant", "The set of all candidate keys", "A decomposition with no transitive dependency"],
                "answer": 1,
                "why": "Extraneous attributes and redundant dependencies are removed, but the closure stays the same.",
            },
        ],
        "examTip": "List the dependencies, compute each closure, mark the candidate key, then name the dependency that breaks 2NF or 3NF.",
    },

    "CSCA413-MII-T07": {
        "explanation": "A table that is not normalised repeats the same fact in many rows, which causes insertion, update and deletion anomalies. First normal form requires every attribute to hold one atomic value, so no repeating groups or multivalued cells. Second normal form removes partial dependencies on part of a composite key, and third normal form removes transitive dependencies on the key. BCNF is stricter: for every non trivial dependency, the left side must be a super key. Fourth normal form removes multivalued dependencies, fifth normal form removes join dependencies, and denormalisation deliberately steps back to make reporting faster.",
        "example": "A row storing CSE and IT together in one Department column is not in first normal form. Splitting it into two rows fixes the cell and makes counting departments possible.",
        "quiz": [
            {
                "q": "Which normal form requires every attribute to hold a single atomic value?",
                "options": ["1NF", "2NF", "3NF", "BCNF"],
                "answer": 0,
                "why": "First normal form removes repeating groups and multivalued attributes.",
            },
            {
                "q": "A relation is in 1NF and has no partial dependency on part of a candidate key. Which form is it in?",
                "options": ["1NF", "2NF", "3NF", "BCNF"],
                "answer": 1,
                "why": "Removing partial dependencies on a composite key is exactly the step from 1NF to 2NF.",
            },
            {
                "q": "How does BCNF differ from 3NF?",
                "options": ["BCNF allows transitive dependencies that 3NF forbids", "BCNF requires the left side of every dependency to be a super key", "BCNF applies only to single attribute keys", "BCNF is a weaker form than 3NF"],
                "answer": 1,
                "why": "That single condition makes BCNF stricter, and some relations in 3NF still fail it.",
            },
            {
                "q": "Which statement about normalisation is NOT correct?",
                "options": ["Denormalisation is sometimes chosen to speed up reporting", "Higher normal forms reduce redundancy and anomalies", "A relation in 4NF is free of multivalued dependencies", "A relation in 3NF is always in BCNF as well"],
                "answer": 3,
                "why": "BCNF is stricter than 3NF, so there are relations in 3NF that still violate BCNF.",
            },
            {
                "q": "Which of these is NOT one of the three classic update anomalies?",
                "options": ["Insertion anomaly", "Deletion anomaly", "Update anomaly", "Concurrency anomaly"],
                "answer": 3,
                "why": "Insertion, deletion and update anomalies come from redundancy; concurrency is handled by transaction control.",
            },
        ],
        "examTip": "Give one line per form: 1NF atomic, 2NF no partial, 3NF no transitive, BCNF super key.",
    },

    "CSCA413-MII-T08": {
        "explanation": "A query passes through several steps before a single row is read. The parser checks the syntax and the validator checks that the tables and columns exist. The translator then turns the statement into a relational algebra expression. The optimiser compares equivalent expressions and access paths and picks the cheapest plan it can find. Cost is estimated mainly in block transfers and disk seeks. The estimate uses statistics such as the number of tuples, the blocking factor and the selectivity of a condition. Simple heuristics help too: push selections down before joins, and do the most restrictive operation first.",
        "example": "A selection that keeps 5 rows out of 100,000 should run before the join, not after it. Pushing it down means the join works on 5 rows instead of 100,000.",
        "quiz": [
            {
                "q": "Which step checks that the tables and columns named in a query really exist?",
                "options": ["Parsing", "Validation", "Optimisation", "Execution"],
                "answer": 1,
                "why": "Validation checks the query against the catalogue, after the syntax has been accepted.",
            },
            {
                "q": "What is query cost usually measured in?",
                "options": ["Lines of SQL and number of joins", "Block transfers and disk seeks", "Processor clock speed only", "Number of users connected"],
                "answer": 1,
                "why": "Disk access dominates query time, so the estimate counts blocks moved and seeks performed.",
            },
            {
                "q": "Which heuristic rule helps most when optimising by hand?",
                "options": ["Perform joins before selections", "Perform selections and projections as early as possible", "Sort every table before reading it", "Read the largest table first"],
                "answer": 1,
                "why": "Pushing selections and projections down shrinks the data before the expensive join runs.",
            },
            {
                "q": "Which statement about query processing is NOT correct?",
                "options": ["The translator produces a relational algebra expression", "The optimiser compares several equivalent plans", "Selectivity helps estimate how many rows a condition returns", "The optimiser always finds the cheapest possible plan"],
                "answer": 3,
                "why": "Optimisers search a limited space of plans, so they aim for a good plan rather than a guaranteed best one.",
            },
        ],
        "examTip": "Draw the pipeline as parse, validate, translate, optimise, execute, and add the note that cost means block transfers plus seeks.",
    },
}
