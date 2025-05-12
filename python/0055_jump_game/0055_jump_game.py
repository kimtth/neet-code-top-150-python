from typing import List


"""
LeetCode Jump Game

Problem from LeetCode: https://leetcode.com/problems/jump-game/

Description:
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

class Solution:

    def can_jump(self, nums: List[int]) ->bool:
        """
        Determine if you can reach the last index in the array.
        
        Each element in the array represents the maximum jump length at that position.
        
        Args:
            nums: Non-negative integers representing maximum jump lengths
            
        Returns:
            bool: True if you can reach the last index, otherwise False
        """
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

    def canJump_forward(self, nums: List[int]) ->bool:
        """
        Alternative implementation using a forward greedy approach.
        
        Args:
            nums: Non-negative integers representing maximum jump lengths
            
        Returns:
            bool: True if you can reach the last index, otherwise False
        """
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        return True

    def canJump_dp(self, nums: List[int]) ->bool:
        """
        Dynamic programming approach to determine if we can reach the end.
        
        Args:
            nums: Non-negative integers representing maximum jump lengths
            
        Returns:
            bool: True if you can reach the last index, otherwise False
        """
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = True
                    if i + j == n - 1:
                        return True
        return dp[n - 1]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [2, 3, 1, 1, 4]
    result1 = solution.can_jump(nums1)
    print(f"Example 1: {result1}")  # Expected output: True
    
    # Example 2
    nums2 = [3, 2, 1, 0, 4]
    result2 = solution.can_jump(nums2)
    print(f"Example 2: {result2}")  # Expected output: False
    
    # Additional examples
    nums3 = [2, 0, 0]
    result3 = solution.can_jump(nums3)
    print(f"Example 3: {result3}")  # Expected output: True
    
    nums4 = [1, 1, 1, 0]
    result4 = solution.can_jump(nums4)
    print(f"Example 4: {result4}")  # Expected output: True
    
    # Compare different implementations
    print("\nUsing forward approach:")
    print(f"Example 1: {solution.canJump_forward(nums1)}")
    print(f"Example 2: {solution.canJump_forward(nums2)}")
    
    print("\nUsing dynamic programming approach:")
    print(f"Example 1: {solution.canJump_dp(nums1)}")
    print(f"Example 2: {solution.canJump_dp(nums2)}")
