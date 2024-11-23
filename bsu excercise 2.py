#linear search test
L= []
def linearsearch(data):
    index = 0
    while index < len(L):
        if data == L[index]:
            return index
        index = index + 1

size = int(input("what is the size?"))
for x in range(size):
    data = int(input("enter the data"))
    L.append(data)
print(" the old array:", L)

searchitem = int(input("What's the item that needs to be searched? "))
state = linearsearch(searchitem)
if state is not None:
    print("found")
else:
    print("not found")
    
