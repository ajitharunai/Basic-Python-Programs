#Armstrong Number: Write a program that checks if a given number is an Armstrong number or not.

def is_armstrong(n):
    num_str = str(n)
    length = len(num_str)
    sum = 0
    for char in num_str:
        sum += int(char)**length
    return sum == n

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
