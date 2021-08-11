# STRING METHODS

# 1 how many times a certain character appear?
msg = "hello".count("l")
print( "1 " + str( msg ))

# 2 another way
msg = "hello"
print("2 " + str( msg.count("ell") ))

# 3 lower case without modifying varible originally
msg = "GOOd MOrning"
print("3 " + str( msg.lower() ))

# 4 Upper case without modifying varible originally
msg = "GOOd MOrning"
print("4 " + str( msg.upper() ))

# 5 Capitalize
msg = "GOOd MOrning"
print("5 " + str( msg.capitalize() ))

# 6 Title
msg = "GOOd MOrning"
print("6 " + str( msg.title() ))



# 7 To check if any condition or text is already in title or other case
print( msg.istitle() )

# 8 to return index of a substring within provided string ( return an error if 
# substring not found. HARDSTOP)
msg = "GOOd MOrning"
print("8 " + str( msg.index("MOrn") ))


# 9 to return index of a substring within provided string ( return a -1 if 
# substring not found.SOFTSTOP)
msg = "GOOd MOrning"
print("9 " + str( msg.find("MOrn") ))


# 10 to strip away a certain character from a given string
# TO REMOVE ONLY SPACE USE strip()
msg = "000000000GOOd MOrning000000000000000"
print("10 " + str( msg.strip("0") ))

# 11 to strip away a certain character from a given string " LEFT SIDE"
msg = "000000000GOOd MOrning000000000000000"
print("11 " + str( msg.lstrip("0") ))

# 12 to strip away a certain character from a given string " RIGHT SIDE"
msg = "000000000GOOd MOrning000000000000000"
print("12 " + str( msg.rstrip("0") ))

#13 to slice up astring we use, string[start:end:steps]
# here we are reversing the entire string
msg = "000000000GOOd MOrning000000000000000"
print("13 " + str( msg[::-1] ))

#14 convert string to boolean
msg = bool("True")
print(type(msg))
