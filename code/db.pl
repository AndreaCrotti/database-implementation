factory('bigcomp').
factory('bigcomp2').

city('guidizzolo').
city('paperopoli').

empl(1, 'milner', 'bigcomp', 100, 'guidizzolo').
empl(2, 'adam', 'bigcomp2', 400, 'paperopoli').

manager(1, 'paperopoli').

boss(1, 1).
boss(2, 3).

% putting one after the other we get automatically and OR
dep(X,Y) :-
	factory(Y),
	empl(_,X,Y,_,_).

dep(X,Y) :-
	factory(Y),
	empl(X,_,Y,_,_).

rich(X) :-
	empl(X,_,_,S,_), S > 100.