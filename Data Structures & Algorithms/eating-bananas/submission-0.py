import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        result = high 

        while low <= high:
            speed = (low + high) // 2
            
            total_hour = 0
            for pile in piles:
                total_hour += math.ceil(pile / speed)
            
            if total_hour <= h:
                result = speed
                high = speed - 1
            else:
                low = speed + 1
                
        return result