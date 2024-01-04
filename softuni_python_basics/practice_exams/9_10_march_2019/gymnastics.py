country = input()
apparatus = input()

difficulty_rating = 0
performance_rating = 0


if apparatus == "ribbon":
    if country == "Russia":
        difficulty_rating = 9.100
        performance_rating = 9.400
    elif country == "Bulgaria":
        difficulty_rating = 9.600
        performance_rating = 9.400
    elif country == "Italy":
        difficulty_rating = 9.200
        performance_rating = 9.500
elif apparatus == "hoop":
    if country == "Russia":
        difficulty_rating = 9.300
        performance_rating = 9.800
    elif country == "Bulgaria":
        difficulty_rating = 9.550
        performance_rating = 9.750
    elif country == "Italy":
        difficulty_rating = 9.450
        performance_rating = 9.
elif apparatus == "rope":
    if country == "Russia":
        difficulty_rating = 9.600
        performance_rating = 9.000
    elif country == "Bulgaria":
        difficulty_rating = 9.500
        performance_rating = 9.400
    elif country == "Italy":
        difficulty_rating = 9.700
        performance_rating = 9.150

total_rating = difficulty_rating + performance_rating
percent_needed_to_max = (1 - (total_rating / 20)) * 100

print(f"The team of {country} get {total_rating:.3f} on {apparatus}.")
print(f"{percent_needed_to_max:.2f}%")