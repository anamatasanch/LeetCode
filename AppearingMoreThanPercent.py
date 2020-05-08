#1287. Element Appearing More Than 25% In Sorted Array
#Author: Ana Luisa Mata

#Given an integer array sorted in non-decreasing order, 
#there is exactly one integer in the array that occurs 
#more than 25% of the time.
#Return that integer.

#Runtime: 88 ms, faster than 90.71% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
#Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
#Time complexity: O(n)
#Space complexity: O(1)

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        target = len(arr)*0.25
        
        curr = arr[0]
        count = 1
        for i in range(1,len(arr)):
            if count > target:
                return curr
            elif arr[i]!=curr:
                count = 1
                curr = arr[i]
            elif arr[i] == curr:
                count+=1
        
        return curr
        
