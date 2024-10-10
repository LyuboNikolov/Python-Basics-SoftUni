poor_grades_limit = int(input())
grades_sum = 0
poor_grades_counter = 0
problems_counter = 0
last_problem = ""

while True:
    command = input()
    if command == "Enough":
        average_grade = grades_sum / problems_counter
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {problems_counter}")
        print(f"Last problem: {last_problem}")
        break
    last_problem = command
    grade = int(input())
    problems_counter += 1
    grades_sum += grade

    if grade <= 4:
        poor_grades_counter += 1
    if poor_grades_counter == poor_grades_limit:
        print(f"You need a break, {poor_grades_counter} poor grades.")
        break
