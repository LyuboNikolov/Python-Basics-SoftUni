month = input()
hours_spent = int(input())
number_people = int(input())
time_of_day = input()

price = 0

if month == "march" or month == "april" or month == "may":
    if time_of_day == "day":
        price = 10.5
    elif time_of_day == "night":
        price = 8.4
elif month == "june" or month == "july" or month == "august":
    if time_of_day == "day":
        price = 12.6
    elif time_of_day == "night":
        price = 10.2

if number_people >= 4:
    price *= 0.9

if hours_spent >= 5:
    price *= 0.5

total_price = price * hours_spent * number_people

print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")