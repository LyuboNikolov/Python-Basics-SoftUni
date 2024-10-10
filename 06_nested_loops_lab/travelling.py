destination = input()
total_money = 0
money_is_enough = False

while destination != "End":
    trip_price = float(input())
    while not money_is_enough:
        money_saved = float(input())
        total_money += money_saved

        if total_money >= trip_price:
            money_is_enough = True
            total_money = 0
            print(f"Going to {destination}!")

    destination = input()
    money_is_enough = False
