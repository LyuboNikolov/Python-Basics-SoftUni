desired_profit = float(input())
total_sum = 0
sum_is_reached = False

cocktail_name = input()
while cocktail_name != "Party!":
    number_cocktails = int(input())

    current_sum = number_cocktails * len(cocktail_name)
    if current_sum % 2 != 0:
        current_sum *= 0.75
    total_sum += current_sum
    if total_sum >= desired_profit:
        sum_is_reached = True
        break
    cocktail_name = input()

if sum_is_reached:
    print("Target acquired.")
    print(f"Club income - {total_sum:.2f} leva.")
else:
    needed_sum = abs(total_sum - desired_profit)
    print(f"We need {needed_sum:.2f} leva more.")
    print(f"Club income - {total_sum:.2f} leva.")
