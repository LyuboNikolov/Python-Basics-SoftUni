steps_goal = 10000
steps_counter = 0
goal_is_reached = False

while True:
    command = input()
    if command == "Going home":
        steps_to_return = int(input())
        steps_counter += steps_to_return
        if steps_counter >= steps_goal:
            goal_is_reached = True
        break

    steps_walked = int(command)
    steps_counter += steps_walked

    if steps_counter >= steps_goal:
        goal_is_reached = True
        break

diff = steps_counter - steps_goal
if goal_is_reached:
    print(f"Goal reached! Good job!\n{diff} steps over the goal!")
else:
    print(f"{abs(diff)} more steps to reach goal.")
