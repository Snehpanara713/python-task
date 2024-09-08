# -	Create a function longest_palindromic_subsequence(s: str) -> int that finds the length of the longest palindromic subsequence in a given string.
# 	Explanation: This task involves dynamic programming to find the longest subsequence that reads the same backward as forward.

def isPalindrome(s:str)-> int:
    def expend_around_center(left:int,right:int)->int:
        while left>=0 and right < len(s) and s[left]==s[right]:
            
            left-=1
            right+=1
            
        return right-left-1
    
    if not s:
        return 0
    
    max_length=0
    for i in range (len(s)):
        len1=expend_around_center(i,i)
        len2=expend_around_center(i,i+1)
        max_length=max(max_length,len1,len2)
        
    return max_length


s="babad"
print(isPalindrome(s))