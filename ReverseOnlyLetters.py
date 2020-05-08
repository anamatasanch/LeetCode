#917. Reverse Only Letters
#Author: Ana Luisa Mata

#Given a string S, return the "reversed" string 
#where all characters that are not a letter stay 
#in the same place, and all letters reverse their positions.

#Runtime: 24 ms, faster than 92.67% of Python3 online submissions for Reverse Only Letters.
#Memory Usage: Memory Usage: 13.5 MB, less than 5.56% of Python3 online submissions for Reverse Only Letters.
#Time complexity: O(n)
#Space complexity: O(n)

class Solution:
    def isLetter(self, a):
        isValid = False
        
        if ord(a)>=65 and ord(a)<=90:
            isValid=True
        if ord(a)>=97 and ord(a)<=122:
            isValid=True
        
        return isValid
    
    def reverseOnlyLetters(self, S2: str) -> str:
        S = list(S2)    
        i = 0
        j = len(S)-1
        
        while(i<j):
            if self.isLetter(S[i]) == False:
                i+=1
            if self.isLetter(S[j]) == False:
                j-=1
            if self.isLetter(S[i])==True:
                if self.isLetter(S[j])==True:
                    S[i],S[j] = S[j],S[i]
                    i+=1
                    j-=1
        
        return "".join(S)
    
