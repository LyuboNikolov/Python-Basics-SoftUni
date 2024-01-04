from math import floor

record_in_seconds = float(input())
distance = float(input())
climbing_1_meter_time = float(input())

slope_delay = floor(distance / 50) * 30
total_time = climbing_1_meter_time * distance + slope_delay

if total_time < record_in_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    diff = total_time - record_in_seconds
    print(f"No! He was {diff:.2f} seconds slower.")
