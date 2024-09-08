# Count the number of elements in a list using recursion.

def recursive_sum(numbers):

    if not numbers:
        return 0
    
    else:
        return 1+recursive_sum(numbers[1:])
        # return recursive_sum(len(numbers))
    
elements=[1,2,3,4,5]

len_ele=recursive_sum(elements)
print(len_ele)