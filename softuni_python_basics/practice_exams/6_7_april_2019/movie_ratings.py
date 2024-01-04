number_of_movies = int(input())
min_rating = 10
max_rating = 1
total_rating = 0
movie_highest_rating = " "
movie_lowest_rating = " "

for movies in range(number_of_movies):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating
    if movie_rating > max_rating:
        max_rating = movie_rating
        movie_highest_rating = movie_name
    if movie_rating < min_rating:
        min_rating = movie_rating
        movie_lowest_rating = movie_name

average_rating = total_rating / number_of_movies
print(f"{movie_highest_rating} is with highest rating: {max_rating:.1f}")
print(f"{movie_lowest_rating} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
