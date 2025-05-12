from typing import List


"""
LeetCode 217: Contains Duplicate

Problem from LeetCode: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

class Solution:

    def contains_duplicate(self, nums: List[int]) ->bool:
        """
        Determine if the array contains any duplicates.
        
        Args:
            nums: An array of integers
            
        Returns:
            bool: True if any value appears at least twice in the array, False otherwise
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def contains_duplicate_alternative(self, nums: List[int]) ->bool:
        """
        Alternative implementation using set comparison.
        
        Args:
            nums: An array of integers
            
        Returns:
            bool: True if any value appears at least twice in the array, False otherwise
        """
        return len(set(nums)) < len(nums)

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums = [1, 2, 3, 1]
    result = solution.contains_duplicate(nums)
    print(result)  # Output: True
    
    # Example 2
    nums = [1, 2, 3, 4]
    result = solution.contains_duplicate(nums)
    print(result)  # Output: False
    
    # Example 3
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result = solution.contains_duplicate(nums)
    print(result)  # Output: True
