#Qno:Write a program that prompts the user to enter a number between 1 and 30 and prints the
#corresponding day of October. The program should:
# not use more than 7 condition
def weekDays(number):
    if(number>31 and number<1):
        print("\nInvalid number")
        return
    day = number%7
    if(day==1):
        print("Tuesday")
    elif(day==2):
        print("Wednesday")
    elif(day==3):
        print("Thursday")
    elif(day==4):
        print("Friday")
    elif(day==5):
        print("Saturday")
    elif(day==6):
        print("Sunday")
    else:
        print("Monday")

def main():
    number = int(input("Enter any Number between 1 to 31 : "))
    weekDays(number)

if(__name__=="__main__"):
    main()
    