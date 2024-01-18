kids_counter = 0
adults_counter = 0

command = input()

while command != "Christmas":

    age = int(command)

    if age <= 16:
        kids_counter += 1
    else:
        adults_counter += 1
    command = input()


money_toys = kids_counter * 5
money_sweaters = adults_counter * 15

print(f"Number of adults: {adults_counter}")
print(f"Number of kids: {kids_counter}")
print(f"Money for toys: {money_toys}")
print(f"Money for sweaters: {money_sweaters}")
