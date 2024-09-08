# Define a function can_partition(nums: List[int], target_sum: int) -> bool that determines whether it is possible to partition a given set of numbers into two subsets such that the sum of elements in both subsets is equal.
# Explanation: Solving this task involves dynamic programming to check if a subset with a specific sum can be formed.


from itertools import combinations

def car_partition(num,target_sum: int):
    new_list=[]
    
    for i in range (len(num) + 1):
        for j in list(combinations(num,i)):
            
            if sum (j)==target_sum:
                new_list.append(j)
    return new_list

print(car_partition([x for x in range(6)],10))            
                
        