# -	Create a function edit_distance(word1: str, word2: str) -> int that calculates the minimum number of operations (insertion, deletion, or substitution) required to convert one word into another.
# 	Explanation: This task involves dynamic programming to find the minimum edit distance between two strings.

def editDistance(str1, str2,m,n):

    if m==0:   # insert all character of second string into first string
        return n
    
    if n==0:    # remove all character of first string
        return m
    
    
    #if last character of two string are same nothing match to do ignore last character 
    if str1[m-1]  == str2[n-1]:
        return editDistance(str1,str2,m-1,n-1)
    
    return 1+min(editDistance(str1,str2,m,n-1),
                 
                 editDistance(str1,str2,m-1,n),
                 
                 editDistance(str1,str2,m-1,n-1)
                 
                 ) 
    
str1 = "GEEXSFRGEEKKS"
str2 = "GEEKSFORGEEKS"

print(editDistance(str1,str2,len(str1),len(str2)))

    