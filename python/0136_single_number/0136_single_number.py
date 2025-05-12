from typing import List, Optional

"""
LeetCode Single Number

Problem from LeetCode: https://leetcode.com/problems/single-number/

Description:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""

class Solution:

    def single_number(self, nums: list[int]) ->int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [2, 2, 1]
    result1 = solution.single_number(nums1)
    print(f"Example 1: {result1}")  # Expected output: 1
    
    # Example 2
    nums2 = [4, 1, 2, 1, 2]
    result2 = solution.single_number(nums2)
    print(f"Example 2: {result2}")  # Expected output: 4
    
    # Example 3
    nums3 = [1]
    result3 = solution.single_number(nums3)
    print(f"Example 3: {result3}")  # Expected output: 1
