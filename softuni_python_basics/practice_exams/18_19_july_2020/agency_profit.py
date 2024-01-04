airline_name = input()
number_adult_tickets = int(input())
number_kid_tickets = int(input())
net_price_adults = float(input())
service_fee = float(input())
price_kids = net_price_adults * 0.3
total_sales = (net_price_adults + service_fee) * number_adult_tickets \
              + (price_kids + service_fee) * number_kid_tickets
agency_profit = total_sales * 0.2
print(f"The profit of your agency from {airline_name} tickets is {agency_profit:.2f} lv.")
