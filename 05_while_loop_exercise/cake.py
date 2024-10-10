width = int(input())
length = int(input())
cake_size = width * length
pieces_eaten = 0

while True:
    command = input()
    if command == "STOP":
        pieces_left = cake_size - pieces_eaten
        print(f"{pieces_left} pieces are left.")
        break

    current_pieces = int(command)
    pieces_eaten += current_pieces

    if pieces_eaten >= cake_size:
        pieces_needed = pieces_eaten - cake_size
        print(f"No more cake left! You need {pieces_needed} pieces more.")
        break
