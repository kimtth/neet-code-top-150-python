from typing import List, Optional

"""
LeetCode 198. House Robber

Problem from LeetCode: https://leetcode.com/problems/house-robber/

Description:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money 
you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400
"""

class Solution:

    def rob(self, nums: list[int]) ->int:
        """
        Dynamic programming approach for house robber problem.
        rob1 represents the maximum money we can get if we consider houses up to i-2
        rob2 represents the maximum money we can get if we consider houses up to i-1
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        rob1 = 0
        rob2 = 0
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [1, 2, 3, 1]
    result1 = solution.rob(nums1)
    print(f"Input: nums = {nums1}")
    print(f"Output: {result1}")  # Expected output: 4
    
    # Example 2
    nums2 = [2, 7, 9, 3, 1]
    result2 = solution.rob(nums2)
    print(f"Input: nums = {nums2}")
    print(f"Output: {result2}")  # Expected output: 12
    
    # Edge cases
    print(f"\nEmpty array: {solution.rob([])}")  # Expected output: 0
    print(f"Single element: {solution.rob([5])}")  # Expected output: 5
