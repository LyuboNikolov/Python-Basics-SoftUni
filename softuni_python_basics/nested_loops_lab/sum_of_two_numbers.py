start_number = int(input())
end_number = int(input())
magic_number = int(input())
combination_counter = 0
combination_is_found = False

for first_number in range(start_number, end_number + 1):
    for second_number in range(start_number, end_number + 1):
        combination_counter += 1
        if first_number + second_number == magic_number:
            combination_is_found = True
            print(f"Combination N:{combination_counter} ({first_number} + {second_number} = {magic_number})")
            break
    if combination_is_found:
        break

if not combination_is_found:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
