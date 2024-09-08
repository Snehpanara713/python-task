# Write a function that takes two lists as input and returns a new list that contains the elements that are unique to each list (i.e., not common to both lists).

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        x= list((a_set & b_set))
        print(x)
    else:
        print("No common elements") 
          
  
list1 = []
num1 = int(input("Enter number of elements for the first list: "))
for i in range(num1):
    element = int(input(f"Enter element : "))
    list1.append(element)


list2 = []
num2 = int(input("Enter number of elements for the second list: "))
for i in range(num2):
    element = int(input(f"Enter element : "))
    list2.append(element)
    
common_member(list1, list2)


        
  
