initial_state(at(door), on_floor, at(window), has_not).

goal_state(has).

climb_up :-
    write('Monkey climbs onto the box'), nl.

solve :-
    initial_state(at(door), on_floor, at(window), has_not),
    write('Monkey moves from door to middle'), nl,
    write('Monkey pushes the box to middle'), nl,
    climb_up,
    write('Monkey takes the banana'), nl,
    write('Monkey has the banana'), nl.