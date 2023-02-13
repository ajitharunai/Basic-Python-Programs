#Binary Search: Write a program that performs a binary search on a sorted list of numbers.

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("Enter a number to search: "))

result = binary_search(arr, x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in the list")
