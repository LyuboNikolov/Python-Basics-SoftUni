tournament_days = int(input())

total_money_raised = 0
won_games_total = 0
lost_games_total = 0

for days in range(tournament_days):
    sport = input()
    daily_money = 0
    won_games_daily = 0
    lost_games_daily = 0

    while sport != "Finish":
        result = input()
        if result == "win":
            won_games_daily += 1
            daily_money += 20
        else:
            lost_games_daily += 1
        sport = input()
    if won_games_daily > lost_games_daily:
        daily_money *= 1.1
    total_money_raised += daily_money
    won_games_total += won_games_daily
    lost_games_total += lost_games_daily
else:
    if won_games_total > lost_games_total:
        total_money_raised *= 1.2
        print(f"You won the tournament! Total raised money: {total_money_raised:.2f}")
    else:
        print(f"You lost the tournament! Total raised money: {total_money_raised:.2f}")
