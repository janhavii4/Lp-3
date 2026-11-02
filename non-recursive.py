def fibonacci_series(n):
    a=0
    b=1
    steps=0

    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
        steps += 1

    print("\nStep count:", steps)
    

n=int(input("Enter a number:"))

if n < 0:
    print("The number is negative")
else:
    print("Fibonacci Series: ")
    fibonacci_series(n)