def vacuum_cleaner():
    rooms = {'A': 'Dirty', 'B': 'Dirty'}
    location = 'A'

    while True:
        if rooms[location] == 'Dirty':
            print("Cleaning Room", location)
            rooms[location] = 'Clean'
        else:
            print("Room", location, "is already Clean")

        if location == 'A':
            location = 'B'
        else:
            break

    print("\nFinal Status:")
    for room in rooms:
        print(room, ":", rooms[room])

vacuum_cleaner()