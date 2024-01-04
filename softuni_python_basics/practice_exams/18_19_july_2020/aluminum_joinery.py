number_joinery = int(input())
type_joinery = input()
delivery = input()
price = 0

if type_joinery == "90X130":
    price = 110
    if 30 < number_joinery <= 60:
        price *= 0.95
    elif number_joinery > 60:
        price *= 0.92
elif type_joinery == "100X150":
    price = 140
    if 40 < number_joinery <= 80:
        price *= 0.94
    elif number_joinery > 80:
        price *= 0.9
elif type_joinery == "130X180":
    price = 190
    if 20 < number_joinery <= 50:
        price *= 0.93
    elif number_joinery > 50:
        price *= 0.88
elif type_joinery == "200X300":
    price = 250
    if 25 < number_joinery <= 50:
        price *= 0.91
    elif number_joinery > 50:
        price *= 0.86
total_price = number_joinery * price
if delivery == "With delivery":
    total_price += 60
if number_joinery < 10:
    print("Invalid order")
elif number_joinery >= 10:
    if number_joinery > 99:
        total_price *= 0.96
    print(f"{total_price:.2f} BGN")
