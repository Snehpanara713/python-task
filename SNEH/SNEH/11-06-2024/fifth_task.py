# Write a function to determine if a string has all unique characters.



def isUniqueChars(string):
    
    for i in string:
        if string.count(i)>1:
            
            return False
        
    return True

st=input("Enter a string:")
print(isUniqueChars(st))