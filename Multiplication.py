# Program to find the product of two numbers

# Function to calculate the product
def multiply(a, b):
    return a * b

# Input numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call the function and print the result
result = multiply(num1, num2)
print("The product of", num1, "and", num2, "is", result)
