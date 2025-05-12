from typing import List


"""
LeetCode Partition Equal Subset Sum

Problem from LeetCode: https://leetcode.com/problems/partition-equal-subset-sum/

Given an integer array nums, return true if you can partition the array into two subsets 
such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
    Input: nums = [1,2,3,5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 100
"""

class Solution:

    def can_partition(self, nums: List[int]) ->bool:
        """
        Determine if the given array can be partitioned into two subsets 
        with equal sum.
        
        Args:
            nums: Array of positive integers
            
        Returns:
            bool: True if the array can be partitioned into two subsets with equal sum
        """
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
        return dp[target]

    def canPartition_memo(self, nums: List[int]) ->bool:
        """
        Recursive approach with memoization.
        
        Args:
            nums: Array of positive integers
            
        Returns:
            bool: True if the array can be partitioned into two subsets with equal sum
        """
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        memo = {}

        def dfs(index, current_sum):
            if current_sum > target:
                return False
            if current_sum == target:
                return True
            if index == len(nums):
                return False
            if (index, current_sum) in memo:
                return memo[index, current_sum]
            memo[index, current_sum] = dfs(index + 1, current_sum + nums[index]
                ) or dfs(index + 1, current_sum)
            return memo[index, current_sum]
        return dfs(0, 0)

    def canPartition_2d(self, nums: List[int]) ->bool:
        """
        2D dynamic programming approach.
        
        Args:
            nums: Array of positive integers
            
        Returns:
            bool: True if the array can be partitioned into two subsets with equal sum
        """
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        n = len(nums)
        dp = [([False] * (target + 1)) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - num]
        return dp[n][target]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: nums = [1,5,11,5]
    print("Example 1:")
    result = solution.can_partition([1,5,11,5])
    print(f"Output: {result}")  # Expected: true
    
    # Example 2: nums = [1,2,3,5]
    print("\nExample 2:")
    result = solution.can_partition([1,2,3,5])
    print(f"Output: {result}")  # Expected: false
    
    # Test with alternative implementations
    print("\nAlternative implementations:")
    print("Memoization approach:", solution.canPartition_memo([1,5,11,5]))
    print("2D DP approach:", solution.canPartition_2d([1,5,11,5]))
