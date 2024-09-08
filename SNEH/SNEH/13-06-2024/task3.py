# -	Create a function word_break(s: str, word_dict: List[str]) -> bool that determines if a given string can be segmented into a space-separated sequence of one or more dictionary words.
# 	Explanation: This task involves dynamic programming to check if the input string can be broken down into valid words from the dictionary.


def wordBreak(word):
    word_dict=['samsung','sam','sung'] 
    
    for i in range (len(word)):
         new_word=word[i:]
         
         if new_word in word_dict:
             print(new_word)
             
             return True
         
    return  False

word=input("Enter a string:-")

print(wordBreak(word))
             
         