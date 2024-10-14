#Write a code to check whether a given number is a palindrome.

#first method to check wether number is palindrome
def checkPalindrome1(number):
    reverse = 0
    tempNumber = number
    while(tempNumber>0):
        digit = tempNumber%10
        tempNumber = tempNumber//10
        reverse = (reverse*10)+ digit
    if(reverse==number):
        print("Number is a palindrome")
    else:
        print("Number is not a palindrome")

#second method to check wether number is palindrome or not
def checkPalindrome2(number):
    number = str(number)
    if number == number[::-1]:
        print("Number is a palindrome")
    else:
        print("Number is not a palindrome")


        

#main function
def main():
    number = int(input("Enter a Number : "))
    checkPalindrome1(number)
    checkPalindrome2(number)

if __name__ == "__main__":
    main()