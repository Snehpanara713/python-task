# Write a function that takes two dictionaries as input and returns a new dictionary containing key-value pairs that exist in both input dictionaries.


def common_key_value_pairs(user_dict1, user_dict2):

    common_dict = {}

    for key in user_dict1:
        if key in user_dict2:
            if user_dict1[key] == user_dict2[key]:
                # common_dict[key] = user_dict1[key]
                common_dict.update({key: value})

    return common_dict


user_dict1 = {}

num_entries = int(input("Enter the number of entries you want to add dictonary1: "))

for i in range(num_entries):
    key = input("enter a student name:")
    value = int(input("enter a student score:"))
    user_dict1.update({key: value})


user_dict2 = {}

num_entries = int(input("Enter the number of entries you want to add dictonary2: "))

for i in range(num_entries):
    key = input("enter a student name:")
    value = int(input("enter a student score:"))
    user_dict2.update({key: value})


print(user_dict1)
print(user_dict2)

result = common_key_value_pairs(user_dict1, user_dict2)
print("common dictonary:"result)



