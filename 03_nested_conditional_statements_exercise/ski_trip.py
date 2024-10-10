days = int(input())
room_type = input()
review = input()
price = 0

if room_type == "room for one person":
    price = 18
elif room_type == "apartment":
    price = 25
    if days < 10:
        price *= 0.7
    elif 10 <= days <= 15:
        price *= 0.65
    else:
        price *= 0.5
elif room_type == "president apartment":
    price = 35
    if days < 10:
        price *= 0.9
    elif 10 <= days <= 15:
        price *= 0.85
    else:
        price *= 0.8

if review == "positive":
    price *= 1.25
elif review == "negative":
    price *= 0.9

total_price = (days - 1) * price
print(f"{total_price:.2f}")
