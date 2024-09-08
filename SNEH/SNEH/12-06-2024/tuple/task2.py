# Given two tuples, create a new tuple that combines elements from both tuples without any duplicates.


test_tup1 = (1, 3, 5,5)
test_tup2 = (4, 6)

rese=test_tup1+test_tup2
x=set(rese)
tup=tuple(x)
print(tup)