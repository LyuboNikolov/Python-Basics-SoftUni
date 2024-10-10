budget = float(input())
statists = int(input())
clothes_price = float(input())

decor = budget * 0.1
total_clothing_price = statists * clothes_price

if statists > 150:
    total_clothing_price *= 0.9

total_price = total_clothing_price + decor
diff = abs(budget - total_price)

if budget >= total_price:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
