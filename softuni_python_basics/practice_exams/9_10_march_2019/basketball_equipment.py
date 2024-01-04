annual_fee = int(input())
sneakers = annual_fee * 0.6
kit = sneakers * 0.8
ball = kit * 0.25
accessories = ball * 0.2
total = annual_fee + sneakers + kit + ball + accessories
print(f"{total:.2f}")
