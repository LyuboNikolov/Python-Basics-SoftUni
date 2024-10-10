from math import floor

spaceship_width = float(input())
spaceship_length = float(input())
spaceship_height = float(input())
average_height_astronauts = float(input())

one_room = 2 * 2 * (average_height_astronauts + 0.4)

volume_spaceship = spaceship_height * spaceship_length * spaceship_width

rooms_available = floor(volume_spaceship / one_room)

if 3 <= rooms_available <= 10:
    print(f"The spacecraft holds {rooms_available} astronauts.")
elif rooms_available < 3:
    print("The spacecraft is too small.")
elif rooms_available > 10:
    print("The spacecraft is too big.")

