# Exercise: Create a list of the names of the first names your friends. Create a list with the top ten
# common names. Use set operations to see if any of your friends have common names.

names = set(["Armin", "Peter", "James"])
top_ten = set(["Liam", "Noah", "Elijah", "Logan", "Mason", "James", "Aiden", "Ethan", "Lucas", "Jacob"])
common_names = names & top_ten

print(common_names)