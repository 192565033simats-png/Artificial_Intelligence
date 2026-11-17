% Towers of Hanoi Program

hanoi(1, A, C, _) :-
    write('Move disk from '),
    write(A),
    write(' to '),
    write(C),
    nl.

hanoi(N, A, C, B) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, A, B, C),
    write('Move disk from '),
    write(A),
    write(' to '),
    write(C),
    nl,
    hanoi(N1, B, C, A).