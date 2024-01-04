from math import ceil

wall_height = int(input())
wall_width = int(input())
clear_walls_percent = int(input())
all_is_painted = False
area_for_painting = wall_height * wall_width * 4
area_for_painting = area_for_painting * (100 - clear_walls_percent) / 100 # *=
command = input()
while command != "Tired!":
    current_liters_paint = int(command)
    area_for_painting -= current_liters_paint
    if area_for_painting <= 0:
        all_is_painted = True
        break
    command = input()
if all_is_painted: #if all_is_painted == True
    if area_for_painting < 0:
        area_for_painting = int(ceil(abs(area_for_painting)))
        print(f"All walls are painted and you have {area_for_painting} l paint left!")
    else: #area_for_painting == 0
        print("All walls are painted! Great job, Pesho!")
else:
    print(f"{int(area_for_painting)} quadratic m left.")