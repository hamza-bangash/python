#Write a code to find the minimum among three given numbers.

def minimum(number1,number2,number3):
    if(number1<number2 and number1<number3):
        return number1
    elif(number2<number1 and number2<number3):
        return number2
    elif(number3<number1 and number3<number2):
        return number3
    else:
        return None

def main():
    print("Enter three un Equal number")
    number1 = float(input("Enter a first Number : "))
    number2 = float(input("Enter a Second Number : "))
    number3 = float(input("Enter a third Number : "))

    minimumNumber = minimum(number1,number2,number3)
    if(minimumNumber==None):
        print("invalid input")
    else:
        print(f"Minimum number is {minimumNumber}")


if __name__=="__main__":
    main()

