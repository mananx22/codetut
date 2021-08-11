students = {
    "male":["manan", "bob", "johnny", "hercules"],
     "female":["taylor", "britanny", "cassidy", "emily"]    
     }


for iterable in students.keys():
 for anything in students[iterable]:
    if "n" in anything:
     print(anything)