% Bird Flying Program

% Facts
bird(sparrow).
bird(parrot).
bird(pigeon).
bird(penguin).
bird(ostrich).

% Birds that cannot fly
flightless(penguin).
flightless(ostrich).

% Rule to check flying ability
can_fly(X) :-
    bird(X),
    \+ flightless(X).

% Rule to check non-flying birds
cannot_fly(X) :-
    bird(X),
    flightless(X).