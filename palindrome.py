
#function that checks if a word is a palindrome
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
print(palindrome("anna"))    
