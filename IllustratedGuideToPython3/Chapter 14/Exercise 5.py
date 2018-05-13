# Exercise: Tuples and lists are similar but have different behavior. Use set operations to find the
# attributes of a list object that are not in a tuple object.

list_attributes = set(dir([]))
tuple_attributes = set(dir((1,1)))

unique_list_attributes = list_attributes - tuple_attributes

print("List:", list_attributes)
print("Tuple:", tuple_attributes)
print("")
print("Unique list attributes:", unique_list_attributes)