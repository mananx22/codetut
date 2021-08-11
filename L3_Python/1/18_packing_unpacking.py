numbers = [1,2,3,4,5]
# normal version
print(numbers)
# unpacked version
print(*numbers)

# example of packing, here packed in to a single tuple and looping through tuple
def add(*number):
    total=0
    for num in number:
        total = total + num
    print(total)

add(1,2,3,2,5,78,3,7,9)