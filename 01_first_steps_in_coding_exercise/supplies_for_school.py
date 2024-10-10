number_pens = int(input())
number_markers = int(input())
liters_cleaning_product = int(input())
discount = int(input())

pens_price = number_pens * 5.8
markers_price = number_markers * 7.2
cleaning_product_price = liters_cleaning_product * 1.2

total_sum = pens_price + markers_price + cleaning_product_price
final_sum = total_sum - (total_sum * discount / 100)
print(final_sum)
