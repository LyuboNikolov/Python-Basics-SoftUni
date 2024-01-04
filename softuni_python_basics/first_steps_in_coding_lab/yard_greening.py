area = float(input())
price_per_square_meter = 7.61
discount = 0.18 * area * price_per_square_meter

total_price = area * price_per_square_meter - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")
