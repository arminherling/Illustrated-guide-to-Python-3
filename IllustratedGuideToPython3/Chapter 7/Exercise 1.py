# Exercise: Create a variable that points to a floating point number.  Examine
# the id, type, and value of that number.  Update the variable by adding 20 to
# it.  Re-examine the id, type, and value.  Did the id change?  Did the value
# change?

float_number = 3.14
print('ID:', id(float_number))
print('Type:', type(float_number))
print('Value:', float_number)

float_number = float_number + 20
print('ID:', id(float_number))
print('Type:', type(float_number))
print('Value:', float_number)