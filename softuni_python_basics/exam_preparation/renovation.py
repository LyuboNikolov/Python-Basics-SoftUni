from math import ceil

height = int(input())
width = int(input())
percent_not_painted = int(input())
total_area = height * width * 4
area_to_paint = ceil(total_area - (percent_not_painted / 100) * total_area)
all_is_painted = False
total_paint = 0

command = input()
while command != "Tired!":
    paint_liters = int(command)
    total_paint += paint_liters
    area_to_paint -= paint_liters

    if area_to_paint <= 0:
        all_is_painted = True
        break

    command = input()

if all_is_painted:
    paint_left = abs(area_to_paint)
    if paint_left == 0:
        print("All walls are painted! Great job, Pesho!")
    else:
        print(f"All walls are painted and you have {paint_left} l paint left!")
else:
    print(f"{area_to_paint} quadratic m left.")
