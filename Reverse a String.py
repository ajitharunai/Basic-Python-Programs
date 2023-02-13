#Reverse a String: Write a program that reverses a given string.

def reverse_string(s):
    return s[::-1]

string = input("Enter a string: ")

print("The reversed string is:", reverse_string(string))
