hour = int(input())
day = input()

if hour < 10 or hour > 18:
    print("closed")
elif day == "Sunday":
    print("closed")
else:
    print("open")
