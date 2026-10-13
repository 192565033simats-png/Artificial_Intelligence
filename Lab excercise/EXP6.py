rooms = {'A': 1, 'B': 1}
position = 'A'

while 1 in rooms.values():
    print("Vacuum at:", position)

    if rooms[position] == 1:
        rooms[position] = 0
        print(position, "cleaned")
    else:
        position = 'B' if position == 'A' else 'A'

print("Final status:", rooms)
print("Both rooms are clean")
