from math import floor

word = input()
most_points = 0
most_powerful_word = ""
total_points = 0

while True:
    if word == "End of words":
        break
    current_points = 0

    for char in word:
        current_points = ord(char)
        total_points += current_points
    list_vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y"]
    # if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" \
    #         or word[0] == "u" or word[0] == "y" or word[0] == "A" or word[0] == "E" or \
    #         word[0] == "I" or word[0] == "O" or word[0] == "U" or word[0] == "Y":
    if word[0] in list_vowels:
        total_points *= len(word)
    else:
        total_points /= len(word)
        floor(total_points)

    if total_points >= most_points:
        most_points = total_points
        most_powerful_word = word

    total_points = 0
    word = input()

print(f"The most powerful word is {most_powerful_word} - {most_points}")


