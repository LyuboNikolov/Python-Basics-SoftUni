actor_name = input()
initial_points = float(input())
reviewers_number = int(input())
total_points = initial_points
is_nominated = False

for actor in range(reviewers_number):
    current_reviewer = input()
    reviewer_points = float(input())

    total_points += len(current_reviewer) * reviewer_points / 2

    if total_points > 1250.5:
        is_nominated = True
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break

if not is_nominated:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
