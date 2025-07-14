#Write a program that prints a customizable diamond pattern based on user input using for, nested for loop.
#Requirements:
#Input:
#Prompt the user to enter the height of the diamond, which must be an odd integer (e.g., 5,7, 9).
#Prompt the user to enter a character that will be used to draw the diamond (e.g., *, #,etc.).
#Ask the user if they want to print a hollow diamond or a filled diamond by entering y for hollow or n for filled.

def hollowDimandEmpty(height):
    for i in range(0,height): # for height
        for j in range(1,height-i):
            print(" ",end="")
        if(i==0):
            print("*")
        else:
            print("*",end="")
            for k in range(1,i*2):
                print(" ",end="")
            print("*")
    for i in range(0,(height-1)):
        for j in range(0,i+1):
            print(" ",end="")
        if(i==height-2):
            print("*")
        else:
            print("*",end="")
            for j in range(i*2,((height-2)*2)-1):
                print(" ",end="")
            print("*")
def hollowDimandFilled(height):
    for i in range(0,height): # for height
        for j in range(1,height-i):
            print(" ",end="")
        if(i==0):
            print("*")
        else:
            print("*",end="")
            for k in range(1,i*2):
                print("*",end="")
            print("*")
    for i in range(0,(height-1)):
        for j in range(0,i+1):
            print(" ",end="")
        if(i==height-2):
            print("*")
        else:
            print("*",end="")
            for j in range(i*2,((height-2)*2)-1):
                print("*",end="")
            print("*")

def main():
    height = int(input("Enter the height : "))
    choice = int(input("1. for hollowDimandEmpty and 2. hollowDiamandfilled : "))
    if choice==1:
        hollowDimandEmpty(height)
    elif choice==2:
        hollowDimandFilled(height)
    else:
        print("invalid input")

if(__name__=="__main__"):
    main()
            
        
    


    
            