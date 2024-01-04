length = int(input())
width = int(input())
height = int(input())
accessories = float(input())

volume = length * width * height
volume_in_liters = volume / 1000

tank_capacity = volume_in_liters - (accessories / 100 * volume_in_liters)
print(tank_capacity)
