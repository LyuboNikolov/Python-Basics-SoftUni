stars_per_side = int(input())

for rows in range(1, stars_per_side + 1):
    print("*", end="")
    for columns in range(1, stars_per_side):
        print(" *", end="")
    print()
