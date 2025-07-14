#Write a code to find the sum of numbers divisible by 4.The code must allow the user to accept a number and add it to the sum if it is divisible by 4. It should continue accepting numbers as long as the user wants to provide an input and should display the final sum.

def sumNumbers():
    sum=0
    while(True):
        try:
            number = int(input("Enter a number or press E for skip"))
            if number%4==0:
                sum = sum+number
        except ValueError:
            break
    return sum

def main():
    result = sumNumbers()

    print(f"The sum of numbers is {result}")

if __name__=="__main__":
    main()