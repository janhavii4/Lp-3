steps = 0

def recfibonacci_series(n,a=0,b=1):
    global steps
    steps +=1

    if n == 0:
        return

    print(a,end="")
    recfibonacci_series(n-1,b,a+b)

n = int(input("Enter a number:"))

if n <0:
    print("The number is negative")
else:
    print("Fibonnacii series: ")
    recfibonacci_series(n)
    print("\nStep count:", steps)