#Reverse a List: Write a program that reverses a given list.

def reverse_list(lst):
    return lst[::-1]

list = [1, 2, 3, 4, 5]

reversed_list = reverse_list(list)

print("Original list:", list)
print("Reversed list:", reversed_list)
