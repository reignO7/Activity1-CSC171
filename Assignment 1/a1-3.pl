hoofer(tony).
hoofer(shikuo).
hoofer(ellen).

hoofer(X) :- skier(X) ; mountainClimber(X) ; skier(X), mountainClimber(X).

skier(X) :- likes(X, snow).
mountainClimber(X) :- dislikes(X, rain).

likes(tony, snow).
likes(tony, rain).

likes(tony, _) :- dislikes(ellen, _).
dislikes(ellen, _) :- likes(tony, _).



start() :-
	write("Is there a Hoofers Club member who is a mountain climber but not a skier?"),
	nl,
	nl,
	queryClimber([tony, shikuo, ellen]).

queryClimber([Head|Tail]) :- (mountainClimber(Head) -> querySkier([Head|Tail]), nl ; queryClimber(Tail)).

querySkier([Head|Tail]) :- (skier(Head) -> queryClimber(Tail) ; write(Head), nl).