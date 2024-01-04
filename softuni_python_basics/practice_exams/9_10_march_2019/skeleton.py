minutes_control = int(input())
seconds_control = int(input())
track_length = float(input())
seconds_per_100_meters = int(input())

minutes_into_seconds = minutes_control * 60
total_seconds_control = minutes_into_seconds + seconds_control

slope_acceleration = (track_length / 120) * 2.5
marin_time = (track_length / 100 * seconds_per_100_meters) - slope_acceleration

if marin_time <= total_seconds_control:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    diff = marin_time - total_seconds_control
    print(f"No, Marin failed! He was {diff:.3f} second slower.")