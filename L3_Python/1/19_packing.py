# now suppose if we want to unpack an entire dictionary
def exp(name="jack",age=9,like="nothing"):
    return "Hi {0}, your age is {1} and you like {2}".format(name,age,like)

dictionary={ "age":32,
             "name":"manan",
             "like":"anything"
             }
# let's parse the above dictionary in exp function unpacked. order doesn't matter
# we put ** TWO STARS instead of one, for key-value pair unpacking
print(exp(**dictionary))