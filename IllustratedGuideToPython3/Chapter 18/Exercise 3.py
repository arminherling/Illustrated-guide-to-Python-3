# Exercise: Create a function, is_palindrome, to determine if a supplied word is the same if the
# letters are reversed.

def is_palindrome(text):
    left = 0
    right = len(text)-1
    while True:
        if right < left:
            return True
        if text[left].lower() == text[right].lower():
            left += 1
            right -= 1
        else:
            return False


print("anna", "is a palindrome", is_palindrome("anna"))
print("car", "is a palindrome", is_palindrome("car"))
print("Racecar", "is a palindrome", is_palindrome("Racecar"))
print("computer", "is a palindrome", is_palindrome("computer"))