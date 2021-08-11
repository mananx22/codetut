knownusers = ["Alice", "Man", "fred", "monk"]
print(len(knownusers))

while True:
    print("hi my name is travis")
    name = input("your name: ").strip().capitalize()
    if name in knownusers:
        print("hello : {0} ".format(name)) 


        remove = input("would you like to be removed?:" ).strip().lower() 
        if remove == "y":
            index = knownusers.index(name)
            del knownusers[index]
            print(knownusers)
        
        add = input("would you like to add any user? :" ).strip().lower()
        if add == "y":
            user = input("enter name of user :" ).strip().capitalize()
            # a new way to add user to list. we can use append() as usual
            knownusers = knownusers + [user]
            print(knownusers)
        break

    else:
        print("name not recognized") 