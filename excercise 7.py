#excercise 7
x=0
y=1
def increment():
    for x in range(50):
        x +=1
        print(x)

def decrement():
    for y in range(51): # changed to 51 to get 0
        y = 50 - y
        print(y)

def thirtytofifty():
    a= 30
    for x in range(20):
        a = a + 1
        print(a)

def fiftytoten():
    for x in range(50, 9, -2): # 9 is stopping point
        print(x)


def hundred():
    for x in range(100, 205, 5): # 205 is the stopping point so it will stop 5 steps back
        print(x)

hundred()
