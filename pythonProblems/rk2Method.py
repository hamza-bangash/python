def givenFunction(t,y):
    return (1+(y/t))


def main():

    startValue = float(input("Enter the value of a : "))
    EndValue = float(input("Enter the value of b : "))
    h = float(input("Enter value of h : "))

    w = float(input("Enter the intial Value : "))

    iteration = int((EndValue-startValue)/h)
    print(f"w0 = {w}")
    for i in range(0,iteration):
        t = (startValue + (i*h))
        k1 = givenFunction(t,w)
        k2 = givenFunction((t+(h/2)) , (w+(h/2)*k1))

        w = w + (h*k2)

        print(f"w{i+1} = {w}")

main()