# Write a function to find the missing number in a list of integers from 1 to n.



def find_missing_element(list1):
    missing_ele = []
    for ele in range(list1[0], list1[-1] + 1):  
        if ele not in list1:
            missing_ele.append(ele)
    return missing_ele 

list1 = []
num1 = int(input("Enter number of elements for first list:"))
for i in range(1, num1 + 1):
    b = int(input("Enter element:"))
    list1.append(b)

missing_elements = find_missing_element(list1)

if missing_elements:
    print("Missing elements:", missing_elements)
else:
    print("No missing elements in the list.")

