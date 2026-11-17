% Best First Search Program

% Graph Connections
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).
edge(d, h).
edge(e, h).
edge(f, h).
edge(g, h).

% Heuristic Values
heuristic(a, 7).
heuristic(b, 6).
heuristic(c, 4).
heuristic(d, 5).
heuristic(e, 3).
heuristic(f, 2).
heuristic(g, 1).
heuristic(h, 0).

% Best First Search
best_first(Start, Goal, Path) :-
    search([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

search([[Goal|Path]|_], Goal, [Goal|Path]).

search([ [Current|Path] | Rest], Goal, Result) :-
    findall([Next, Current|Path],
            (edge(Current, Next),
             \+ member(Next, [Current|Path])),
            NewPaths),
    append(Rest, NewPaths, AllPaths),
    sort_paths(AllPaths, SortedPaths),
    search(SortedPaths, Goal, Result).

% Sort paths by heuristic value
sort_paths(Paths, Sorted) :-
    map_list_to_pairs(path_heuristic, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

path_heuristic([Node|_], H) :-
    heuristic(Node, H).