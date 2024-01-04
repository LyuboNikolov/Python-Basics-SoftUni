hall_rent = int(input())
statuettes_price = hall_rent * 0.7
catering_price = statuettes_price * 0.85
sound_price = catering_price * 0.5
total_price = hall_rent + statuettes_price + catering_price + sound_price
print(f"{total_price:.2f}")

