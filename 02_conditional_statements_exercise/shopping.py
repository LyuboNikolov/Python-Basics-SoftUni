budget = float(input())
video_cards_count = int(input())
cpu_count = int(input())
ram_count = int(input())

video_cards_price = video_cards_count * 250
cpu_price = video_cards_price * 0.35 * cpu_count
ram_price = video_cards_price * 0.1 * ram_count

total_price = video_cards_price + cpu_price + ram_price

if video_cards_count > cpu_count:
    total_price *= 0.85

diff = abs(budget - total_price)
if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
