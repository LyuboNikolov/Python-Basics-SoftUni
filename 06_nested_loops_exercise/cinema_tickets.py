student_tickets = 0
standard_tickets = 0
kid_tickets = 0

movie_name = input()
while movie_name != "Finish":
    seats = int(input())
    movie_tickets = 0

    for seat in range(seats):
        current_ticket = input()
        if current_ticket == "End":
            break
        elif current_ticket == "student":
            student_tickets += 1
        elif current_ticket == "standard":
            standard_tickets += 1
        elif current_ticket == "kid":
            kid_tickets += 1

        movie_tickets += 1
    percent_hall_fullness = movie_tickets / seats * 100
    print(f"{movie_name} - {percent_hall_fullness:.2f}% full.")
    movie_name = input()

total_tickets = student_tickets + standard_tickets + kid_tickets
percent_student_tickets = student_tickets / total_tickets * 100
percent_standard_tickets = standard_tickets / total_tickets * 100
percent_kid_tickets = kid_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")
