#Binary to Decimal: Write a program that converts a binary number to decimal and vice versa.

def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

while True:
    choice = int(input("Enter 1 to convert binary to decimal, 2 to convert decimal to binary, or 0 to quit: "))

    if choice == 0:
        break
    elif choice == 1:
        binary = input("Enter a binary number: ")
        print("Decimal equivalent:", binary_to_decimal(binary))
    elif choice == 2:
        decimal = int(input("Enter a decimal number: "))
        print("Binary equivalent:", decimal_to_binary(decimal))
    else:
        print("Invalid choice")
