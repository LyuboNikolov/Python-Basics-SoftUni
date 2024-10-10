width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height
house_is_full = False

input_line = input()
while input_line != "Done":
    free_space -= int(input_line)

    if free_space <= 0:
        house_is_full = True
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        break

    input_line = input()

if not house_is_full:
    print(f"{free_space} Cubic meters left.")
