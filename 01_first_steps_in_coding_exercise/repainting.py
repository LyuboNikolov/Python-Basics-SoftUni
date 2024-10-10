nylon = int(input())
paint = int(input())
thinner = int(input())
hours_worked = int(input())

nylon_price = (nylon + 2) * 1.5
paint_price = paint * 1.1 * 14.5
thinner_price = thinner * 5
bags = 0.4

materials_sum = nylon_price + paint_price + thinner_price + bags
workers_price = materials_sum * 0.3 * hours_worked
final_sum = materials_sum + workers_price

print(final_sum)
