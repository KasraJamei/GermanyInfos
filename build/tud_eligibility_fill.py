import pymupdf, sys
SRC = '/mnt/user-data/attachments/bcb18ef6-a48f-579b-bcdf-5777bddeb396/d0bb5013-Eligibility_check_261123_103519.pdf'
OUT = sys.argv[1]
FS = float(sys.argv[2]) if len(sys.argv) > 2 else 7

V = {
'Text1': '144',
'Text2': '8',
# Functional and OO Programming
'Text3': """Advanced Programming (3 units)
- Object-oriented programming in Java: classes, inheritance, generics
- Exception handling, file I/O and streams, multithreading
- Own implementation of data structures (linked lists)
- Debugging and testing of programs
Computer Fundamentals and Programming (3 units)
- Structured programming in C++: variables, types, control flow, loops
- Subprograms, arrays/matrices, input/output, search and sort
Programming Language Design (3 units)
- Concepts and components of programming languages
- Functional languages (LISP, Scheme, Standard ML, Haskell), OO languages
- Abstract data types; design, implementation and testing of projects""",
# ADS
'Text4': """Data Structures (3 units)
- Arrays, matrices, stacks, queues, linked lists (circular, doubly linked)
- Trees, search trees, decision/game trees; graphs and their representation
- Dynamic memory allocation; searching, sorting and merging algorithms
Algorithm Design (3 units)
- Complexity analysis and comparison of algorithms
- Divide and conquer (Quicksort, Strassen), dynamic programming (TSP, matrix chain), greedy (Huffman, scheduling)
- Exhaustive search, backtracking, alpha-beta pruning
Theory of Languages and Machines (3 units)
- Complexity classes P and NP, NP-complete and NP-hard problems""",
# Digital Design
'Text5': """Logic Circuits (3 units)
- Boolean algebra, logic gates, CMOS gates
- Combinational and sequential circuits, flip-flops, finite state machines
- Arithmetic circuits, memory arrays, programmable logic
- Hardware description languages
Logic Circuits and Computer Architecture Lab (1 unit)
- Karnaugh maps, multiplexers/demultiplexers, encoders
- Adders, subtractors, ALU design; SR, D, JK and T flip-flops
- Counters, shift registers; ROM, RAM, PLDs
- VHDL/Verilog basics and simulation of digital circuits
Computer-Aided Design of Digital Systems (3 units)
- Implementation and testing of digital circuits from logic gates to state machines (counting, timing, arithmetic)""",
# Computer Organisation (page 2 part)
'Text6': """Computer Architecture (3 units)
- Computer organization and design, instruction codes, register transfer, micro-operations, control unit
- Fixed/floating-point representation, CPU organization, arithmetic algorithms""",
'Text7': """- I/O organization, memory hierarchy, cache, virtual memory
Microprocessor and Assembly Language (3 units)
- ISA, assembly programming, addressing modes, data transfer instructions, subroutines, interrupts, I/O interfacing
Microprocessor Lab (1 unit): microprocessor-based system design
Logic Circuits and Computer Architecture Lab (1 unit): datapath, control unit, microprogramming, simple processor design""",
# Parallel Programming
'Text8': """Advanced Programming (3 units)
- Multithreading in Java; parallel and distributed programs over the network
Operating Systems Lab (1 unit)
- C++ and shell programming in Linux, system calls
- Processes and threads with pthreads; synchronization and communication between threads
Operating Systems (3 units)
- Multiprocessor systems, process concurrency, mutual exclusion""",
# Operating Systems
'Text9': """Operating Systems (3 units)
- Role, functions and types of operating systems; OS hierarchy
- Program status word, interrupts (types, processing, priorities)
- I/O programming and concurrency in I/O
- Multiprogramming; static and dynamic memory allocation, partitioning, demand paging, memory hierarchy
- Processor management: job and process scheduling, scheduling policies
- Multiprocessor systems, inter-process communication
- Resource allocation, deadlock (blocked state and recovery methods)
- Mutual exclusion, process concurrency with semaphores
- Device management: dedicated, shared and virtual devices, auxiliary storage, spooling
Operating Systems Lab (1 unit)
- Compiling and installing Linux; system calls; /proc
- Creating, running and terminating processes and threads (pthread library)
- Synchronization and inter-process communication
- Memory management, shared memory, virtual memory
- CPU scheduling; installable file systems
- Disk and I/O scheduling
- Design and implementation of device drivers
- Linux security mechanisms
- Real-time and embedded operating systems
- Introduction to the Windows Research Kernel""",
# Compiler (page 3 part)
'Text10': """Compiler Design Principles (3 units); Theory of Languages and Machines (3 units); Programming Language Design (3 units) - details below""",
'Text11': """Compiler Design Principles: structure and components of a compiler, grammars, lexical, syntax and semantic analysis, code generation and optimization, automated compiler-construction tools, development of a working compiler
Theory of Languages and Machines: context-free grammars, derivations and derivation trees, ambiguity, normal forms, CYK, deterministic parsing of context-free languages
Programming Language Design: projects on simple parsers and translators""",
# Automata
'Text12': """Theory of Languages and Machines (3 units)
- Languages and grammars, countable/uncountable sets
- DFA, NFA, regular languages and expressions, regular grammars, pumping lemma
- Context-free grammars and languages, Chomsky and Greibach normal forms, CYK, pushdown automata, deterministic PDAs, pumping lemma for CFLs
- Turing machines, Church-Turing thesis, decidability, halting problem, Post correspondence problem
Formal Methods in Software Engineering (3 units)
- Regular expressions, finite state machines, context-free grammars
Discrete Mathematics (3 units)
- Proof methods, induction, sets and relations""",
# Logic
'Text13': """Theory of Languages and Machines (3 units)
- Propositional logic, predicate logic, proof systems
Formal Methods in Software Engineering (3 units)
- Predicate calculus and natural deduction
- Structural induction
Discrete Mathematics (3 units)
- Formal logic notation, proof methods""",
# Formal Methods in Software Design
'Text14': """Formal Methods in Software Engineering (3 units)
- Formal notations for describing computations and computing systems
- Formal specification of software; specification languages
- Predicate calculus and natural deduction
- Inductive definitions of data types, recursive functions, structural induction
- Semantics of programming languages
- Partial correctness and proofs of termination""",
# Probabilistic Methods (page 4 part)
'Text15': """Engineering Statistics and Probability (3 units); Artificial Intelligence and Expert Systems (3 units) - details below""",
'Text16': """Engineering Statistics and Probability: probability theory, random variables, expected value and variance, discrete and continuous distributions, joint distributions, random sampling and random number generation, estimation, confidence intervals, hypothesis testing, ANOVA, regression and correlation
Artificial Intelligence and Expert Systems: belief networks, statistical methods for uncertainty management""",
# AI
'Text17': """Artificial Intelligence and Expert Systems (3 units)
- Search methods
- Knowledge acquisition and knowledge representation
- Belief networks; uncertainty management (statistical, symbolic, fuzzy logic)
- Neural networks
- Expert systems and expert system shells
- PROLOG programming
Algorithm Design (3 units)
- Adversarial search with alpha-beta pruning (game trees, e.g. tic-tac-toe)
Software Project (3 units) - bachelor's final project "Machine Learning for Cyberattack Detection"
- Supervised, unsupervised and deep learning methods for intrusion detection
- Evaluation with accuracy, detection rate and false positive rate""",
# Networks
'Text18': """Computer Networks (3 units)
- Network architectures, ISO reference model, topologies
- Physical layer, data link protocols, sliding window protocol
- Network layer, routing algorithms; broadcast in satellite and radio networks
Computer Networks Lab (1 unit)
- TCP/IP protocols analysed with Wireshark and network simulators
Internet Engineering (3 units)
- TCP/IP addressing, routing and transport protocols; network programming, web services""",
# Security (page 5 part)
'Text19': """Computer Networks (3 units)
- Network security algorithms; implementing a secure network
Internet Engineering (3 units)
- Internet security
Software Project (3 units)
- Cyberattack types and intrusion detection systems""",
'Text20': """Operating Systems Lab (1 unit)
- Linux security mechanisms""",
# Information Management
'Text21': """Databases (3 units)
- Relational database management systems
- Entity-relationship modelling, database design
- Relational algebra and relational calculus
- SQL data definition and manipulation
- Functional dependencies and normalization
- Indexing and hashing
- Transaction processing and concurrency control
- Database recovery and security
- Current trends in database technology
Database Lab (1 unit)
- Schema design, SQL
- Data warehouses, NoSQL
- Client/server model, internet database environments
- Basic database administration""",
# Software Engineering
'Text22': """Software Engineering (3 units): planning, requirements analysis, software design methods, software quality, maintenance, practical project
Software Engineering Lab (1 unit): team project covering requirements, analysis, design, implementation and testing
Object-Oriented Systems Design (3 units): OO analysis and design, UML, use cases, software quality assurance
Software Testing (3 units): test methods, coverage criteria (graph, logic, input space, syntax based), test tools
Systems Analysis and Design (3 units): requirements and feasibility analysis, modelling, architectural design, project management""",
# Scientific Computing (page 6 part)
'Text23': """Differential Equations (3 units)
- First and second order linear ODEs, series solutions, systems of ODEs, Laplace transform
- Numerical and analytical solution methods
Signals and Systems (3 units)
- Modelling of physical systems, LTI systems, state-space analysis, MATLAB exercises""",
'Text24': """Engineering Mathematics (3 units)
- Fourier series and transform; partial differential equations (wave, heat, Laplace equations)
General Mathematics 2 (3 units)
- Matrices, systems of linear equations, linear transformations, eigenvalues and eigenvectors""",
# Modeling, Specification and Semantics
'Text25': """Formal Methods in Software Engineering (3 units)
- Predicate calculus as a modelling tool
- Specification languages
- Semantics of programming languages
- Mathematically rigorous arguments about program properties
Programming Language Design (3 units)
- Syntax and semantics of programming languages
Discrete Mathematics (3 units)
- Proof techniques, induction, sets and relations""",
# Visual Computing
'Text26': '-',
}

d = pymupdf.open(SRC)
for p in d:
    for w in p.widgets():
        if w.field_name in V:
            w.field_value = V[w.field_name]
            w.text_fontsize = 9 if w.field_name in ('Text1', 'Text2') else (6.5 if w.field_name == 'Text7' else FS)
            w.update()
d.save(OUT)
