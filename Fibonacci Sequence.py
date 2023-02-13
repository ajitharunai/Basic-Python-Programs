#Fibonacci Sequence: Write a program that generates the first n numbers in the Fibonacci sequence.

def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Incorrect input")
else:
    print("Fibonacci sequence:")
    for i in range(1, n+1):
        print(fibonacci(i))
