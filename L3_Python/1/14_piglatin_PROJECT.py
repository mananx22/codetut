given = input("Enter your sentence: ").strip().split()
print(given)

midvow=midcons=string=""

for inpu in given: 
    for i in inpu:   
        if i in "aeiouAEIOU":
            midvow = inpu[inpu.index(i): len(inpu)]
            midcons = inpu[0:inpu.index(i)]            
            break

    if inpu[0] in "aeiouAEIOU":
     string = string + inpu + "yay "
    else:
     string = string + midvow + midcons + "ay " 
print(string)

