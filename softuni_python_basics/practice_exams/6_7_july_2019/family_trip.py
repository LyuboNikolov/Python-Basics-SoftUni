budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_extra_cost = int(input())

price_all_nights = nights * price_per_night
if nights > 7:
    price_all_nights = price_all_nights * 0.95

total_price = price_all_nights + budget * (percent_extra_cost / 100)

diff = abs(budget - total_price)
if budget >= total_price:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')

