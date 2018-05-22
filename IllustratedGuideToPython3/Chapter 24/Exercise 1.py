# Exercise: Find a package in the Python standard library for dealing with JSON. Import the
# library module and inspect the attributes of the module. Use the help function to
# learn more about how to use the module. Serialize a dictionary mapping 'name' to
# your name and 'age' to your age, to a JSON string. Deserialize the JSON back into
# Python.

import json

person = {}
person["name"] = "Armin Herling"
person["age"] = 29

print("Person dictionary:", person)

json_string = json.dumps(person)
print("Person dictionary as JSON string:", json_string)

deserialized_person = json.loads(json_string)
print("Deserialized Person dictionary from JSON string:", deserialized_person)
