
from math import floor
from math import ceil

price_racket = float(input())
number_rackets = int(input())
number_sneakers = int(input())

price_sneakers = price_racket / 6

total_sneakers_rackets = number_sneakers * price_sneakers + number_rackets * price_racket
other_equipment = total_sneakers_rackets * 0.2

sum_paid_djokovic = floor((total_sneakers_rackets + other_equipment) / 8)
sum_paid_sponsors = ceil(((total_sneakers_rackets + other_equipment) / 8) * 7)

print(f"Price to be paid by Djokovic {sum_paid_djokovic}")
print(f"Price to be paid by sponsors {sum_paid_sponsors}")

