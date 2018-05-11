# Exercise: Create a tuple with your first name, last name, and age. Create a list, people, and
# append your tuple to it. Make more tuples with the corresponding information from
# your friends and append them to the list. Sort the list. When you learn about functions,
# you can use the key parameter to sort by any field in the tuple, first name, last name,
# or age.

me = ("Armin", "Herling", 29)
people = [me]
people.append(("First","Second",20))
people.sort()

print(people)