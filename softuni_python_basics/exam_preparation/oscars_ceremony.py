hall_rent_price = int(input())

statuettes = 0.7 * hall_rent_price
catering = 0.85 * statuettes
sound = 0.5 * catering

total_price = hall_rent_price + statuettes + catering + sound
print(f"{total_price:.2f}")
