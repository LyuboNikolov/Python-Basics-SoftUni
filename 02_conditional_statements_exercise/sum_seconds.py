time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third
total_minutes = total_time // 60
total_seconds = total_time % 60

print(f"{total_minutes}:{total_seconds:02d}")
