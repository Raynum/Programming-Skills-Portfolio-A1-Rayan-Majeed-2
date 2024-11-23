#Exercise 6:  Brute Force Attack

def security():
    imax = 5
    for i in range(imax):
        password = int(input('Enter a password'))
        while password == 12345:
            print("correct")
            return
        else:
            print("retry")

    print("too many attempts, try again later")

security()
x
