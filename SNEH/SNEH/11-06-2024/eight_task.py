# Write a function to count the frequency of each character in a string.


string = input("enter a string")

def string_func(string):
    
    for i in string:
        
        frequency=string.count(i)
        
        print(str(i) ,str(frequency), end=" ")
        # print(str(i)  + str(frequency), end=", ")
        

string_func(string)


# a='abbcd'
# for char in a:
#     x=a.count(char)
#     print(char,x,end="")
        

