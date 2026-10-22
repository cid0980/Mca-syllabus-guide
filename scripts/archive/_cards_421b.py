# CSCA 421 Computer Networks - Modules II and III
# The data link layer and the network layer.

CODE = "CSCA421"

CARDS = {
    "CSCA421-MII-T01": {
        "explanation": "The data link layer takes the raw bit stream of the physical layer and turns it into a reliable link between two neighbours. The first job is framing: marking where one frame starts and the next ends. The methods are a character count, flag bytes with stuffing, or a physical layer coding violation. Error control adds acknowledgements, timers and retransmission so damaged frames are noticed and sent again. Flow control stops a fast sender from drowning a slow receiver. Link management sets up and releases the link, and addressing names the two ends with physical addresses.",
        "example": "A flag byte marks the start and end of each frame. If that byte appears inside the data, the sender inserts an escape byte, which is called byte stuffing.",
        "quiz": [
            {
                "q": "What is the job of marking where a frame starts and ends called?",
                "options": ["Framing", "Routing", "Multiplexing", "Switching"],
                "answer": 0,
                "why": "Framing turns the raw bit stream into units the receiver can recognise and check.",
            },
            {
                "q": "What does flow control prevent?",
                "options": ["Frames being damaged in transit", "A fast sender overwhelming a slow receiver", "The wrong route being chosen", "Two stations transmitting together"],
                "answer": 1,
                "why": "Flow control matches the sending rate to what the receiver can absorb.",
            },
            {
                "q": "Which statement about the data link layer is NOT correct?",
                "options": ["It delivers frames between two adjacent nodes", "Framing can use flag bytes with stuffing", "Error control uses acknowledgements and timers", "It chooses the route across the whole Internet"],
                "answer": 3,
                "why": "Routing across networks belongs to the network layer, not to the link between two neighbours.",
            },
            {
                "q": "Which technique inserts an escape byte so a flag inside the data is not read as a frame boundary?",
                "options": ["Bit stuffing", "Byte stuffing", "Checksumming", "Piggybacking"],
                "answer": 1,
                "why": "Byte stuffing works on characters, while bit stuffing inserts a zero after a run of ones.",
            },
            {
                "q": "Which addresses does the data link layer use to identify the two ends of a link?",
                "options": ["IP addresses", "Port numbers", "MAC addresses", "Domain names"],
                "answer": 2,
                "why": "Physical or MAC addresses identify devices on one link, and they stay local to that link.",
            },
        ],
        "examTip": "Name the four jobs framing, error control, flow control and link management, with one method under each.",
    },

    "CSCA421-MII-T02": {
        "explanation": "A frame can arrive damaged, so extra bits are added to catch the damage. A single bit error flips one bit, while a burst error damages a run of consecutive bits. A parity bit makes the number of ones even or odd, which is cheap but misses two bit errors. Two dimensional parity checks rows and columns, so it can locate and fix a single error. A checksum adds the data words and appends the total; CRC treats the frame as a polynomial and appends a division remainder. Hamming code places check bits at power of two positions so a single error can be corrected.",
        "example": "With even parity the byte 1010 0001 gets a 0 appended, because it already holds two ones. If one bit flips in transit the parity fails and the frame is discarded.",
        "quiz": [
            {
                "q": "Which method treats the frame as a polynomial and appends the remainder of a division?",
                "options": ["Parity check", "Checksum", "CRC", "Hamming code"],
                "answer": 2,
                "why": "CRC divides by a generator polynomial, catching far more error patterns than a checksum.",
            },
            {
                "q": "Where does Hamming code place its check bits?",
                "options": ["At the end of the frame", "At power of two positions", "Before every data byte", "In a separate frame"],
                "answer": 1,
                "why": "Those positions let the receiver add up the failing checks and point at the bad bit.",
            },
            {
                "q": "Which statement about error methods is NOT correct?",
                "options": ["Simple parity can miss a two bit error", "A checksum adds the data words", "Hamming code can correct a single bit error", "CRC is weaker than a simple parity check"],
                "answer": 3,
                "why": "CRC is much stronger than parity, which is why Ethernet and disk systems rely on it.",
            },
            {
                "q": "What decides how many errors a code can detect or correct?",
                "options": ["The frame length", "The minimum Hamming distance between valid codewords", "The number of parity bits alone", "The transmission medium"],
                "answer": 1,
                "why": "A minimum distance of d detects d minus 1 errors and corrects about half that many.",
            },
            {
                "q": "An error that damages a run of consecutive bits is called:",
                "options": ["A single bit error", "A burst error", "A parity error", "A lost frame"],
                "answer": 1,
                "why": "Burst errors are common on real links, which is why CRC is designed to catch them.",
            },
        ],
        "examTip": "List parity, checksum, CRC and Hamming with one line each on what they catch and what they miss.",
    },

    "CSCA421-MII-T03": {
        "explanation": "The elementary protocols build reliability one step at a time. The unrestricted simplex protocol assumes a perfect channel, so the sender transmits endlessly with no flow control. Stop and wait sends one frame and waits for its acknowledgement before sending the next, which solves flow control at the cost of throughput. For a noisy channel the frames are numbered, and a timeout or a negative acknowledgement triggers a retransmission. Piggybacking saves bandwidth by attaching the acknowledgement to a data frame going the other way.",
        "example": "Two students passing notes: stop and wait means one waits for a nod before the next note. Piggybacking means the nod rides back on the reply note instead of travelling alone.",
        "quiz": [
            {
                "q": "Which protocol sends one frame and waits for its acknowledgement before the next?",
                "options": ["Unrestricted simplex", "Stop and wait", "Go Back N", "Selective Repeat"],
                "answer": 1,
                "why": "Stop and wait keeps one frame outstanding, which is safe but leaves the link idle.",
            },
            {
                "q": "What does piggybacking do?",
                "options": ["Sends two frames at once", "Attaches an acknowledgement to a data frame going back", "Retransmits a lost frame", "Numbers the frames"],
                "answer": 1,
                "why": "It avoids a separate acknowledgement frame, which saves bandwidth on both directions.",
            },
            {
                "q": "Which statement about the elementary protocols is NOT correct?",
                "options": ["The unrestricted simplex protocol assumes a perfect channel", "Stop and wait solves flow control", "A noisy channel needs sequence numbers and timers", "Piggybacking increases the number of frames on the link"],
                "answer": 3,
                "why": "Piggybacking reduces the frame count by combining the acknowledgement with outgoing data.",
            },
            {
                "q": "Which mechanism tells the sender that a frame was lost on a noisy channel?",
                "options": ["A piggyback", "A timeout", "A parity bit", "A routing table"],
                "answer": 1,
                "why": "If no acknowledgement arrives before the timer expires, the sender sends the frame again.",
            },
            {
                "q": "What is the main weakness of stop and wait?",
                "options": ["It is too complex to implement", "The link sits idle while the sender waits", "It never detects errors", "It needs no sequence numbers"],
                "answer": 1,
                "why": "Only one frame is outstanding, so on a long delay path most of the capacity is wasted.",
            },
        ],
        "examTip": "Describe the four protocols as a ladder, saying what each one adds, and end with why piggybacking helps.",
    },

    "CSCA421-MII-T04": {
        "explanation": "Stop and wait wastes a long delay link, so sliding window protocols keep several frames outstanding at once. Each side keeps a window of sequence numbers, and the window slides forward as acknowledgements arrive. A one bit window is really stop and wait with numbered frames. Go Back N lets the receiver discard out of order frames and makes the sender resend the whole window from the lost frame. Selective Repeat buffers the correct frames at the receiver and resends only the missing ones, which is efficient but needs more memory and logic.",
        "example": "On a satellite link the round trip is long, so a window of one frame wastes almost all the capacity. A window of dozens of frames keeps the pipe full while the acknowledgements travel.",
        "quiz": [
            {
                "q": "What does Go Back N do when a frame is lost?",
                "options": ["Resends only that frame", "Resends that frame and every frame sent after it", "Waits for the receiver to ask", "Closes the connection"],
                "answer": 1,
                "why": "The receiver discards anything out of order, so the sender must go back to the lost frame.",
            },
            {
                "q": "How does Selective Repeat differ from Go Back N?",
                "options": ["It never retransmits", "It buffers correct frames and resends only the missing ones", "It uses no sequence numbers", "It works only on wireless links"],
                "answer": 1,
                "why": "Buffering correct frames avoids resending work that already arrived, but costs more memory.",
            },
            {
                "q": "Which statement about sliding windows is NOT correct?",
                "options": ["The window slides forward as acknowledgements arrive", "A larger window keeps a long delay link busier", "A one bit window behaves like stop and wait", "The window size can be chosen without regard to the delay"],
                "answer": 3,
                "why": "The window must cover the bandwidth-delay product, or the link runs partly idle.",
            },
            {
                "q": "With a window size of 7, how many sequence numbers does Selective Repeat need at least?",
                "options": ["7", "8", "14", "16"],
                "answer": 2,
                "why": "Selective Repeat needs at least twice the window size, so 14, to keep numbers unambiguous.",
            },
            {
                "q": "Why does a large window improve utilisation?",
                "options": ["It makes each frame smaller", "It keeps more frames in flight while waiting for acknowledgements", "It removes the need for timers", "It reduces the error rate"],
                "answer": 1,
                "why": "More frames in flight means the link keeps carrying data instead of waiting idle.",
            },
        ],
        "examTip": "Draw the sender window sliding, then contrast Go Back N with Selective Repeat in two lines each.",
    },

    "CSCA421-MII-T05": {
        "explanation": "A protocol that looks correct in the common cases can still fail in a rare interleaving, so it is checked formally. The finite state machine model draws each side as states and transitions, then builds the combined machine and searches it for deadlock or unspecified states. A Petri net models the flow of tokens, where tokens stand for messages and states. Channels can be modelled as bounded queues, which exposes what happens when a queue overflows or a frame is lost. The point is to find the rare sequence that a test would never hit.",
        "example": "Two machines may both decide to open a connection at the same moment. Testing may never produce that timing, but a state machine search reaches it and shows what the protocol does there.",
        "quiz": [
            {
                "q": "What does the finite state machine model search for?",
                "options": ["The fastest route", "Deadlock and unspecified states", "The cheapest cable", "The error rate"],
                "answer": 1,
                "why": "Reachable states where the protocol has no defined next move are exactly the bugs worth finding.",
            },
            {
                "q": "What do tokens represent in a Petri net model of a protocol?",
                "options": ["Routers", "Messages and states", "Cables", "Error bits"],
                "answer": 1,
                "why": "Tokens move through places and transitions, modelling how messages and states change.",
            },
            {
                "q": "Which statement about protocol verification is NOT correct?",
                "options": ["It checks rare interleavings that testing may miss", "Bounded queue models expose overflow behaviour", "Petri nets model the flow of messages and states", "Testing every case by hand is enough for a real protocol"],
                "answer": 3,
                "why": "The number of interleavings grows too fast for hand testing, which is why formal models are used.",
            },
            {
                "q": "Why is verification worth the effort?",
                "options": ["It makes the protocol faster", "A rare interleaving can deadlock or lose data in the field", "It removes the need for sequence numbers", "It is required by the physical layer"],
                "answer": 1,
                "why": "The failures that matter most are the rare ones that are hardest to reproduce.",
            },
        ],
        "examTip": "Name the three models, say what each one exposes, and finish with why testing alone is not enough.",
    },

    "CSCA421-MII-T06": {
        "explanation": "When many stations share one channel, something has to decide who may transmit. In ALOHA a station sends whenever it likes and retransmits after a collision, and slotted ALOHA doubles the throughput by forcing transmissions into time slots. CSMA makes a station listen first, with persistent and non persistent variants differing in how they retry. CSMA/CD detects a collision while transmitting and aborts early, which is classic Ethernet. Wireless cannot detect collisions, so CSMA/CA avoids them with backoff and acknowledgements. Collision free protocols such as token passing remove the problem entirely, at the cost of overhead.",
        "example": "A classroom where everyone talks at once is pure ALOHA. Waiting for silence before speaking is CSMA. Holding a talking stick so only one person speaks is a collision free protocol.",
        "quiz": [
            {
                "q": "What does slotted ALOHA do differently from pure ALOHA?",
                "options": ["It uses a token", "It forces transmissions to begin at a time slot boundary", "It detects collisions", "It reserves the channel"],
                "answer": 1,
                "why": "Aligning to slots halves the vulnerable period and roughly doubles the throughput.",
            },
            {
                "q": "Which protocol underlies classic wired Ethernet?",
                "options": ["CSMA/CA", "CSMA/CD", "Token passing", "Slotted ALOHA"],
                "answer": 1,
                "why": "Stations detect a collision while still transmitting and stop early to save channel time.",
            },
            {
                "q": "Why can wireless networks not use collision detection?",
                "options": ["They are too slow", "A station cannot hear its own transmission well enough while sending", "They have no addresses", "They use tokens instead"],
                "answer": 1,
                "why": "The incoming signal is far weaker than what is being sent, so CSMA/CA avoids collisions instead.",
            },
            {
                "q": "Which statement about multiple access is NOT correct?",
                "options": ["ALOHA retransmits after a collision", "CSMA listens before transmitting", "Token passing removes collisions entirely", "CSMA/CD is used in wireless LANs"],
                "answer": 3,
                "why": "Wireless LANs use CSMA/CA, because collision detection is impossible on a radio link.",
            },
            {
                "q": "What is the approximate maximum throughput of pure ALOHA?",
                "options": ["18 percent", "37 percent", "50 percent", "100 percent"],
                "answer": 0,
                "why": "Pure ALOHA peaks at 1 over 2e, about 18 percent, and slotted ALOHA doubles that to 37 percent.",
            },
        ],
        "examTip": "List ALOHA, slotted ALOHA, CSMA, CSMA/CD and CSMA/CA with one line each, and state the collision rule.",
    },

    "CSCA421-MII-T07": {
        "explanation": "The IEEE 802 family holds the standards for local and metropolitan networks. Ethernet, numbered 802.3, uses CSMA/CD with MAC addresses and is the dominant wired LAN technology, now mostly switched and full duplex. Token bus and token ring, numbered 802.4 and 802.5, passed a token for deterministic access and are now obsolete but still examined. Wireless LANs are 802.11, using CSMA/CA with optional RTS/CTS handshaking, in variants such as b, g, n, ac and ax. The 802.1 group covers bridging and VLAN tagging, and 802.2 covers the logical link control sublayer.",
        "example": "A campus lab runs 802.3 Ethernet to the wall sockets and 802.11ac wireless for laptops. Its switches use VLAN tagging under 802.1Q to keep staff and student traffic apart.",
        "quiz": [
            {
                "q": "Which standard defines Ethernet?",
                "options": ["IEEE 802.3", "IEEE 802.5", "IEEE 802.11", "IEEE 802.1"],
                "answer": 0,
                "why": "802.3 is Ethernet, which uses CSMA/CD and MAC addressing on wired LANs.",
            },
            {
                "q": "Which standard covers wireless LANs?",
                "options": ["IEEE 802.3", "IEEE 802.5", "IEEE 802.11", "IEEE 802.2"],
                "answer": 2,
                "why": "The 802.11 family defines wireless LANs, using CSMA/CA rather than collision detection.",
            },
            {
                "q": "Which statement about the 802 family is NOT correct?",
                "options": ["802.11 uses CSMA/CA", "Token ring is numbered 802.5", "802.1 covers bridging and VLAN tagging", "802.3 uses token passing"],
                "answer": 3,
                "why": "Ethernet uses CSMA/CD; it was the token networks 802.4 and 802.5 that passed a token.",
            },
            {
                "q": "What does a switch use to decide where to forward a frame?",
                "options": ["The IP address", "The MAC address", "The port number", "The domain name"],
                "answer": 1,
                "why": "A switch works at the data link layer and forwards by the MAC address it has learned.",
            },
            {
                "q": "What is the purpose of a VLAN?",
                "options": ["To increase cable length", "To separate broadcast domains on one physical network", "To raise the data rate", "To replace IP addresses"],
                "answer": 1,
                "why": "A VLAN groups ports logically, so broadcasts stay inside the group even on shared hardware.",
            },
        ],
        "examTip": "List 802.3, 802.4, 802.5 and 802.11 with the access method each uses, then add a line on bridges and VLANs.",
    },

    "CSCA421-MIII-T01": {
        "explanation": "The network layer carries a packet from the source host to the destination host, possibly across many networks. A router stores each incoming packet, reads its header and forwards it on the chosen outgoing link. Two services can be offered upwards. A datagram service treats each packet on its own, while a virtual circuit service sets up a path first. Routing is the work of building the tables, and forwarding is the per packet decision made from them. Internetworking has to cope with different frame sizes, different addressing and different quality of service. When the offered load passes capacity, the layer must also manage congestion.",
        "example": "A packet from a hostel laptop to a server abroad passes through a dozen routers. Each one reads only the destination address and picks the next hop.",
        "quiz": [
            {
                "q": "What is the difference between routing and forwarding?",
                "options": ["They are the same thing", "Routing builds the tables, forwarding uses them per packet", "Forwarding is done by the application", "Routing happens inside one host"],
                "answer": 1,
                "why": "Routing is the slower global computation, and forwarding is the fast local lookup per packet.",
            },
            {
                "q": "Which service sets up a path before any data is sent?",
                "options": ["Datagram service", "Virtual circuit service", "Connectionless service", "Best effort service"],
                "answer": 1,
                "why": "A virtual circuit reserves a path first, while a datagram service sends each packet alone.",
            },
            {
                "q": "Which statement about the network layer is NOT correct?",
                "options": ["Routers store and forward packets", "It delivers packets across many networks", "It handles congestion when load exceeds capacity", "It guarantees that no packet is ever lost"],
                "answer": 3,
                "why": "The Internet datagram service is best effort, so packets can be delayed, dropped or reordered.",
            },
            {
                "q": "Which is NOT an internetworking challenge listed in the syllabus?",
                "options": ["Different frame sizes", "Different addressing schemes", "Different quality of service", "The colour of the cable"],
                "answer": 3,
                "why": "The real challenges are differences in frame size, addressing and quality of service.",
            },
        ],
        "examTip": "State store and forward, contrast datagram with virtual circuit, then separate routing from forwarding in one line.",
    },

    "CSCA421-MIII-T02": {
        "explanation": "Routing algorithms fall into two families. Distance vector routing has each router tell its neighbours its distance to every destination, as RIP does. It is simple but converges slowly and can count to infinity. Link state routing gives every router the full topology through link state packets, then runs Dijkstra's shortest path algorithm, as OSPF does. Path vector routing, used by BGP, exchanges whole paths, which detects loops and lets policy be applied between autonomous systems. Fixed routing uses static tables, and flooding sends on every link but the incoming one.",
        "example": "A college with three buildings can use fixed routes written by hand. A national backbone cannot, because a link failure must be noticed and routed around within seconds.",
        "quiz": [
            {
                "q": "Which algorithm does OSPF use to compute paths?",
                "options": ["Bellman Ford", "Dijkstra shortest path", "Flooding", "Token passing"],
                "answer": 1,
                "why": "Every router learns the full topology and then runs Dijkstra to build a least cost tree.",
            },
            {
                "q": "Which problem is distance vector routing prone to?",
                "options": ["Deadlock", "Count to infinity", "Collision", "Fragmentation"],
                "answer": 1,
                "why": "Bad news travels slowly, so routers can keep raising a cost towards infinity after a link fails.",
            },
            {
                "q": "Which statement about routing is NOT correct?",
                "options": ["RIP is a distance vector protocol", "OSPF is a link state protocol", "BGP exchanges full path information", "Flooding is the most efficient way to route a large network"],
                "answer": 3,
                "why": "Flooding sends copies everywhere, which wastes bandwidth badly outside small special cases.",
            },
            {
                "q": "Which protocol routes between autonomous systems?",
                "options": ["RIP", "OSPF", "BGP", "ARP"],
                "answer": 2,
                "why": "BGP is the inter domain protocol, and it carries policy along with reachability.",
            },
            {
                "q": "Which method sends every packet out on all links except the one it arrived on?",
                "options": ["Fixed routing", "Flooding", "Hierarchical routing", "Multicast routing"],
                "answer": 1,
                "why": "Flooding guarantees delivery if a path exists, but produces many duplicate copies.",
            },
        ],
        "examTip": "Contrast distance vector and link state in a table: what is exchanged, convergence speed, one protocol each.",
    },

    "CSCA421-MIII-T03": {
        "explanation": "Congestion happens when more traffic arrives than the network can carry, and the effect is worse than the cause. Queues build, delay grows, packets are dropped, and beyond a point the throughput actually falls as the load rises. Leaky bucket and token bucket shape the traffic: the first releases at a fixed rate, the second allows bursts up to the saved credits. A congested router can send a choke packet, or mark packets, to ask the sender to slow down. Under real pressure the network sheds load by dropping packets deliberately, or refuses new flows by admission control.",
        "example": "A hostel link shared by three hundred students slows to a crawl during exam results. The router queue is full, so packets wait and time out, and the retries make it worse.",
        "quiz": [
            {
                "q": "What happens to throughput once congestion passes a certain point?",
                "options": ["It keeps rising", "It stays flat", "It falls as load keeps rising", "It becomes negative"],
                "answer": 2,
                "why": "Retransmissions and timeouts waste capacity, so more offered load delivers less useful work.",
            },
            {
                "q": "How does a token bucket differ from a leaky bucket?",
                "options": ["It allows bursts up to the saved credits", "It is slower", "It drops every packet", "It only works on wireless"],
                "answer": 0,
                "why": "The leaky bucket forces a constant output rate, while the token bucket permits a saved burst.",
            },
            {
                "q": "Which statement about congestion control is NOT correct?",
                "options": ["Load shedding drops packets deliberately under pressure", "Admission control refuses new flows", "A choke packet asks the sender to slow down", "Congestion control protects the receiver from being overwhelmed"],
                "answer": 3,
                "why": "Protecting the receiver is flow control; congestion control protects the network itself.",
            },
            {
                "q": "Which technique lets a congested router warn the sender without a separate packet?",
                "options": ["Load shedding", "Explicit signalling by marking packets", "Admission control", "Flooding"],
                "answer": 1,
                "why": "Marking bits in packets already flowing avoids adding more traffic to a congested link.",
            },
        ],
        "examTip": "Describe the collapse curve in one line, then give the four responses: shaping, signalling, shedding, admission control.",
    },

    "CSCA421-MIII-T04": {
        "explanation": "The Internet layer holds the whole Internet together with one addressing scheme and one packet format. An IPv4 address was historically split into classes A to E with a network part and a host part, but classless addressing replaced that. Subnetting borrows bits from the host part to make smaller networks, and CIDR aggregates prefixes so the routing tables stay small. Network address translation lets many private addresses share one public address by also using port numbers. ICMP reports errors, ARP resolves an IP address to a MAC address, and DHCP hands out addresses automatically.",
        "example": "A home router gives every device an address like 192.168.1.10 and shows one public address to the Internet. That translation is NAT, and it is why IPv4 has lasted as long as it has.",
        "quiz": [
            {
                "q": "What does ARP do?",
                "options": ["Assigns IP addresses automatically", "Resolves an IP address to a MAC address", "Reports errors", "Routes between autonomous systems"],
                "answer": 1,
                "why": "ARP finds the hardware address for a known IP address on the same link.",
            },
            {
                "q": "What problem does CIDR solve?",
                "options": ["Address shortage inside a home", "The growth of routing tables by aggregating prefixes", "Collisions on a LAN", "Encryption of packets"],
                "answer": 1,
                "why": "Aggregating prefixes means one table entry can stand for many networks.",
            },
            {
                "q": "Which statement about IP is NOT correct?",
                "options": ["NAT lets many private addresses share one public address", "IPv6 uses 128 bit addresses", "IPv4 addresses were historically grouped into classes", "DHCP is used to resolve IP addresses to MAC addresses"],
                "answer": 3,
                "why": "Resolving addresses is ARP's job; DHCP assigns a configuration to a host automatically.",
            },
            {
                "q": "How many bits does an IPv6 address use?",
                "options": ["32", "64", "128", "256"],
                "answer": 2,
                "why": "IPv6 moved from 32 to 128 bits, which removes the address shortage entirely.",
            },
            {
                "q": "Which protocol reports errors and carries the echo used by ping?",
                "options": ["ARP", "DHCP", "ICMP", "BGP"],
                "answer": 2,
                "why": "ICMP carries error reports and the echo request and reply that ping uses.",
            },
        ],
        "examTip": "Write the IPv4 header fields as a list, then contrast subnetting, CIDR and NAT in one line each.",
    },
}
