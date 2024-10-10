groups_number = int(input())
mussala_group = 0
montblanc_group = 0
kilimanjaro_group = 0
k2_group = 0
everest_group = 0
total_climbers = 0

for group in range(groups_number):
    current_group = int(input())
    total_climbers += current_group
    if current_group <= 5:
        mussala_group += current_group
    elif 6 <= current_group <= 12:
        montblanc_group += current_group
    elif 13 <= current_group <= 25:
        kilimanjaro_group += current_group
    elif 26 <= current_group <= 40:
        k2_group += current_group
    elif current_group >= 41:
        everest_group += current_group

percent_mussala = mussala_group / total_climbers * 100
percent_montblanc = montblanc_group / total_climbers * 100
percent_kilimanjaro = kilimanjaro_group / total_climbers * 100
percent_k2 = k2_group / total_climbers * 100
percent_everest = everest_group / total_climbers * 100

print(f"{percent_mussala:.2f}%")
print(f"{percent_montblanc:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
