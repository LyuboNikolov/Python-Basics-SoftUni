name = input()
total_points = 301
successful_shots = 0
failed_shots = 0

while True:  # mozhe i s buleva - leg_is_won while not leg_is_won
    command = input()
    if command == "Retire":
        print(f"{name} retired after {failed_shots} unsuccessful shots.")
        break

    current_points = int(input())
    successful_shots += 1

    if command == "Single":
        current_points *= 1
    if command == "Double":
        current_points *= 2
    if command == "Triple":
        current_points *= 3
    total_points -= current_points

    if total_points < 0:
        successful_shots -= 1
        failed_shots += 1
        total_points += current_points
        continue

    if total_points == 0:
        print(f"{name} won the leg with {successful_shots} shots.")
        break


# count = 0
# successful_shots = 0
# failed_shots = 0
# total_points = 301
# tmp_points = 301
# won_leg = False
# name = input()
#
# while not won_leg:
#
#     if total_points != 0:
#         command = input()
#
#     if total_points == 0:
#         won_leg = True
#         print(f"{name} won the leg with {successful_shots} shots.")
#
#     if command != "Retire" and total_points != 0:
#         points = int(input())
#
#     if command == "Single":
#         tmp_points -= points
#
#         if tmp_points >= 0:
#             total_points = tmp_points
#             successful_shots += 1
#
#         else:
#             tmp_points = total_points
#             failed_shots += 1
#
#     elif command == "Double":
#         tmp_points -= points * 2
#
#         if tmp_points >= 0:
#             total_points = tmp_points
#             successful_shots += 1
#
#         else:
#             tmp_points = total_points
#             failed_shots += 1
#
#     elif command == "Triple":
#         tmp_points -= points * 3
#
#         if tmp_points >= 0:
#             total_points = tmp_points
#             successful_shots += 1
#
#         else:
#             tmp_points = total_points
#             failed_shots += 1
#
#     elif command == "Retire":
#         print(f"{name} retired after {failed_shots} unsuccessful shots.")
#         break
