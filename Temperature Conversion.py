#Temperature Conversion: Write a program that converts degrees from Celsius to Fahrenheit and vice versa.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = int(input("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter your choice: "))

if choice == 1:
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit:", fahrenheit)
elif choice == 2:
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("Temperature in Celsius:", celsius)
else:
    print("Invalid choice.")
