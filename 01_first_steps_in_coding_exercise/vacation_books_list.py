number_pages = int(input())
pages_per_hour = int(input())
number_days = int(input())

total_hours_reading = number_pages // pages_per_hour
hours_needed_daily = total_hours_reading // number_days

print(hours_needed_daily)
