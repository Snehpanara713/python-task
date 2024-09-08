# Implement a function that calculates the sum of the digits of a positive integer.

def positive_sum(arr):
    total=0
    for i in arr:
        if i>0:
            total=total+i
            
    return total

arr=[-1, 1, -2, 2]
call=positive_sum(arr)
print(call)
