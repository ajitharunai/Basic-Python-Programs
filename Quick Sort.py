#3Quick Sort: Write a program that implements the quick sort algorithm to sort a given list of numbers.

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    left = [x for x in numbers[1:] if x <= pivot]
    right = [x for x in numbers[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

sorted_numbers = quick_sort(numbers)

print("Sorted list:", sorted_numbers)

  
