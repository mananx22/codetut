# unless return is mentioned no number is stored in a function. print does not return anything.
# in python functions create local scopes, where as loops & if statements dont.


def add(x,y):
    c = x+y
    return c
print(add(5,10))


def word(k):
    print(k[::-1])
w = input("Enter your string")
word(w)

