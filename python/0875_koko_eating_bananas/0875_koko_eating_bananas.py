from typing import List
import math


"""
LeetCode Koko Eating Bananas

Problem from LeetCode: https://leetcode.com/problems/koko-eating-bananas/

Description:
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:
1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
"""

class Solution:

    def min_eating_speed(self, piles: List[int], h: int) ->int:
        """
        Find the minimum eating speed k such that Koko can eat all the bananas within h hours.
        
        Args:
            piles: List of banana piles where piles[i] represents the number of bananas in the ith pile
            h: The maximum number of hours Koko can take to eat all bananas
            
        Returns:
            int: The minimum integer k such that Koko can eat all the bananas within h hours
        """
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if self._can_finish(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left

    def _can_finish(self, piles: List[int], speed: int, h: int) ->bool:
        """
        Check if Koko can eat all bananas within h hours at the given speed.
        
        Args:
            piles: List of banana piles
            speed: Eating speed (bananas per hour)
            h: Maximum hours allowed
            
        Returns:
            bool: True if Koko can finish all bananas within h hours, False otherwise
        """
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
            if hours > h:
                return False
        return True

    def minEatingSpeed_alt(self, piles: List[int], h: int) ->int:
        """
        Alternative implementation with a different binary search approach.
        
        Args:
            piles: List of banana piles
            h: Maximum hours allowed
            
        Returns:
            int: The minimum eating speed required
        """
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            mid = (left + right) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)
            if hours <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    piles1 = [3, 6, 7, 11]
    h1 = 8
    result1 = solution.min_eating_speed(piles1, h1)
    print(f"Example 1: {result1}")  # Expected: 4
    
    # Example 2
    piles2 = [30, 11, 23, 4, 20]
    h2 = 5
    result2 = solution.min_eating_speed(piles2, h2)
    print(f"Example 2: {result2}")  # Expected: 30
    
    # Example 3
    piles3 = [30, 11, 23, 4, 20]
    h3 = 6
    result3 = solution.min_eating_speed(piles3, h3)
    print(f"Example 3: {result3}")  # Expected: 23
