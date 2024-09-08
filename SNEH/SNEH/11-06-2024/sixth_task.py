list1=[]
list2=[]
num1=int(input("Enter number of elements for first list:"))
for i in range(1,num1+1):
    b=int(input("Enter element:"))
    list1.append(b)

num2=int(input("Enter number of elements for second list:"))
for i in range(1,num2+1):
    d=int(input("Enter element:"))
    list2.append(d)


def list_data(list1,list2):

    list3=list1+list2
    list3.sort()
    print("Sorted list is:",list3)

list_data(list1,list2)



# def flatten_list(nested_list):
#     flat_list = []
#     for sublist in nested_list:
#         for item in sublist:
#             flat_list.append(item)
#     return flat_list

# # Take user input for the nested list
# nested_list = []
# num_sublists = int(input("Enter the number of sublists: "))

# for i in range(num_sublists):
#     sublist = []
#     num_elements = int(input(f"Enter the number of elements for sublist {i}: "))
#     for j in range(num_elements):
#         element = int(input(f"Enter element {j + 1} for sublist {i + 1}: "))
#         sublist.append(element)
#     nested_list.append(sublist)

# # Flatten the nested list
# flat_list = flatten_list(nested_list)
# print("Flattened list:", flat_list)

