mutup = 1, 2, 3, "3", "$", "10"
print(type(mutup))

# it is a iterable data type. it store multiple data type
# but we cannot add or subtract elements in tuples through indexes like array
slicing = mutup[0:3]
print("the slicing result is : {}".format(slicing))


# tuple special property of unpacking
my_tuple = 3, 4.6, "dog"
a, b, c = my_tuple

print(a)      # 3
print(b)      # 4.6
print(c)      # dog

