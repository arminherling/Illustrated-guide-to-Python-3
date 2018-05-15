# Exercise: Create a list with the names of friends and colleagues. Search for the name John using
# a for loop. Print not found if you didn’t find it. (Hint: use else).

names = ["Armin", "Maximilian", "Tombias", "Sascha"]

for name in names:
    if name == "John":
        break
else:
    print("John was not found in the list")