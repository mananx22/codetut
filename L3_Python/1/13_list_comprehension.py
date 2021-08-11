even = [x for x in range(0,101) if x%2 ==0]
print (even)

odd = [x for x in range(0,101) if x%2 !=0]
print (odd)

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
answer = [[w.upper(), w.lower(), len(w)] for w in words ]
print(answer)