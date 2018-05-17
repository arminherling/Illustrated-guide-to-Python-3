# Exercise: Write a function, is_prime, that takes an integer and returns True if the number is
# prime and False if the number is not prime.

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif not number & 1:
        return False

    for n in range(3, int(number**0.5)+1, 2):
        if number % n == 0:
            return False

    return True

print(1, "is prime", is_prime(1))
print(2, "is prime", is_prime(2))
print(3, "is prime", is_prime(3))
print(29, "is prime", is_prime(29))
print(49, "is prime", is_prime(49))
print(95, "is prime", is_prime(95))
print(345, "is prime", is_prime(345))
print(999979, "is prime", is_prime(999979))
print(999981, "is prime", is_prime(999981))