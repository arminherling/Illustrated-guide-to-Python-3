# Exercise: Create a variable, name, set to your name. Create another variable, second_half, that
# tests whether the name would be classified in the second half of the alphabet? What
# do you need to compare it to?

name = "Armin"
alphabet = "abcdefghijklmnopqrstuvwxyz"

first_letter_index = alphabet.find(name[0].lower())
second_half = first_letter_index > 13

print(name, "is in the second half of alphabet:", second_half)