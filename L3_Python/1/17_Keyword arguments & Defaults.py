# defining defaults within functions
def exp(name="jack",age=9,like="nothing"):
    return "Hi {0}, your age is {1} and you like {2}".format(name,age,like)

# Keyword arguments ( arguments passed in no order)
print(exp(age=35, name="manan"))