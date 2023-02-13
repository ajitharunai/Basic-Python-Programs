#Fizz Buzz: Write a program that prints the numbers from 1 to 100, but for multiples of 3, it prints "Fizz" instead of the number, and for multiples of 5, it prints "Buzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
