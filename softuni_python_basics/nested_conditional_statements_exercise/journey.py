budget = float(input())
season = input()
destination = ""
accommodation = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
    elif season == "winter":
        price = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
    elif season == "winter":
        price = budget * 0.8
else:
    destination = "Europe"
    price = budget * 0.9

if season == "winter" or destination == "Europe":
    accommodation = "Hotel"
else:
    accommodation = "Camp"

print(f"Somewhere in {destination}\n{accommodation} - {price:.2f}")
