actor = input()
initial_points = float(input())
reviewers = int(input())
total_points = initial_points
nomination_threshold = 1250.5
is_nominated = False

for member in range(reviewers):
    reviewer_name = input()
    reviewer_points = float(input())
    points_received = (len(reviewer_name) * reviewer_points) / 2

    total_points += points_received

    if total_points > nomination_threshold:
        is_nominated = True
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
        break

if not is_nominated:
    points_needed = nomination_threshold - total_points
    print(f"Sorry, {actor} you need {points_needed:.1f} more!")
