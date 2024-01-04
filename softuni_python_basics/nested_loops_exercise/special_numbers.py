number = int(input())

for num in range(1111, 10000):
    num_as_string = str(num)
    number_is_special = True
    for index, digit in enumerate(num_as_string):
        if int(digit) == 0 or number % int(digit) != 0:
            number_is_special = False
            break

    if number_is_special:
        print(num_as_string, end=" ")
