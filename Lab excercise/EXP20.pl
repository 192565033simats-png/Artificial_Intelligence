% Forward Chaining Program

:- dynamic known/1.

% Initial Facts
initial_fact(fever).
initial_fact(cough).
initial_fact(body_pain).

% Rules
rule([fever, cough], flu).
rule([flu, body_pain], consult_doctor).

% Check all conditions
all_known([]).

all_known([H|T]) :-
    known(H),
    all_known(T).

% Forward Chaining
forward_chain :-
    rule(Conditions, Conclusion),
    \+ known(Conclusion),
    all_known(Conditions),
    !,
    assertz(known(Conclusion)),
    write('Derived: '),
    write(Conclusion),
    nl,
    forward_chain.

forward_chain.

% Run Program
run :-
    retractall(known(_)),
    forall(initial_fact(X), assertz(known(X))),
    forward_chain,
    nl,
    write('Final Facts:'),
    nl,
    listing(known).