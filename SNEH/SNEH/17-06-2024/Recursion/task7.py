# Write a program that performs operations on lists, such as finding the maximum element, sorting, and removing duplicates.


my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

max_element = max(my_list)
print("maximum number:",max_element)



x=my_list.sort()
print("Sorted list:", x)

unique_list = list(set(my_list)) 
print(unique_list)
