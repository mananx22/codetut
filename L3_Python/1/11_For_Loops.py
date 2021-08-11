###############################################

for i in range(1,11):
    print(i)


###############################################

k=0
y=0
input = input("enter your word : ")
for i in input:    
    if i.lower() in "aeiou":
        k=k+1
    elif i == " ":
        pass
    else:        
        y=y+1
print("no of vowels is : {}".format(k))        
print("no of consonants is : {}".format(y))  

