rent_hall = float(input())

cake_price = 0.2 * rent_hall
drinks_price = cake_price * 0.55
animator_price = rent_hall / 3

total_price = rent_hall + cake_price + drinks_price + animator_price

print(f'{total_price:.1f}')
