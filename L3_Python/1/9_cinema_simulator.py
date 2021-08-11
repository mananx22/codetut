movies = {
    "jurassic": {"seats":45, "age":18, },
    "wizards": {"seats":3, "age":72, },
    "harry": {"seats":42, "age":6, },
    "lotr": {"seats":11, "age":45, }
}


name = input("enter your name: ").strip().capitalize()
print("hello {}, Please select any one film you want to watch : ".format(name))
print(movies.keys());

selected = input(" enter your movie name : ").strip().lower()
ag = int(input(" enter your age : ").strip())

if ag < movies[selected]["age"]:
    print("sorry my friend, you're not allowed")
else:
    seat = int(input("how many seats you want to book? :"))
    if seat > movies[selected]["seats"]:
            print("sorry my friend, not enough seats avaialbe")
    else:
            print("congratulations, you're booked")
            movies[selected]["seats"] = movies[selected]["seats"] - seat
            print(movies)
            
