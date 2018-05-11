# Exercise: Create a list. Append the names of your colleagues and friends to it. Has the id of the
# list changed? Sort the list. What is the first item in the list? What is the second item in
# the list?
names = []

print("List ID:", id(names))
names.append("Tobias")
names.append("Peter")
names.append("Armin")
print("List ID:", id(names))
names.sort()
print("First", names[0])
print("Second", names[1])