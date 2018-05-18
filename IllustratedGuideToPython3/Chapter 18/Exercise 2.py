# Exercise: Create a variable, filename. Assuming that it has a three letter extension, and using
# slice operations, find the extension. For README.txt, the extension should be txt.
# Write code using slice operations that will give the name without the extension. Does
# your code work on filenames of arbitrary length?

def filename(filename):
    return filename[:-4]

def extension(filename):
    return filename[-3:]


fullname = "README.txt"

print(fullname)
print(filename(fullname))
print(extension(fullname))
