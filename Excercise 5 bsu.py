#Exercise 5: Days of the Month
DictMonth = {
    1: 31,  # Jan
    2: 28,  # Feb
    3: 31,  # Mar
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # Aug
    9: 30,  # Sep
    10: 31, # Oct
    11: 30, # Nov
    12: 31  # Dec
}
   
        
def userinput():
    month = int(input("enter a number between 1-12 to choose your month"))
    if month >=1 or month <=12:
        print(f"There are {DictMonth[month]} days in month {month}.")
        
    else:
        print("invalid")
    

userinput()
