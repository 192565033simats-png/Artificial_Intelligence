% Backward Chaining Program

% Facts
human(socrates).
human(plato).

% Rules
mortal(X) :-
    human(X).

mammal(X) :-
    human(X).

warm_blooded(X) :-
    mammal(X).