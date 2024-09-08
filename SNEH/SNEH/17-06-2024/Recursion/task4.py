# Write a function that checks if a given string is a palindrome (reads the same forwards and backward), ignoring spaces and letter casing.


def isPalindrome(s):
    s=''.join(c for c in s.lower() if c.isalnum())
    return s==s[::-1]

s= "A man, a plan, a canal: Panama"

ans=isPalindrome(s)

if ans:
    
    print("yes")
    
else:
    print("no")

