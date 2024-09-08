# string = input("enter a string:-")

# def string_func(string):
    
#     for i in string:
        
#         frequency=string.count(i)
        
#         print(str(i) + str(frequency), end="")
        

# string_func(string)


def return_non_repeted(s):
    for i in s:
        if s.count(i)==1:
            return i
        
a="abcddccba"
print(return_non_repeted(a))