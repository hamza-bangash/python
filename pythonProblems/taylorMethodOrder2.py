def givenFunction(y,t):
    return (1+(y/t))

def derivateFunction(y,t):
    return (1/t)



def main():
    # input values
    startValue = float(input("Enter the value of a : "))
    EndValue = float(input("Enter the value of b : "))
    h = float(input("Enter value of h : "))

    w = float(input("Enter the intial Value : "))

    iteration = int((EndValue-startValue)/h)
    print(f"w0 = {w}")
    for i in range(0,iteration):
        t = (startValue + (i*h))
        w = (w + (h *givenFunction(w,(t)))+ ((h*h)/2)*derivateFunction(w,t))

        print(f"w{i+1} = {w}")

main()