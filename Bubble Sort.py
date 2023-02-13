#Bubble Sort: Write a program that implements the bubble sort algorithm to sort a given list of numbers.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [int(x) for x in input("Enter a list of numbers to be sorted, separated by spaces: ").split()]

print("Sorted list:", bubble_sort(numbers))
