age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
saved_money = 0
toys_received = 0
even_years_counter = 0

for year in range(1, age + 1):
    if year % 2 != 0:
        toys_received += 1
    else:
        even_years_counter += 1
        saved_money += (even_years_counter * 10) - 1

total_money = saved_money + toy_price * toys_received
diff = abs(total_money - washing_machine_price)
if total_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
