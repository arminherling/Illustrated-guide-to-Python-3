# Exercise: Write a function that reads a CSV file. It should return a list of dictionaries, using the
# first row as key names, and each subsequent row as values for those keys. For the data
# in the previous example it would return:

# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22},
# {'name': 'John', 'address': '54 Love Ave', 'age': 21}]

def read_csv(filename):
    file = open("/test.txt")
    people = []
    all_lines = file.readlines()
    headers = all_lines[:1][0].replace("\n","").split(",")
    all_values = all_lines[1:]

    for line in all_values:
        values = line.replace("\n","").split(",")
        person = {}
        for i, header in enumerate(headers):
            person[header] = values[i]

        people.append(person)

    return people


print(read_csv("/test.txt"))