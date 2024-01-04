chicken_menus = int(input())
fish_menus = int(input())
veggie_menus = int(input())

chicken_price = 10.35
fish_price = 12.4
veggie_price = 8.15
delivery = 2.5

total_price = chicken_price * chicken_menus + fish_price * fish_menus + veggie_price * veggie_menus
dessert = 0.2 * total_price

final_price = total_price + dessert + delivery

print(final_price)
