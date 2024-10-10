from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
relax_time = break_duration / 4

total_time = episode_duration + lunch_time + relax_time

diff = abs(break_duration - total_time)
time_rounded_up = ceil(diff)
if break_duration >= total_time:
    print(f"You have enough time to watch {series_name} and left with {time_rounded_up} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {time_rounded_up} more minutes.")
