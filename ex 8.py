#exceecise 8 linear search
#give extra marks for effort :)

List = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

def linearsearch(data):
    index = 0
    while index < len(List):
        if data == List[index]:
            return index
        index = index +1

def userinput():
    searchitem= input("what person needs to be found")
    state = linearsearch(searchitem)
    if state is not None:
        print("Found")
    else:
        print("Not found")
    
    
def main():
    print(List)
    userinput()


    
        
main()    
        
