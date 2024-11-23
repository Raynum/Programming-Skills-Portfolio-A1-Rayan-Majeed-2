#excerise 10

def oddoreven():
    global num
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

def userinput():
    global num
    num = int(input("Enter your number :"))


def main():
    userinput()
    oddoreven()

main()
