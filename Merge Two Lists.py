#Merge Two Lists: Write a program that merges two given lists into a new list.

def merge_lists(list1, list2):
    return list1 + list2

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print("First list:", list1)
print("Second list:", list2)
print("Merged list:", merge_lists(list1, list2))
