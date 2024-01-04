jury_members = int(input())
total_sum_grades = 0
presentations_counter = 0

input_line = input()
while input_line != "Finish":
    presentation_name = input_line
    presentation_grades_sum = 0
    presentations_counter += 1

    for presentation in range(jury_members):
        current_grade = float(input())
        presentation_grades_sum += current_grade

    presentation_average_grade = presentation_grades_sum / jury_members
    total_sum_grades += presentation_average_grade
    print(f"{presentation_name} - {presentation_average_grade:.2f}.")
    input_line = input()

final_average_grade = total_sum_grades / presentations_counter
print(f"Student's final assessment is {final_average_grade:.2f}.")
