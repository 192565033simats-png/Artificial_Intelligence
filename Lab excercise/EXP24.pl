% Family Tree Program

% Facts
male(john).
male(paul).
male(mike).
male(david).

female(mary).
female(lisa).
female(susan).
female(anna).

% Parent Relationships
parent(john, paul).
parent(mary, paul).

parent(john, lisa).
parent(mary, lisa).

parent(paul, mike).
parent(susan, mike).

parent(paul, anna).
parent(susan, anna).

% Rules

% Father
father(X, Y) :-
    male(X),
    parent(X, Y).

% Mother
mother(X, Y) :-
    female(X),
    parent(X, Y).

% Sibling
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    dif(X, Y).

% Grandparent
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Ancestor
ancestor(X, Y) :-
    parent(X, Y).

ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).