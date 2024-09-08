# Calculate the sum of all elements in a list using recursion.

def recursive_sum(numbers):
    
    if not numbers:
        return 0
    else:
        return numbers[0]+recursive_sum(numbers[1:])
    
elements=[1,2,3,4,5]

total_sum=recursive_sum(elements)
print(total_sum)