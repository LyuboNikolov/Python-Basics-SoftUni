number_bitcoin = int(input())
yuan_number = float(input())
commission = float(input())

one_bitcoin_price = 1168
one_yuan_price = 0.15
usd_price = 1.76
euro_price = 1.95
fee = commission / 100

total_bitcoin = number_bitcoin * one_bitcoin_price
total_yuan = (yuan_number * 0.15) * usd_price
result = (total_bitcoin + total_yuan) / euro_price
fee = result * fee
result -= fee

print(f'{result:.2f}')