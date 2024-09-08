# Given two dictionaries, merge them into a new dictionary, and in case of overlapping keys, combine their values into a list.


from collections import Counter

ini_dictionary1 = {'nikhil': 1, 'akash': 5, 'manjeet': 10, 'akshat': 15}
ini_dictionary2 = {'akash': 7, 'akshat': 5, 'm': 15}

# dict3={**ini_dictionary1,**ini_dictionary2}
# print(dict3)

ini_dictionary_data = Counter({'nikhil': 1, 'akash' : 5,
                    'manjeet' : 10, 'akshat' : 15})
ini_dictionary2_data = Counter({'akash' : 7, 'akshat' : 5,
                                        'm' : 15})

final=ini_dictionary_data+ini_dictionary2_data
print(final)