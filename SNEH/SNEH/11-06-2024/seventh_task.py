# Write a function to flatten a nested list.

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# def flatten_list(nested_list):
#     flat_list = []
#     for sublist in nested_list:
#         for item in sublist:
#             flat_list.append(item)
#     return flat_list


# flat_list = flatten_list(nested_list)
# print(flat_list)




def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

# Take user input and convert it to a nested list
nested_list_input = input("Enter a nested list (e.g., [[1, 2, 3], [4, 5, 6], [7, 8, 9]]): ")
nested_list = eval(nested_list_input)

# Flatten the nested list
flat_list = flatten_list(nested_list)
print("Flattened list:", flat_list)










