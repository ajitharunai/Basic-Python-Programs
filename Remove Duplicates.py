#Remove Duplicates: Write a program that removes duplicate elements from a given list.

def remove_duplicates(lst):
    return list(set(lst))

my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4]

print("Original list:", my_list)
print("List without duplicates:", remove_duplicates(my_list))
