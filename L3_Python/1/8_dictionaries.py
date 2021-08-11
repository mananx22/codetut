# in dictionaries, each item has a key and value
# dictionaries does not have any index. the only way to access any item is through its keys

students={}
students = {"manan":25, "bob":23, "Claire":14, "distro":74 }
students["manan"] = 3
del students["bob"]
print(students)


print(students.keys())
a = list(students.keys())
print(a[2])

students = {
    "manan":["ID001", 25, "A"],
    "bob":["ID002", 234, "A"], 
    "Claire":["ID003", 23, "A"], 
    "distro":["ID004", 54, "A"]  
    }
print(students["Claire"][0])
print(students["bob"][2])


# multiple dictionaries
students = {
    "manan":{ "id":"ID001", "age":25, "grade":"A"},
    "bob":{ "id":"ID002", "age":234, "grade":"A"}, 
    "Claire":{ "id":"ID003", "age":23, "grade":"A"}, 
    "distro":{ "id":"ID004", "age":54, "grade":"A"}  
    }
print(students["Claire"]["age"])
print(students["bob"]["grade"])


