# Write a function to check if two strings are anagrams.


def check(s1, s2):
    if sorted(s1) == sorted(s2):

        print("The strings are anagrams.")

    else:
        print("The strings  aren't anagrams.")


s1 = input("enter a string_1:")
s2 = input("enter a string_2:")

check(s1, s2)
