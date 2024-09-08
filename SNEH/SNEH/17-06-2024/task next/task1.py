# Write a function that generates all permutations of a given string.

import itertools  

def unique_permutations(string):
    perams=itertools.permutations(string)
    
    unique_perms =sorted(set(perams))
    
    for data in unique_perms:
        print(''.join(data))
        
string ="ABC"
print(unique_permutations(string))