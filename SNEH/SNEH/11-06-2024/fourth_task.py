# Write a function to reverse a string without using built-in functions.


def reverse(string):
    string_reverse = string[::-1]
    return string_reverse


s = input("Enter a string:-")

print("the original string is :", end="")

print(s)

print("the reversed string is :", end="")

print(reverse(s))
