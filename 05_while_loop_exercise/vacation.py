trip_price = float(input())
current_money = float(input())
total_money = current_money
days_counter = 0
consecutive_days_spending = 0

while True:
    action = input()
    amount = float(input())

    days_counter += 1

    if action == "spend":
        consecutive_days_spending += 1
        total_money -= amount
        if total_money <= 0:
            total_money = 0
        if consecutive_days_spending == 5:
            print(f"You can't save the money.\n{days_counter}")
            break
    elif action == "save":
        consecutive_days_spending = 0
        total_money += amount
        if total_money >= trip_price:
            print(f"You saved the money for {days_counter} days.")
            break
