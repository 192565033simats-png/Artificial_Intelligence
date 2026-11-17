% Fruit and Color Database

fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(orange, orange).
fruit_color(grapes, purple).
fruit_color(mango, yellow).
fruit_color(guava, green).
fruit_color(watermelon, green).
fruit_color(strawberry, red).
show_fruits :-
    fruit_color(Fruit, Color),
    write(Fruit),
    write(' is '),
    write(Color),
    nl,
    fail.

show_fruits.