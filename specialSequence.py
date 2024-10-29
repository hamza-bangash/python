#You are tasked with writing a program that finds and prints a special sequence of integers in reverse order using while loop, following these rules:
#Starting number: The user inputs a positive integer N.
#Reduction process: Starting from N, repeatedly do the following:
#If the number is even, divide it by 2.
#If the number is odd, multiply it by 3 and add 1.
#Continue until the number reaches 1.
#Reversing the sequence: Print all the numbers encountered during this process in reverse order (i.e., starting from 1 and ending at N).
#Loop Condition: You must use a while loop to implement the process. Do not use any other types of loops.
#Challenge: You are not allowed to use arrays, vectors, or any data structures that would directly store the sequence beforehand. Instead, you must find a way to reverse the output through logic.

def sequence(number):
    count=0
    tempNumber =number
    print("\nThe Sequence is : ",end=" : ")
    while(tempNumber!=1):
        if(tempNumber%2==0):
            tempNumber=tempNumber/2
        else:
            tempNumber = (tempNumber*3)+1
        count+=1
    

    while(count>=0):
        tempNumber = number
        currentCount=0

        while(currentCount<count):
            if(int(tempNumber%2)==0):
                tempNumber =tempNumber/2
            else:
                tempNumber = (tempNumber*3)+1
            currentCount = currentCount + 1

        print(int(tempNumber),end=" ")
        count = count -1


def main():
    number = int(input("\nEnter a number : "))   
    sequence(number) 

if(__name__=="__main__"):
    main()
