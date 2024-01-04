win_counter = 0
loss_counter = 0
total_games = 0

while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        break
    tournament_games = int(input())
    total_games += tournament_games
    for games in range(1, tournament_games + 1):
        team_desi = int(input())
        team_opponents = int(input())
        diff = abs(team_desi - team_opponents)
        if team_desi > team_opponents:
            win_counter += 1
            print(f"Game {games} of tournament {tournament_name}: win with {diff} points.")
        else:
            loss_counter += 1
            print(f"Game {games} of tournament {tournament_name}: lost with {diff} points.")
percent_won = win_counter / total_games * 100
percent_lost = loss_counter / total_games * 100
print(f"{percent_won:.2f}% matches win")
print(f"{percent_lost:.2f}% matches lost")
