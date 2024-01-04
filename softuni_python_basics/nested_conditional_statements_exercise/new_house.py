flower_type = input()
quantity = int(input())
budget = int(input())
price = 0

if flower_type == "Roses":
    price = 5
    if quantity > 80:
        price *= 0.9
elif flower_type == "Dahlias":
    price = 3.80
    if quantity > 90:
        price *= 0.85
elif flower_type == "Tulips":
    price = 2.80
    if quantity > 80:
        price *= 0.85
elif flower_type == "Narcissus":
    price = 3
    if quantity < 120:
        price *= 1.15
elif flower_type == "Gladiolus":
    price = 2.50
    if quantity < 80:
        price *= 1.2

total_price = quantity * price
diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {quantity} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
