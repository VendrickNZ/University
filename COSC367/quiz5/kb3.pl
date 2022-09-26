listtran([],[]).
listtran([Head|Tail], [Trans|Ttail]) :- tran(Head, Trans), listtran(Tail, Ttail).

tran(tahi,one). 
tran(rua,two). 
tran(toru,three). 
tran(wha,four). 
tran(rima,five). 
tran(ono,six). 
tran(whitu,seven). 
tran(waru,eight). 
tran(iwa,nine).

test_answer :-
    listtran(X, [one, seven, six, two]),
    writeln(X).