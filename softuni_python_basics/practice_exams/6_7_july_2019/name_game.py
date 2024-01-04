name = input()
best_points = 0
winner = ""

while name != "Stop":
    current_points = 0
    for i in range(len(name)):
        number = int(input())
        if number == ord(name[i]):
            current_points += 10
        else:
            current_points += 2
        if current_points >= best_points:
            best_points = current_points
            winner = name
    name = input()
print(f"The winner is {winner} with {best_points} points!")
