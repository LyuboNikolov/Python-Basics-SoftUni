from math import floor

tournaments = int(input())
initial_points = int(input())
total_points = initial_points
tournaments_won = 0

for tournament in range(tournaments):
    stage_reached = input()
    if stage_reached == "W":
        total_points += 2000
        tournaments_won += 1
    elif stage_reached == "F":
        total_points += 1200
    elif stage_reached == "SF":
        total_points += 720

average_points = floor((total_points - initial_points) / tournaments)
percent_won = tournaments_won / tournaments * 100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_won:.2f}%")
