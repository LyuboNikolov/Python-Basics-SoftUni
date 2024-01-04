number_people = int(input())
entrance_fee = float(input())
sunbed_fee = float(input())
umbrella_fee = float(input())

from math import ceil
sunbeds_cost = (ceil(number_people * 0.75)) * sunbed_fee
umbrellas_cost = (ceil(number_people * 0.5)) * umbrella_fee

total_cost = sunbeds_cost + umbrellas_cost + entrance_fee * number_people
print(f'{total_cost:.2f} lv.')
