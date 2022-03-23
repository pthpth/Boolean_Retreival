# Boolean Information Retrieval System

## To perform boolean querying :
``$ python main.py``

_To terminate the program send EOF_
## Testcases :
```
$ python .\main.py
Enter query: (julius and cal*) or cassius  
FOUND  8  DOCUMENTS SATISFYING USER QUERY
Henry VI, Part 1
Henry VI, Part 2
Julius Caesar
Richard III
Richard II
Antony and Cleopatra
Cymbeline
Hamlet
-------------------------------------------------------------------------------
Enter query: (ce*ar and (brutus and cal*)) or cassius
FOUND  6  DOCUMENTS SATISFYING USER QUERY
Henry VI, Part 2
Julius Caesar
Lucrece
Antony and Cleopatra
Titus Andronicus
Coriolanus
-------------------------------------------------------------------------------
Enter query: CaLiFoRnIa Or (OlYmPuS aNd SlIpPeRy)
Did you mean Calphurnia ?
FOUND  3  DOCUMENTS SATISFYING USER QUERY
Julius Caesar
Troilus and Cressida
Coriolanus
-------------------------------------------------------------------------------
Enter query: Kinhs AND Ham* 
Did you mean Kinds ?
FOUND  16  DOCUMENTS SATISFYING USER QUERY
Henry VI, Part 2
Henry VI, Part 3
Henry V
King John
Lucrece
Pericles, Prince of Tyre
Richard II
Romeo and Juliet
Sonnets
Antony and Cleopatra
The Two Gentlemen of Verona
The Winter's Tale
Titus Andronicus
Troilus and Cressida
Hamlet
Henry IV, Part 2
-------------------------------------------------------------------------------
```
## Documentation:
- Made using pdocs3
- Located in _./html_