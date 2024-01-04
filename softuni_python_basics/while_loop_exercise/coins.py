change = float(input())
change_in_coins = round(change * 100)
coins_counter = 0

while change_in_coins > 0:
    if change_in_coins // 200 >= 1:
        coins_counter += 1
        change_in_coins -= 200
    elif change_in_coins // 100 >= 1:
        coins_counter += 1
        change_in_coins -= 100
    elif change_in_coins // 50 >= 1:
        coins_counter += 1
        change_in_coins -= 50
    elif change_in_coins // 20 >= 1:
        coins_counter += 1
        change_in_coins -= 20
    elif change_in_coins // 10 >= 1:
        coins_counter += 1
        change_in_coins -= 10
    elif change_in_coins // 5 >= 1:
        coins_counter += 1
        change_in_coins -= 5
    elif change_in_coins // 2 >= 1:
        coins_counter += 1
        change_in_coins -= 2
    elif change_in_coins // 1 >= 1:
        coins_counter += 1
        change_in_coins -= 1

print(coins_counter)
