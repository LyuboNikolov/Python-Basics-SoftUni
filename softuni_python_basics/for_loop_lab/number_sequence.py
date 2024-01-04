from sys import maxsize

numbers_count = int(input())
min_number = maxsize
max_number = -maxsize

for number in range(numbers_count):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number

    if current_number < min_number:
        min_number = current_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
