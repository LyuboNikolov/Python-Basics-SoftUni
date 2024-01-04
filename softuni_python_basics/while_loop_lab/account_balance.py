total_money = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        break

    current_sum = float(command)

    if current_sum < 0:
        print("Invalid operation!")
        break
    else:
        total_money += current_sum
        print(f"Increase: {current_sum:.2f}")

print(f"Total: {total_money:.2f}")
