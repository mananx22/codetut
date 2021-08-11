a = 250

def f1():
    # here by defining a variable under global, the global variable is affected and replaced. 
    # This does not hold true for list & dictionaries
    global a 
    a = 100
    print(a)

def f2():
    # global a 
    a = 50
    print(a)

f1()
f2()
print(a)