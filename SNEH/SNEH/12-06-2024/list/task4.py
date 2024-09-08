# Write a function that takes two lists as input and returns a new list containing elements that are common to both input lists (intersection).



def intersection(list1, list2):
    lst = [value for value in list1 if value in list2]
    return lst


list1 = []
num1 = int(input("Enter number of elements for the first list: "))
for i in range(num1):
    element = int(input(f"Enter element : "))
    list1.append(element)


list2 = []
num2 = int(input("Enter number of elements for the second list: "))
for i in range(num2):
    element = int(input(f"Enter element : "))
    list2.append(element)


result = intersection(list1, list2)


print("Common elements:", result)
