#Write a program that generates a multiplication table for a user-defined range using for
#and nested for loop. The program should prompt the user for two numbers: the starting
#and ending values for the multiplication table. Then, it should print the multiplication
#table for all numbers in that range, including:

def multiplicationTable(start,end):
    total=0
    for i in range(start,end+1):
        print(f"\t{i}",end="")
    print("")
    for i in range(start,end+1):
        sum=0
        print(i,end="")

        for j in range(start,end+1):
            print(f"\t{j} * {i} = {j*i}",end="")
            sum=sum+(j*i)

        print(f"\t| {sum}")
        total = total+sum
    
    print("------------------------")
    print(f"total {total}")


def main():
    multiplicationTable(3,5)

if(__name__=="__main__"):
    main()
