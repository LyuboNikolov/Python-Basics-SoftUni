open_tabs = int(input())
salary = int(input())
copy_salary = salary
is_valid = True

for page in range(open_tabs):
    current_tab = input()
    if current_tab == "Facebook":
        copy_salary -= 150
    elif current_tab == "Instagram":
        copy_salary -= 100
    elif current_tab == "Reddit":
        copy_salary -= 50
    if copy_salary <= 0:
        is_valid = False
        print("You have lost your salary.")
        break

if is_valid:
    print(f"{copy_salary}")
