from sys import maxsize

n = int(input())
max_number = -maxsize
total_sum = 0

for number in range(n):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_number:
        max_number = current_number

total_sum -= max_number
diff = abs(total_sum - max_number)
if diff == 0:
    print(f"Yes\nSum = {total_sum}")
else:
    print(f"No\nDiff = {diff}")
