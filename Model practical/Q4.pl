% Shortest Route Between Cities
connection(chennai, bangalore, 350).
connection(chennai, hyderabad, 630).
connection(bangalore, mysore, 145).
connection(bangalore, hyderabad, 570).
connection(mysore, mangalore, 255).
connection(hyderabad, mumbai, 710).
connection(bangalore, mumbai, 980).
% Roads are bidirectional
road(X, Y, D) :-
    connection(X, Y, D).
road(X, Y, D) :-
    connection(Y, X, D).
% Find all possible routes
route(X, Y, Path, Distance) :-
    travel(X, Y, [X], ReversePath, Distance),
    reverse(ReversePath, Path).
travel(X, Y, Visited, [Y|Visited], D) :-
    road(X, Y, D).
travel(X, Y, Visited, Path, Distance) :-
    road(X, Z, D1),
    \+ member(Z, Visited),
    travel(Z, Y, [Z|Visited], Path, D2),
    Distance is D1 + D2.
% Find the shortest route
shortest_route(X, Y, Path, Distance) :-
    setof(D-P, route(X, Y, P, D), [Distance-Path|_]).