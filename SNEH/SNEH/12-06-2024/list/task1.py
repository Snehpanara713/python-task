# Given a list of numbers, write a function that takes the list as input and returns a new list containing only the even numbers from the original list.


def even_only(lst):
    even=[]
    
    for number in lst:
        if number%2==0:
            even.append(number)
            
    return even

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list1=[]

numbers=int(input("Enter number of elements for first list:"))
for i in range(1,numbers+1):
    b=int(input("Enter element:"))
    list1.append(b)
    
    
even_numbers = even_only(list1)
print(even_numbers)