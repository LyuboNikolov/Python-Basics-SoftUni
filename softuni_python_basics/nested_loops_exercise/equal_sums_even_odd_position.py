start_number = int(input())
end_number = int(input())

for number in range(start_number, end_number + 1):
    odd_digits_sum = 0
    even_digits_sum = 0
    number_to_string = str(number)
    for index, digit in enumerate(number_to_string):
        if index % 2 == 0:
            odd_digits_sum += int(digit)
        else:
            even_digits_sum += int(digit)

    if even_digits_sum == odd_digits_sum:
        print(number, end=" ")
