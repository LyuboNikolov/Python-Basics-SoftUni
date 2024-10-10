numbers_count = int(input())
odd_sum = 0
even_sum = 0

for number in range(numbers_count):
    current_number = int(input())
    if number % 2 != 0:
        odd_sum += current_number
    else:
        even_sum += current_number

if odd_sum == even_sum:
    print(f"Yes\nSum = {odd_sum}")
else:
    diff = abs(odd_sum - even_sum)
    print(f"No\nDiff = {diff}")
