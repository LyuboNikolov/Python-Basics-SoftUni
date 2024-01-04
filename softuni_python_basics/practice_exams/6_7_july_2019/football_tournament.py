football_team = input()
number_of_games = int(input())
wins = 0
draws = 0
losses = 0
points = 0

for games in range(number_of_games):
    result = input()
    if result == "W":
        wins += 1
        points += 3
    elif result == "D":
        draws += 1
        points += 1
    elif result == "L":
        losses += 1
if number_of_games == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    print(f"{football_team} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {losses}")
    percent_games_won = wins / number_of_games * 100
    print(f"Win rate: {percent_games_won:.2f}%")


