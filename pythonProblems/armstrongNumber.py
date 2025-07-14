#A three digit number is said to be an “Armstrong number” if the sum of the third power of its individual digits is equal to the number itself.Write a program to check whether a number is armstrong or not.


#first method 
def armstrongNumber1(number):
    resultNumber=0
    numberOfDigit = len(str(number))
    tempNumber = number
    while(tempNumber>0):
        digit = tempNumber%10
        tempNumber = tempNumber//10
        resultNumber = digit**numberOfDigit + resultNumber
    print("\nFirst Method")
    if(resultNumber == number):
        print("ArmstrongNumber")
    else:
        print("Not a ArmstrongNumber")

#Second method
def armstrongNumber2(number):
    listOfDigit = [int(digit) for digit in str(number)]
    resultNumber=0
    numberOfDigit = len(listOfDigit)
    for digit in listOfDigit:
        resultNumber = digit**numberOfDigit + resultNumber

    print("\nSecond method")
    if(resultNumber==number):
        print("ArmstrongNumber")
    else:
        print("Not a ArmstrongNumber")





def main():
    number = int(input("\nEnter any Number : "))
    armstrongNumber1(number)
    armstrongNumber2(number)


if(__name__=="__main__"):
    main()