from typing import List


"""
LeetCode Burst Balloons

Problem from LeetCode: https://leetcode.com/problems/burst-balloons/

Description:
You are given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i-1] * nums[i] * nums[i+1] coins. If i-1 or i+1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +  3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:
Input: nums = [1,5]
Output: 10

Constraints:
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""

class Solution:

    def max_coins(self, nums: List[int]) ->int:
        """
        Return the maximum coins you can collect by bursting the balloons.
        
        Args:
            nums: Array of integers representing balloon values
            
        Returns:
            int: Maximum coins obtainable
        """
        n = len(nums)
        extended_nums = [1] + nums + [1]
        dp = [([0] * (n + 2)) for _ in range(n + 2)]
        for length in range(1, n + 1):
            for left in range(1, n - length + 2):
                right = left + length - 1
                for i in range(left, right + 1):
                    coins = extended_nums[left - 1] * extended_nums[i
                        ] * extended_nums[right + 1]
                    coins += dp[left][i - 1] + dp[i + 1][right]
                    dp[left][right] = max(dp[left][right], coins)
        return dp[1][n]

    def max_coins_recursive(self, nums: List[int]) ->int:
        """
        Return the maximum coins using a top-down recursive approach with memoization.
        
        Args:
            nums: Array of integers representing balloon values
            
        Returns:
            int: Maximum coins obtainable
        """
        nums = [1] + nums + [1]
        memo = {}

        def dp(left, right):
            if left > right:
                return 0
            if (left, right) in memo:
                return memo[left, right]
            result = 0
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                coins += dp(left, i - 1) + dp(i + 1, right)
                result = max(result, coins)
            memo[left, right] = result
            return result
        return dp(1, len(nums) - 2)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [3, 1, 5, 8]
    result1 = solution.max_coins(nums1)
    print(f"Example 1: {result1}")  # Expected output: 167
    
    # Example 2
    nums2 = [1, 5]
    result2 = solution.max_coins(nums2)
    print(f"Example 2: {result2}")  # Expected output: 10
    
    # Using recursive approach
    print("\nUsing recursive approach:")
    result3 = solution.max_coins_recursive(nums1)
    print(f"Example 1: {result3}")  # Expected output: 167
    
    result4 = solution.max_coins_recursive(nums2)
    print(f"Example 2: {result4}")  # Expected output: 10
