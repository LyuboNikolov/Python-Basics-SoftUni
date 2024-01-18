locations = int(input())

average_gold_daily = 0
total_gold_gathered = 0

for locations in range(1, locations + 1):
    expected_average_gold_daily = float(input())
    days_digging = int(input())
    for days in range(1, days_digging + 1):
        gold_gathered_day = float(input())
        total_gold_gathered += gold_gathered_day
        average_gold_daily = total_gold_gathered / days_digging
        if days == days_digging:
            total_gold_gathered = 0
            if average_gold_daily >= expected_average_gold_daily:
                print(f"Good job! Average gold per day: {average_gold_daily:.2f}.")
            else:
                gold_needed = expected_average_gold_daily - average_gold_daily
                print(f"You need {gold_needed:.2f} gold.")
