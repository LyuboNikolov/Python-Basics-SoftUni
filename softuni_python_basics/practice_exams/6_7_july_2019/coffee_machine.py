drink = input()
sugar = input()
number_drinks = int(input())
total_price = 1 * number_drinks

if sugar == 'Without':
    total_price = total_price * 0.65
    if drink == 'Espresso' and number_drinks < 5:
        total_price = total_price * 0.9
    elif drink == 'Espresso' and number_drinks >= 5:
        total_price = total_price * 0.9 * 0.75
    elif drink == 'Cappuccino':
        total_price = total_price * 1.00
    elif drink == 'Tea':
        total_price = total_price * 0.5

elif sugar == 'Normal':
    if drink == 'Espresso' and number_drinks < 5:
        total_price = total_price * 1
    elif drink == 'Espresso' and number_drinks >= 5:
        total_price = total_price * 1 * 0.75
    elif drink == 'Cappuccino':
        total_price = total_price * 1.2
    elif drink == 'Tea':
        total_price = total_price * 0.6

elif sugar == 'Extra':
    if drink == 'Espresso' and number_drinks < 5:
        total_price = total_price * 1.2
    elif drink == 'Espresso' and number_drinks >= 5:
        total_price = total_price * 1.2 * 0.75
    elif drink == 'Cappuccino':
        total_price = total_price * 1.6
    elif drink == 'Tea':
        total_price = total_price * 0.7

if total_price > 15:
    total_price = total_price * 0.8
print(f"You bought {number_drinks} cups of {drink} for {total_price:.2f} lv.")
