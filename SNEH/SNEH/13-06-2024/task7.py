# -	Design a function find_longest_chain(pairs: List[Tuple[int, int]]) -> int that finds the length of the longest chain of pairs (a, b) where each pair is (a, b) such that b > a.
# 	Explanation: This task challenges you to come up with a greedy algorithm to find the longest chain of pairs.

from typing import List,Tuple


def max_chain_len(p:List[Tuple[int,int]])-> int:
    
    p.sort(key=lambda x:x[1])
    prev= -1e9
    ans = 0
    
    for x in p:
        if x[0]>prev:
            ans +=1
            prev = x[1]
            
    return ans

n=5
p=[
    (5, 24),
    (39, 60),
    (15, 28),
    (27, 40),
    (50, 90)
]

print(max_chain_len(p))
            