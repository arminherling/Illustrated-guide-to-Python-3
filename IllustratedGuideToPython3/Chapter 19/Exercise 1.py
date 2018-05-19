# Exercise: Write a function to write a comma separated value (CSV) file. It should accept a
# filename and a list of tuples as parameters. The tuples should have a name, address,
# and age. The file should create a header row followed by a row for each tuple. If the
# following list of tuples was passed in:

# [('George', '4312 Abbey Road', 22),
# ('John', '54 Love Ave', 21)]

# it should write the following in the file:

# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21

def create_csv(collection, header1, header2, header3):
    output = []
    output.append(tuple_to_comma_seperated((header1, header2, header3)))
    for line in collection:
        output.append(tuple_to_comma_seperated(line))

    return output


def tuple_to_comma_seperated(tuple):
    return ",".join(str(item) for item in tuple)


data = [('George', '4312 Abbey Road', 22),
        ('John', '54 Love Ave', 21)]

lines = create_csv(data, "name", "address", "age")

with open("/test.txt", "w") as file:
    for line in lines:
        file.write(line+"\n")
