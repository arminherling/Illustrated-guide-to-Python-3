# Exercise: Create a string, filename, that has the value 'hello.py'. Check and see if the
# filename ends with '.java'. Find the index location of 'py'. See if it starts with
# 'world'.

filename = "hello.py"

print(filename, "ends with '.java'", filename.endswith(".java"))
print("Index of 'py' in", filename, "is", filename.index("py"))
print(filename, "starts with 'world'", filename.startswith("world"))