# Exercise: Create a list with the names of friends and colleagues.  Calculate
# the average length of the names.

names = ["Armin", "Maximilian", "Tombias", "Sascha"]

letter_count = 0
for name in names:
    for letter in name:
        letter_count += 1

average_letter_count = letter_count / len(names)

print("The average number of letters in", names, "is", average_letter_count)