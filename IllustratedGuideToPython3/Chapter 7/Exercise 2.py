# Exercise: Create a variable pointing to an empty list.  Examine the id, type,
# and value of the list.  Append the number 300 to the list.  Re-examine the
# id, type, and value.  Did the id change?  Did the value change?

list = []
print('ID:', id(list))
print('Type:', type(list))
print('Value:', list)

list.append(300)
print('ID:', id(list))
print('Type:', type(list))
print('Value:', list)
