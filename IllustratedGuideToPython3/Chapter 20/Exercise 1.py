# Exercise: Go to http://unicode.org and download a chart that has code points on it. Choose
# a non-ASCII character and write Python code to print the character by both the code
# point and name.

from_name = "\N{HEAVY MULTIPLICATION X}"
from_code_point = "\u2716"

print(from_name)
print(from_code_point)