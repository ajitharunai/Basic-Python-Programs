#Palindrome: Write a program that checks if a given string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")

if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
