#1344. Angle Between Hands of a Clock
#Author: Ana Luisa Mata
#Given two numbers, hour and minutes. 
#Return the smaller angle (in degrees) 
#formed between the hour and the minute hand.

#Runtime: 24 ms, faster than 89.46% of Python3 online submissions for Angle Between Hands of a Clock.
#Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Angle Between Hands of a Clock.
#Time complexity: O(1)
#Space complexity: O(1)

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minAngle = minutes*6
        hourAngle = float(hour*30 + (minutes*.5))
        
        angle = abs(hourAngle-minAngle)
        angle = min(360 - angle, angle) 
        
        return angle
