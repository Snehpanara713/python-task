# Write a function that takes a list as input and returns a new list with the elements reversed, without using the built-in reverse method.

def Reverse(lst):
    new_lst=lst[::-1]
    
    return new_lst


lst=[]
num1=int(input("Enter number of elements for the list: "))
for i in range (num1):
    ele=int(input(f"Enter a element: "))
    lst.append(ele)
    
result=Reverse(lst)
print(result)