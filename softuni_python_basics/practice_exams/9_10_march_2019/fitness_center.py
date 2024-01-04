number_visitors = int(input())

counter_back = 0
counter_chest = 0
counter_legs = 0
counter_abs = 0

counter_shake = 0
counter_bar = 0

people_training = 0
people_protein = 0
total_people = 0


for i in range(1, number_visitors +1):
    activity = input()
    total_people += 1
    if activity == "Back" or activity == "Chest" or \
        activity == "Legs" or activity == "Abs":
        people_training += 1
        if activity == "Back":
            counter_back += 1
        elif activity == "Chest":
            counter_chest += 1
        elif activity == "Legs":
            counter_legs += 1
        elif activity == "Abs":
            counter_abs += 1
    elif activity == "Protein shake" or activity == "Protein bar":
        people_protein += 1
        if activity == "Protein shake":
            counter_shake += 1
        elif activity == "Protein bar":
            counter_bar += 1

percent_training = people_training / total_people * 100
percent_protein = people_protein / total_people * 100

print(f"{counter_back} - back")
print(f"{counter_chest} - chest")
print(f"{counter_legs} - legs")
print(f"{counter_abs} - abs")
print(f"{counter_shake} - protein shake")
print(f"{counter_bar} - protein bar")
print(f"{percent_training:.2f}% - work out")
print(f"{percent_protein:.2f}% - protein")
