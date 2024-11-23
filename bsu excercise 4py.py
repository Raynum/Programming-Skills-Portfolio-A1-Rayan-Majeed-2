#Exercise 4:  Primitive Quiz
def quiz():
    print("what is the capital of France?")
    answer = input("Enter your answer")
    print(answer)
    if answer == 'Paris' or answer == 'paris':
        print("correct")
    else:
        print("Wrong")

quiz()
