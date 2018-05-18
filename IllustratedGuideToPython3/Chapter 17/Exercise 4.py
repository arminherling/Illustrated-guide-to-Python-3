# Exercise: Write a function that takes camel cased strings (i.e. ThisIsCamelCased), and converts
# them to snake case (i.e. this_is_camel_cased). Modify the function by adding an
# argument, separator, so it will also convert to kebab case (i.e. this-is-camel-case) as
# well.

def case_converter(text, seperator = "_"):
    new_text = []
    for index, letter in enumerate(text):
        if letter.isupper():
            if not index == 0:
                new_text.append(seperator)
            new_text.append(letter.lower())
        else:
            new_text.append(letter)

    return "".join(new_text)


name = "ThisIsCamelCased"

snake_case = case_converter(name)
kebab_case = case_converter(name, "-")

print(snake_case)
print(kebab_case)