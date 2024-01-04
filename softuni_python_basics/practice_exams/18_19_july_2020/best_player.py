import sys

football_player = input()
max_goals = -sys.maxsize
best_player = " "

while football_player != "END":
    goals_scored = int(input())
    if goals_scored > max_goals:
        max_goals = goals_scored
        best_player = football_player
    if goals_scored >= 10:
        break
    football_player = input()
print(f"{best_player} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")

