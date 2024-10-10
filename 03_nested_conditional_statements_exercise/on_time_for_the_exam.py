exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minutes
arrival_time_in_minutes = arrival_hour * 60 + arrival_minutes

diff = exam_time_in_minutes - arrival_time_in_minutes
if diff < 0:
    print("Late")
    if abs(diff) < 60:
        print(f"{abs(diff)} minutes after the start")
    else:
        hours = abs(diff) // 60
        minutes = abs(diff) % 60
        print(f"{hours}:{minutes:02d} hours after the start")

elif 0 <= diff <= 30:
    if diff == 0:
        print("On time")
    else:
        print(f"On time\n{abs(diff)} minutes before the start")

else:
    print("Early")
    if abs(diff) < 60:
        print(f"{abs(diff)} minutes before the start")
    else:
        hours = abs(diff) // 60
        minutes = abs(diff) % 60
        print(f"{hours}:{minutes:02d} hours before the start")
