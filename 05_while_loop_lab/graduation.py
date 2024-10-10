name = input()
current_class = 0
failed_years = 0
grades_sum = 0

while True:
    grade = float(input())
    current_class += 1
    if grade < 4:
        failed_years += 1
        if failed_years == 2:
            print(f"{name} has been excluded at {current_class} grade")
            break
        current_class -= 1
    else:
        grades_sum += grade

    if current_class == 12:
        average_grade = grades_sum / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
