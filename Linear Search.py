#Linear Search: Write a program that performs a linear search on a list of numbers.

def linear_search(numbers, key):
    for i, num in enumerate(numbers):
        if num == key:
            return i
    return -1

numbers = [int(x) for x in input("Enter a list of numbers: ").split()]
key = int(input("Enter the search key: "))

result = linear_search(numbers, key)

if result == -1:
    print("The key was not found in the list")
else:
    print("The key was found at index", result)
