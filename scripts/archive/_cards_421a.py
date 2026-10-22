# CSCA 421 Computer Networks - Module I
# Introduction, reference models, the physical layer and transmission media.

CODE = "CSCA421"

CARDS = {
    "CSCA421-MI-T01": {
        "explanation": "Topology is the arrangement of the nodes and links in a network, and it decides how a failure spreads. In a bus all nodes share one backbone cable, so one break stops the whole network while the cabling stays cheap. In a star every node runs to a central hub or switch, so a broken cable takes out one node only. In a ring the nodes form a closed loop with data circulating one way, often controlled by a token. In a mesh every node links to every other, which gives the best reliability and the highest cabling cost.",
        "example": "A college lab wired in a star keeps working when one cable is unplugged, because only that machine drops off. The same lab on a bus would lose every machine at once.",
        "quiz": [
            {
                "q": "Which topology connects every node to a central hub or switch?",
                "options": ["Bus", "Star", "Ring", "Mesh"],
                "answer": 1,
                "why": "In a star each node has its own cable to the centre, so one cable failure affects only that node.",
            },
            {
                "q": "Which topology gives the highest reliability and the highest cabling cost?",
                "options": ["Bus", "Star", "Ring", "Mesh"],
                "answer": 3,
                "why": "Full mesh links every node to every other, so there are many paths but also many cables.",
            },
            {
                "q": "Which statement about topologies is NOT correct?",
                "options": ["A bus shares one backbone cable among all the nodes", "A ring passes data in one direction around a loop", "A star isolates a failure to a single cable", "A mesh is the cheapest topology to install"],
                "answer": 3,
                "why": "Mesh is the most expensive, because every node needs a link to every other node.",
            },
            {
                "q": "A lab loses the whole network when one cable breaks. Which topology is it?",
                "options": ["Star", "Bus", "Mesh", "Tree"],
                "answer": 1,
                "why": "A shared backbone is the single point of failure in a bus, which is its main weakness.",
            },
            {
                "q": "A network covering a city is classified as a:",
                "options": ["LAN", "MAN", "WAN", "PAN"],
                "answer": 1,
                "why": "Reach sets the class: a room or building is a LAN, a city a MAN, and a country a WAN.",
            },
        ],
        "examTip": "Draw bus, star, ring and mesh in one row, with one advantage and one disadvantage under each.",
    },

    "CSCA421-MI-T02": {
        "explanation": "Network architecture is the plan for who does what in a communication system. In the client server model a server offers a service such as web or mail, and clients ask for it. In the peer to peer model every machine can be both, which suits small networks with no central machine. Layering is the other big idea. Each layer offers services to the layer above and uses the one below, and the rules they follow are protocols. Services come in two flavours: connection oriented, which sets up a path and keeps the order, and connectionless, which sends independent packets.",
        "example": "Opening a college website is client server, because your browser asks and the server answers. Sharing files between two laptops with no server is peer to peer.",
        "quiz": [
            {
                "q": "In which model can every machine act as both client and server?",
                "options": ["Client server", "Peer to peer", "Layered", "Connection oriented"],
                "answer": 1,
                "why": "Peer to peer has no central server, so each machine takes both roles.",
            },
            {
                "q": "What are the rules that two layers follow to talk to each other called?",
                "options": ["A service", "A protocol", "An interface", "A topology"],
                "answer": 1,
                "why": "A protocol is the agreed set of formats and rules; the service is what the layer provides.",
            },
            {
                "q": "Which statement about services is NOT correct?",
                "options": ["A connection oriented service keeps the order of the data", "A connectionless service sends each packet independently", "A connection oriented service sets up a path first", "A connectionless service guarantees delivery and order"],
                "answer": 3,
                "why": "Guaranteeing delivery and order is exactly what a connection oriented service adds.",
            },
            {
                "q": "Which statement about layering is NOT correct?",
                "options": ["Each layer uses the services of the layer below", "Each layer offers services to the layer above", "Layers on two machines talk to each other through a protocol", "Every layer must know how the layer below is implemented"],
                "answer": 3,
                "why": "Layering hides the implementation, so a layer needs only the service, not the code below it.",
            },
        ],
        "examTip": "Contrast client server and peer to peer, then define a protocol and give the two service types with an example each.",
    },

    "CSCA421-MI-T03": {
        "explanation": "The OSI model splits networking into seven layers: physical, data link, network, transport, session, presentation and application. The TCP/IP model uses four: network access, internet, transport and application. OSI separates session and presentation, while TCP/IP folds both into the application layer. TCP/IP is what the Internet really runs. Data passes down one stack and up the other, and each layer adds a header on the way down. That wrapping is called encapsulation, and removing it on the way up is de-encapsulation.",
        "example": "An email leaves your machine as application data, then gains a TCP header, an IP header and an Ethernet header. The receiving machine strips them in the reverse order.",
        "quiz": [
            {
                "q": "How many layers does the OSI model have?",
                "options": ["4", "5", "7", "6"],
                "answer": 2,
                "why": "Physical, data link, network, transport, session, presentation and application make seven.",
            },
            {
                "q": "Which two OSI layers does the TCP/IP model fold into its application layer?",
                "options": ["Network and transport", "Session and presentation", "Physical and data link", "Transport and session"],
                "answer": 1,
                "why": "The TCP/IP application layer covers what OSI splits into application, presentation and session.",
            },
            {
                "q": "Which statement about the models is NOT correct?",
                "options": ["OSI has seven layers", "TCP/IP is what the Internet actually uses", "OSI is mainly a teaching reference", "TCP/IP has a separate presentation layer"],
                "answer": 3,
                "why": "The presentation and session duties sit inside the TCP/IP application layer, not in their own layer.",
            },
            {
                "q": "What is it called when each layer adds its own header on the way down?",
                "options": ["Fragmentation", "Encapsulation", "Multiplexing", "Switching"],
                "answer": 1,
                "why": "Encapsulation wraps the data at each layer, and de-encapsulation unwraps it at the receiver.",
            },
            {
                "q": "The data unit at the transport layer in TCP/IP is called a:",
                "options": ["Frame", "Segment", "Datagram", "Bit"],
                "answer": 1,
                "why": "TCP produces segments, IP produces datagrams and the data link layer produces frames.",
            },
        ],
        "examTip": "Write the seven OSI layers in order with a one line duty each, then place the four TCP/IP layers beside them.",
    },

    "CSCA421-MI-T04": {
        "explanation": "The Internet grew out of two research networks. ARPANET began in 1969 for US defence research and introduced packet switching along with the first host protocols. NSFNET followed in the 1980s as an academic backbone, opening the network to universities and later to commercial traffic. Today the Internet is a network of networks running TCP/IP, held together by ISPs, exchange points and standard bodies such as IETF and ICANN. Alongside it sit the telephone network, cable and mobile networks, and the private intranets of companies.",
        "example": "A student in Chidambaram reaches a server in another country through a chain of ISPs meeting at an exchange point. No single network carries the whole path.",
        "quiz": [
            {
                "q": "Which network introduced packet switching in 1969?",
                "options": ["NSFNET", "ARPANET", "The telephone network", "Ethernet"],
                "answer": 1,
                "why": "ARPANET was the US defence research network that first put packet switching to work.",
            },
            {
                "q": "What was NSFNET?",
                "options": ["A commercial ISP", "A US academic backbone from the 1980s", "A wireless standard", "An email protocol"],
                "answer": 1,
                "why": "NSFNET connected universities and later allowed commercial traffic, which led to today's Internet.",
            },
            {
                "q": "Which statement about the Internet is NOT correct?",
                "options": ["It is a network of networks", "It runs on TCP/IP", "A single organisation owns the whole of it", "ISPs and exchange points connect its parts"],
                "answer": 2,
                "why": "Nobody owns the Internet; IETF and ICANN coordinate standards and names instead.",
            },
            {
                "q": "Which body coordinates Internet standards?",
                "options": ["IEEE alone", "IETF", "ISO alone", "ITU alone"],
                "answer": 1,
                "why": "The IETF publishes the request for comments documents that define Internet standards.",
            },
        ],
        "examTip": "Give one line each on ARPANET, NSFNET and the Internet, with a year for the first two.",
    },

    "CSCA421-MI-T05": {
        "explanation": "The physical layer carries raw bits across a link and defines the voltages, the timings, the data rate and the shape of the connector. Bandwidth is the capacity of the link, data rate is the bits per second achieved and latency is the delay a signal suffers. Transmission may be simplex in one direction only, half duplex alternating, or full duplex both ways at once. Three switching methods exist: circuit switching reserves a path, message switching stores and forwards whole messages, and packet switching forwards small packets. Signals weaken with distance through attenuation, distortion and noise.",
        "example": "A phone call on the old telephone network reserved a path for the whole conversation. A video call today sends packets that share the link with everyone else's traffic.",
        "quiz": [
            {
                "q": "Which switching method reserves a path for the whole conversation?",
                "options": ["Packet switching", "Message switching", "Circuit switching", "Store and forward"],
                "answer": 2,
                "why": "Circuit switching sets up and holds a path, which is how the telephone network worked.",
            },
            {
                "q": "Which transmission mode sends in both directions at the same time?",
                "options": ["Simplex", "Half duplex", "Full duplex", "Multiplex"],
                "answer": 2,
                "why": "Full duplex carries traffic both ways at once, while half duplex has to take turns.",
            },
            {
                "q": "Which statement about the physical layer is NOT correct?",
                "options": ["It defines voltages and connectors", "Bandwidth is the capacity of the link", "Latency is the delay a signal suffers", "It decides the route a packet takes across the Internet"],
                "answer": 3,
                "why": "Choosing a route is the network layer's job; the physical layer only moves bits across one link.",
            },
            {
                "q": "Which of these is NOT a transmission impairment?",
                "options": ["Attenuation", "Distortion", "Noise", "Encapsulation"],
                "answer": 3,
                "why": "Attenuation, distortion and noise degrade the signal, while encapsulation is a layering action.",
            },
            {
                "q": "Sharing one medium among several signals by splitting it into frequency bands is called:",
                "options": ["FDM", "TDM", "Circuit switching", "Flooding"],
                "answer": 0,
                "why": "Frequency division multiplexing splits by frequency, while time division splits by time slots.",
            },
        ],
        "examTip": "List the physical layer duties, define bandwidth and latency, then give the three switching methods in one line each.",
    },

    "CSCA421-MI-T06": {
        "explanation": "Transmission media are the paths a signal travels along, either guided inside a cable or unguided through the air. Twisted pair is two insulated copper wires twisted together; it is cheap and easy to install but picks up interference. Coaxial cable adds a braided shield around the conductor, which raises the bandwidth and blocks noise better. Optical fibre carries light in a glass core, giving very high bandwidth, low attenuation and complete immunity to electrical interference. Radio, microwave, infrared and satellite links are unguided, and each trades coverage against weather, obstacles and delay.",
        "example": "A hostel floor wired with twisted pair is cheap and quick to install. The link between two campus buildings uses fibre, because it carries more and ignores the electrical noise near the power lines.",
        "quiz": [
            {
                "q": "Which medium carries light in a glass core?",
                "options": ["Twisted pair", "Coaxial cable", "Optical fibre", "Radio wave"],
                "answer": 2,
                "why": "Optical fibre uses light, which gives high bandwidth and immunity to electrical interference.",
            },
            {
                "q": "Which statement about transmission media is NOT correct?",
                "options": ["Twisted pair is cheap and easy to install", "Coaxial cable has better noise immunity than twisted pair", "Fibre suffers badly from electromagnetic interference", "Satellite links cover wide areas but add delay"],
                "answer": 2,
                "why": "Fibre is immune to electromagnetic interference, which is one of its main advantages.",
            },
            {
                "q": "Which medium is unguided?",
                "options": ["Twisted pair", "Coaxial cable", "Optical fibre", "Microwave"],
                "answer": 3,
                "why": "Guided media confine the signal to a cable, while microwave travels through free space.",
            },
            {
                "q": "Satellite links are known for:",
                "options": ["Very low delay", "Wide coverage with higher delay", "Immunity to weather", "Zero cost"],
                "answer": 1,
                "why": "The signal travels a long way up and back, which adds delay even though coverage is wide.",
            },
            {
                "q": "Why does coaxial cable resist noise better than twisted pair?",
                "options": ["It uses thicker copper", "It has a braided shield around the conductor", "It carries light instead of electricity", "It is always shorter"],
                "answer": 1,
                "why": "The shield blocks outside interference, which is what gives coaxial cable its better noise immunity.",
            },
        ],
        "examTip": "Draw a table of the media with the columns type, guided or not, bandwidth, distance and one weakness.",
    },
}
