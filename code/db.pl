factory('bigcomp').
factory('bigcomp2').
empl(1, 'milner', 'bigcomp').
empl(2, 'adam', 'bigcomp2').

% putting one after the other we get automatically and OR
dep(X,Y) :-
	factory(Y),
	empl(_,X,Y).

dep(X,Y) :-
	factory(Y),
	empl(X,_,Y).