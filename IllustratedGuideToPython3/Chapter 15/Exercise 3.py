# Exercise: Create a list of tuples of first name, last name, and age for your friends and colleagues.
# If you don’t know the age, put in None. Calculate the average age, skipping over any
# None values. Print out each name, followed by old or young if they are above or below
# the average age.

names = [("Armin", "Herling", 29), ("Anders", "Zero", 25), ("Julian", "Rob", None)]

average_age = 0
age_counts = 0
for (first, second, age) in names:
    if age is not None:
        average_age += age
        age_counts += 1

average_age /= age_counts

print("The average age is:", average_age)

for (first, second, age) in names:
    if age is None:
        print(first, second, "unknown")
    elif age >= average_age:
        print(first, second, "old")
    else:
        print(first, second, "young")