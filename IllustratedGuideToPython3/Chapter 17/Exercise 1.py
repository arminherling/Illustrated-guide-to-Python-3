# Exercise: Write a function, is_odd, that takes an integer and returns True if the number is odd
# and False if the number is not odd.

def is_odd(number):
    return number % 2 != 0

print(0, "is odd", is_odd(0))
print(1, "is odd", is_odd(1))
print(2, "is odd", is_odd(2))
print(3, "is odd", is_odd(3))
print(4, "is odd", is_odd(4))