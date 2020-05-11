#1249. Minimum Remove to Make Valid Parentheses
#Author: Ana Luisa Mata

#Given a string s of '(' , ')' and lowercase English characters. 
#Your task is to remove the minimum number of parentheses ( '(' or ')', 
#in any positions ) so that the resulting parentheses string is valid 
#and return any valid string.

#Runtime: 92 ms, faster than 94.84% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
#Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
#Time complexity: O(n)
#Space complexity: O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sl = list(s)
        stacky = []
        
        for i in range(len(sl)):
            if sl[i] == '(':
                stacky.append(i)
            elif sl[i] == ')':
                if len(stacky)>0:
                    stacky.pop()
                else:
                    sl[i] = ""
        
        while len(stacky)>0:
            sl[stacky.pop()]=""
        
        str1 = ''.join(sl)
        return str1
