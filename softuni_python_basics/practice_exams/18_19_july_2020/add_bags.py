fee_over_20_kg = float(input())
luggage_weight = float(input())
days_to_trip = int(input())
pieces_of_luggage = int(input())

luggage_fee = 0

if luggage_weight < 10:
    luggage_fee = 0.2 * fee_over_20_kg
elif 10 <= luggage_weight <= 20:
    luggage_fee = 0.5 * fee_over_20_kg
else:
    luggage_fee = fee_over_20_kg

if days_to_trip > 30:
    luggage_fee *= 1.1
elif 7 <= days_to_trip <= 30:
    luggage_fee *= 1.15
else:
    luggage_fee *= 1.4

final_cost = luggage_fee * pieces_of_luggage
print(f"The total price of bags is: {final_cost:.2f} lv.")