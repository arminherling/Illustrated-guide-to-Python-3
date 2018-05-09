# Exercise: Make a variable, item, that points to a string, "car". Make a variable, cost, that points
# to 13499.99. Print out a line that has item in a left-justified area of 10 characters, and
# cost in a right-justified area of 10 characters with 2 decimal places and commas in the
# thousands place. It should look like this (without the quotes): 'car 13,499.99'

item = "car"
cost = 13499.99
sentence = "{}{:>10,}".format(item, cost)

print(sentence)