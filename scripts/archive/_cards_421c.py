# CSCA 421 Computer Networks - Modules IV and V
# Transport protocols, applications and network security.

CODE = "CSCA421"

CARDS = {
    "CSCA421-MIV-T01": {
        "explanation": "The transport layer carries data between two processes, not between two machines. It offers reliable or unreliable delivery, connection management, flow control and the multiplexing of several conversations over one network link. The service is described by primitives: LISTEN, CONNECT, ACCEPT, SEND, RECEIVE, DISCONNECT and CLOSE. A socket is an IP address together with a port number, and it names one end of a conversation. The Berkeley sockets API turns those ideas into calls such as socket, bind, listen, accept, connect, send, recv and close.",
        "example": "A web server listens on port 80 while a mail server on the same machine listens on port 25. One IP address, many services, kept apart by the port numbers.",
        "quiz": [
            {
                "q": "What does a socket combine?",
                "options": ["A MAC address and an IP address", "An IP address and a port number", "A port and a protocol name", "A domain name and a path"],
                "answer": 1,
                "why": "The pair names one endpoint, and a connection is named by the two sockets at its ends.",
            },
            {
                "q": "Which primitive does a server call first to wait for incoming connections?",
                "options": ["CONNECT", "LISTEN", "SEND", "CLOSE"],
                "answer": 1,
                "why": "LISTEN puts the server into a state where it can accept connection requests.",
            },
            {
                "q": "Which statement about the transport layer is NOT correct?",
                "options": ["It communicates between processes, not machines", "It can offer reliable or unreliable delivery", "Ports let several conversations share one host", "It forwards packets between routers"],
                "answer": 3,
                "why": "Forwarding between routers is the network layer's job; transport runs end to end between hosts.",
            },
            {
                "q": "Which of these is NOT a Berkeley sockets call?",
                "options": ["bind", "listen", "accept", "route"],
                "answer": 3,
                "why": "Routing is not part of the socket API, whose calls include bind, listen, accept, connect and recv.",
            },
            {
                "q": "What is the well known port for HTTP?",
                "options": ["21", "25", "80", "443"],
                "answer": 2,
                "why": "Port 80 is HTTP, 443 is HTTPS, 25 is SMTP and 21 is the FTP control connection.",
            },
        ],
        "examTip": "List the service primitives in the order a connection uses them, then define a socket with an example port.",
    },

    "CSCA421-MIV-T02": {
        "explanation": "A transport protocol has to solve a fixed list of problems. Addressing uses ports, and a connection identifier keeps two conversations between the same hosts apart. Establishing a connection normally takes a three way handshake, or four when both sides open at once. Releasing one needs care, because if both sides close together, data can be lost, so a two way or four way release is used. Flow control buffers data at the receiver and slides a window. Retransmission timers must be set from measured round trips, and a host that crashes must not corrupt later connections.",
        "example": "Two friends ending a call both say goodbye and wait for the other to finish. That is a two way release; hanging up the moment you are finished would cut off the last sentence.",
        "quiz": [
            {
                "q": "How many messages does the usual three way handshake use?",
                "options": ["One", "Two", "Three", "Four"],
                "answer": 2,
                "why": "SYN, then SYN ACK, then ACK, which sets the sequence numbers on both sides.",
            },
            {
                "q": "Why is connection release harder than it looks?",
                "options": ["The cable may break", "Both sides may close at once and lose data", "Ports may run out", "The window may overflow"],
                "answer": 1,
                "why": "Abrupt release can discard data still in flight, so the two sides confirm with each other.",
            },
            {
                "q": "Which statement about transport elements is NOT correct?",
                "options": ["Ports identify the process at each end", "A connection identifier separates simultaneous conversations", "Timers should be set from measured round trips", "Multiplexing means one process may use only one connection"],
                "answer": 3,
                "why": "Multiplexing lets many processes share one network service, which is the opposite of that.",
            },
            {
                "q": "What happens if a retransmission timer is set too short?",
                "options": ["Data is never sent", "Packets that were only delayed get retransmitted, wasting capacity", "The window stops sliding", "The port number changes"],
                "answer": 1,
                "why": "A premature timeout causes needless retransmission, adding load to an already slow path.",
            },
            {
                "q": "What should a host do after a crash, to stay safe?",
                "options": ["Reuse old connection identifiers at once", "Wait out the maximum packet lifetime before reusing identifiers", "Ignore all incoming data", "Close every port permanently"],
                "answer": 1,
                "why": "Waiting stops an old delayed packet from being accepted as part of a new connection.",
            },
        ],
        "examTip": "Walk through establishment, transfer and release in order, and add the timer rule at the end.",
    },

    "CSCA421-MIV-T03": {
        "explanation": "The Internet offers two transport protocols. UDP wraps the data in an eight byte header with source port, destination port, length and checksum, and offers nothing more; there is no connection. TCP is the opposite: connection oriented, ordered and reliable, with sequence numbers, a sliding window and congestion control. Its header carries the ports, the sequence and acknowledgement numbers, the flags, the window size and a checksum. TCP sets up with a three way handshake, then grows its rate by slow start and backs off after loss.",
        "example": "A cricket live score arrives over UDP, because a lost update matters less than a pause. Downloading a question paper uses TCP, because every byte has to arrive.",
        "quiz": [
            {
                "q": "How large is the UDP header?",
                "options": ["4 bytes", "8 bytes", "20 bytes", "32 bytes"],
                "answer": 1,
                "why": "Source port, destination port, length and checksum make eight bytes in all.",
            },
            {
                "q": "Which protocol is connection oriented and reliable?",
                "options": ["UDP", "TCP", "ICMP", "ARP"],
                "answer": 1,
                "why": "TCP numbers the bytes, acknowledges them and retransmits whatever is missing.",
            },
            {
                "q": "Which statement about UDP and TCP is NOT correct?",
                "options": ["UDP has no connection setup", "TCP orders the data it delivers", "UDP is used for DNS and streaming", "TCP always delivers data faster than UDP"],
                "answer": 3,
                "why": "Reliability costs setup and retransmission time, which is why streaming often prefers UDP.",
            },
            {
                "q": "What does the receiver advertise to control the sender's rate?",
                "options": ["A sequence number", "A window size", "A port number", "A checksum"],
                "answer": 1,
                "why": "The advertised window says how much data may be outstanding before an acknowledgement comes.",
            },
            {
                "q": "Which TCP mechanism grows the sending rate gradually after a connection starts?",
                "options": ["Slow start", "Fast retransmit", "Fast recovery", "Keep alive"],
                "answer": 0,
                "why": "Slow start begins small and grows the window until loss or a threshold is reached.",
            },
        ],
        "examTip": "Compare UDP and TCP in a table: header size, connection, reliability, ordering, one typical use each.",
    },

    "CSCA421-MIV-T04": {
        "explanation": "Transport performance comes down to how much data can be in flight. The bandwidth-delay product of a link tells you that, and the window must be at least that large or the link runs idle. Actual throughput is then limited by the window, the round trip time and any congestion on the way. Round trip time and its variation, called jitter, are measured to set a safe retransmission timeout. Delayed acknowledgements save packets but can slow a connection, and duplicate acknowledgements are the signal TCP uses to spot loss early. Voice and video need bounded delay, which TCP does not promise.",
        "example": "A 100 Mbps link with a 100 ms round trip holds about 1.25 MB in flight. A window smaller than that leaves the link partly empty, whatever the advertised speed says.",
        "quiz": [
            {
                "q": "What is the bandwidth-delay product used for?",
                "options": ["Choosing the cable type", "Sizing the window so the link stays full", "Setting the port number", "Counting lost packets"],
                "answer": 1,
                "why": "It is the amount of data in flight, so a smaller window means the link waits idle.",
            },
            {
                "q": "What is jitter?",
                "options": ["The average delay", "The variation in delay from packet to packet", "The number of lost packets", "The size of the window"],
                "answer": 1,
                "why": "Steady delay is tolerable for voice, but variation forces a large buffer at the receiver.",
            },
            {
                "q": "Which statement about performance is NOT correct?",
                "options": ["Throughput depends on window size and round trip time", "Jitter is the variation in delay", "TCP guarantees a bounded delay for voice calls", "Duplicate acknowledgements can signal a lost segment"],
                "answer": 2,
                "why": "TCP trades delay for reliability, so voice quality needs other arrangements.",
            },
            {
                "q": "Why does a receiver sometimes delay an acknowledgement?",
                "options": ["To slow the sender down deliberately", "To combine it with outgoing data and save a packet", "Because the timer is broken", "To force a retransmission"],
                "answer": 1,
                "why": "Delaying briefly lets the acknowledgement ride along with a reply, cutting the packet count.",
            },
            {
                "q": "If the window is too small for the bandwidth-delay product, what happens?",
                "options": ["Packets are dropped", "The link is under-used and throughput stays low", "The round trip time falls", "The connection resets"],
                "answer": 1,
                "why": "The sender stops while waiting for an acknowledgement, so the path carries less than it could.",
            },
        ],
        "examTip": "Write the bandwidth-delay product with a worked example, then state what limits throughput and why voice needs QoS.",
    },

    "CSCA421-MV-T01": {
        "explanation": "The application layer holds the services people actually use: the web, email, file transfer and the rest. Applications follow either the client server model, where clients ask a server, or the peer to peer model, where equal machines share the work. Every service needs a way to name what it is talking about, which is why URLs, domain names and port numbers exist. Each application protocol defines the message formats and the order of the exchanges. Programmers reach all of it through an API rather than writing the protocol by hand.",
        "example": "Typing a URL names three things at once: the host by its domain name, the service by the port, and the resource by the path. The browser then speaks HTTP to fetch it.",
        "quiz": [
            {
                "q": "Which two models do applications follow?",
                "options": ["Datagram and virtual circuit", "Client server and peer to peer", "Simplex and duplex", "Circuit and packet"],
                "answer": 1,
                "why": "Either a server answers requests, or equal peers share the work among themselves.",
            },
            {
                "q": "What does a URL name, besides the host?",
                "options": ["Only the file name", "The service through the port and the resource through the path", "The cable type", "The MAC address"],
                "answer": 1,
                "why": "Scheme, host, port, path, query and fragment together locate one resource.",
            },
            {
                "q": "Which statement about the application layer is NOT correct?",
                "options": ["It provides web, mail and file transfer", "An application protocol defines message formats", "An API hides the protocol details from the programmer", "It moves bits across a single cable"],
                "answer": 3,
                "why": "Moving bits on one link is the physical layer's job, several layers below this one.",
            },
            {
                "q": "Why does an application need a port number?",
                "options": ["To name the service on the host", "To choose the cable", "To encrypt the data", "To set the data rate"],
                "answer": 0,
                "why": "One host runs many services, and the port picks which one a message is meant for.",
            },
        ],
        "examTip": "Name the three design issues naming, model and protocol, and give one example of each from the web.",
    },

    "CSCA421-MV-T02": {
        "explanation": "DNS turns names people can remember into addresses machines can route to. Its name space is a tree: the root at the top, then top level domains, then second level domains, then individual hosts. Root servers point to top level domain servers, which point to authoritative servers, and a local resolver asks on the user's behalf. Resolution is either recursive, where the server does all the work, or iterative, where it returns the next server to ask. Answers are stored as resource records, and each carries a time to live so caches expire.",
        "example": "Typing a college website name makes the resolver ask a root server, then the domain server, then the college's own server. The answer is cached, so a second visit is instant.",
        "quiz": [
            {
                "q": "Which record holds the IPv4 address of a name?",
                "options": ["MX", "NS", "A", "CNAME"],
                "answer": 2,
                "why": "An A record gives the IPv4 address, and an AAAA record gives the IPv6 one.",
            },
            {
                "q": "What does a CNAME record do?",
                "options": ["Names the mail server", "Gives an alias that points at another name", "Holds the text of the domain", "Lists the name servers"],
                "answer": 1,
                "why": "A canonical name record lets one name act as an alias for another.",
            },
            {
                "q": "Which statement about DNS is NOT correct?",
                "options": ["Resolution may be recursive or iterative", "Resource records carry a time to live", "The name space is a tree with a root at the top", "DNS is a single central database"],
                "answer": 3,
                "why": "DNS is a distributed hierarchy, which is exactly what lets it scale to the whole Internet.",
            },
            {
                "q": "Which record tells mail where to go for a domain?",
                "options": ["A record", "MX record", "PTR record", "SOA record"],
                "answer": 1,
                "why": "The mail exchanger record names the server that accepts mail for that domain.",
            },
            {
                "q": "What threat does DNSSEC address?",
                "options": ["Slow resolution", "Cache poisoning, by signing the answers", "Cable failure", "Address shortage"],
                "answer": 1,
                "why": "Signed records let a resolver check that an answer came from the zone that owns it.",
            },
        ],
        "examTip": "Draw the name space tree, list the server types, then name four record types and what each holds.",
    },

    "CSCA421-MV-T03": {
        "explanation": "Email is a store and forward service rather than a direct conversation. User agents let people compose and read mail, while mail servers transfer it and hold it in mailboxes. SMTP is the push protocol on port 25 that sends a message from one server to the next. At the other end, POP3 downloads messages and usually deletes them from the server, while IMAP keeps them there and syncs folders across devices. A message has RFC 822 headers such as From, To and Subject, and MIME extends that to attachments and other character sets.",
        "example": "Reading mail on a phone and then on a laptop shows the same folders when IMAP is used. With POP3 the messages would already have been downloaded to whichever device got there first.",
        "quiz": [
            {
                "q": "Which protocol pushes mail from one server to the next?",
                "options": ["POP3", "IMAP", "SMTP", "HTTP"],
                "answer": 2,
                "why": "SMTP is the push protocol used to send mail and to relay it between servers.",
            },
            {
                "q": "Which protocol keeps messages on the server and syncs folders across devices?",
                "options": ["POP3", "IMAP", "SMTP", "FTP"],
                "answer": 1,
                "why": "IMAP leaves the mail on the server, so several devices see the same state.",
            },
            {
                "q": "Which statement about email is NOT correct?",
                "options": ["SMTP uses port 25", "MIME allows attachments", "POP3 downloads and usually deletes mail from the server", "IMAP is used to send mail between servers"],
                "answer": 3,
                "why": "Sending between servers is SMTP; IMAP only retrieves and manages mail at the mailbox end.",
            },
            {
                "q": "Which of these is a mail security mechanism?",
                "options": ["DKIM", "ARP", "NAT", "CRC"],
                "answer": 0,
                "why": "DKIM signs the message so the receiver can check the domain and that the content was not altered.",
            },
            {
                "q": "What does MIME add to email?",
                "options": ["Faster delivery", "Attachments, images and other character sets", "Encryption by default", "Routing between servers"],
                "answer": 1,
                "why": "MIME extends the plain text format so binary and non ASCII content can travel as mail.",
            },
        ],
        "examTip": "Draw the path user agent, sending server, receiving server, user agent, and name the protocol on each hop.",
    },

    "CSCA421-MV-T04": {
        "explanation": "The web is a set of hyperlinked documents fetched with HTTP and named by URLs. A URL carries the scheme, host, port, path, query and fragment, so a browser knows exactly what to ask for. HTTP is a text request response protocol, and it is stateless, so cookies or tokens carry any state a session needs. The methods GET, POST, PUT, DELETE, HEAD and OPTIONS say what the client intends, and the response carries a status code. Codes run 1xx informational, 2xx success, 3xx redirection, 4xx client error and 5xx server error.",
        "example": "Loading a results page sends a GET to the server. Submitting the exam form sends a POST, because the data changes something on the server rather than only reading it.",
        "quiz": [
            {
                "q": "Which status code class means the client made a mistake?",
                "options": ["2xx", "3xx", "4xx", "5xx"],
                "answer": 2,
                "why": "4xx means the request was wrong, as with 404 for a page that does not exist.",
            },
            {
                "q": "Which method should submit data that changes something on the server?",
                "options": ["GET", "POST", "HEAD", "OPTIONS"],
                "answer": 1,
                "why": "GET is for reading, while POST carries data that creates or changes a resource.",
            },
            {
                "q": "Which statement about the web is NOT correct?",
                "options": ["HTTP is stateless, so cookies carry session state", "A URL names the scheme, host, path and more", "A proxy can cache responses to speed up delivery", "A 5xx code means the request succeeded"],
                "answer": 3,
                "why": "5xx means the server failed; success is the 2xx family.",
            },
            {
                "q": "Why does HTTP use cookies?",
                "options": ["To make pages load faster", "To carry state across a stateless protocol", "To encrypt the connection", "To name the server"],
                "answer": 1,
                "why": "Each request stands alone in HTTP, so the cookie is what ties them into one session.",
            },
            {
                "q": "What does a persistent connection do?",
                "options": ["Keeps the TCP connection open for several requests", "Stores pages forever", "Encrypts every request", "Names the server"],
                "answer": 0,
                "why": "Reusing one connection removes the handshake cost for every object on a page.",
            },
        ],
        "examTip": "Write the six URL parts, the main methods and the five status classes, each with one example.",
    },

    "CSCA421-MV-T05": {
        "explanation": "Apart from the web and email, the application layer carries several older but still common services. FTP moves files and uses two connections: a control connection on port 21 that stays open, and a separate data connection for each transfer. Telnet gives a remote login but sends everything, including passwords, in the clear, which is why SSH replaced it. SSH encrypts the session and can tunnel other traffic through it. DHCP leases an IP configuration automatically, LDAP holds directory information, and SNMP lets a manager watch and configure network devices.",
        "example": "A laptop joins the hostel network and gets an address, a mask and a gateway without anyone typing them. That is DHCP leasing a configuration for a few hours.",
        "quiz": [
            {
                "q": "Which port does FTP use for its control connection?",
                "options": ["20", "21", "22", "25"],
                "answer": 1,
                "why": "Port 21 carries the commands, while a separate data connection carries the file itself.",
            },
            {
                "q": "Why is SSH preferred over Telnet?",
                "options": ["It is older", "It encrypts the session, including the password", "It uses fewer packets", "It works without a network"],
                "answer": 1,
                "why": "Telnet sends everything in the clear, which anyone on the path can read.",
            },
            {
                "q": "Which statement about these applications is NOT correct?",
                "options": ["DHCP leases IP configuration automatically", "SNMP is used for network management", "LDAP holds directory information such as users", "FTP uses one connection for both commands and data"],
                "answer": 3,
                "why": "FTP keeps control and data on separate connections, which is why firewalls need special handling.",
            },
            {
                "q": "What does SNMP use to report an event without being asked?",
                "options": ["A trap", "A cookie", "A token", "A ping"],
                "answer": 0,
                "why": "An agent sends a trap to the manager when something happens, instead of waiting to be polled.",
            },
            {
                "q": "Which service hands out an IP address automatically when a device joins a network?",
                "options": ["DNS", "DHCP", "SNMP", "SMTP"],
                "answer": 1,
                "why": "DHCP leases an address, a mask, a gateway and usually the DNS server to use.",
            },
        ],
        "examTip": "Give one line each on FTP, Telnet, SSH, DHCP, LDAP and SNMP, with a port number where there is one.",
    },

    "CSCA421-MV-T06": {
        "explanation": "Network security protects data while it travels. The goals are confidentiality, integrity, availability and authentication, and the attacks against them are interception, modification, masquerading and denial of service. A firewall sits between two networks and controls what passes, by packet filtering, stateful inspection or acting as an application proxy. Intrusion detection and prevention systems watch traffic for attack patterns and can act on what they find. A virtual private network carries private traffic across a public network inside an encrypted tunnel.",
        "example": "A college firewall blocks traffic to known command and control addresses. Its intrusion detection system raises an alert when a lab machine starts scanning the network.",
        "quiz": [
            {
                "q": "Which goal is attacked when someone reads data they should not see?",
                "options": ["Availability", "Confidentiality", "Authentication", "Accounting"],
                "answer": 1,
                "why": "Confidentiality means keeping the data readable only by those allowed to read it.",
            },
            {
                "q": "Which firewall method tracks the state of every connection?",
                "options": ["Packet filtering", "Stateful inspection", "Application proxy", "NAT"],
                "answer": 1,
                "why": "Stateful inspection remembers which connections were opened and admits their replies.",
            },
            {
                "q": "Which statement about network security is NOT correct?",
                "options": ["Denial of service attacks availability", "A VPN encrypts traffic across a public network", "An IDS watches for attack patterns", "A firewall can only block traffic, never log it"],
                "answer": 3,
                "why": "Logging is a standard firewall function, and the logs are what make an incident review possible.",
            },
            {
                "q": "What does a VPN provide?",
                "options": ["Faster routing", "An encrypted tunnel over a public network", "More IP addresses", "A domain name"],
                "answer": 1,
                "why": "The tunnel hides the contents, and often the real addresses, from anyone on the public path.",
            },
            {
                "q": "Masquerading is an attack on which goal?",
                "options": ["Authentication", "Availability", "Throughput", "Bandwidth"],
                "answer": 0,
                "why": "Pretending to be someone else defeats authentication, which is about proving identity.",
            },
        ],
        "examTip": "Match the four goals against the four attack types in a table, then add a line on firewalls, IDS and VPNs.",
    },

    "CSCA421-MV-T07": {
        "explanation": "Cryptography turns a plaintext into a ciphertext with a key, and only the right key turns it back. Symmetric schemes such as DES, 3DES and AES use the same secret key both ways. They are fast, but the key has to be shared first. Asymmetric schemes such as RSA and elliptic curve cryptography use a public and a private key, which solves key distribution and also allows signatures. A digital signature is a hash encrypted with the private key, and a certificate authority vouches for the public key. Hash functions such as the SHA family compress a message into a fixed digest.",
        "example": "Visiting a bank site, the browser checks the site certificate, agrees a key with asymmetric cryptography, then switches to AES for the session. That mix is what TLS does.",
        "quiz": [
            {
                "q": "Which type of cryptography uses the same key to encrypt and decrypt?",
                "options": ["Asymmetric", "Symmetric", "Hashing", "Steganography"],
                "answer": 1,
                "why": "One shared secret key does both jobs, which is fast but needs a safe way to share it.",
            },
            {
                "q": "What is a digital signature?",
                "options": ["A scanned image of a signature", "A hash encrypted with the sender's private key", "The message encrypted twice", "A password stored on the server"],
                "answer": 1,
                "why": "Anyone with the public key can check the hash, which proves origin and integrity together.",
            },
            {
                "q": "Which statement about cryptography is NOT correct?",
                "options": ["AES is a symmetric algorithm", "RSA is an asymmetric algorithm", "A hash can be reversed to recover the message", "A certificate authority vouches for a public key"],
                "answer": 2,
                "why": "A hash is one way by design, which is why it proves integrity but cannot be undone.",
            },
            {
                "q": "Why does TLS use both kinds of cryptography?",
                "options": ["Because one is free and the other is not", "Asymmetric solves key exchange, symmetric is fast for bulk data", "Because the browser requires it", "To use two keys at once for extra safety"],
                "answer": 1,
                "why": "The slow asymmetric step agrees a key, then the fast symmetric one carries the data.",
            },
            {
                "q": "Which key does a sender use to create a digital signature?",
                "options": ["Their public key", "Their private key", "The receiver's public key", "A shared session key"],
                "answer": 1,
                "why": "Only the holder of the private key could have made it, and that is what proves the origin.",
            },
        ],
        "examTip": "Define plaintext, ciphertext, key and hash, then contrast symmetric with asymmetric and say why TLS mixes them.",
    },
}
