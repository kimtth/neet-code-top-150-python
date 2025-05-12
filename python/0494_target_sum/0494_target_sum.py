from typing import List


"""
LeetCode Target Sum

Problem from LeetCode: https://leetcode.com/problems/target-sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' 
before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and 
concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

Example 1:
    Input: nums = [1,1,1,1,1], target = 3
    Output: 5
    Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
    -1 + 1 + 1 + 1 + 1 = 3
    +1 - 1 + 1 + 1 + 1 = 3
    +1 + 1 - 1 + 1 + 1 = 3
    +1 + 1 + 1 - 1 + 1 = 3
    +1 + 1 + 1 + 1 - 1 = 3

Example 2:
    Input: nums = [1], target = 1
    Output: 1

Constraints:
    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    0 <= sum(nums[i]) <= 1000
    -1000 <= target <= 1000
"""

class Solution:

    def find_target_sum_ways(self, nums: List[int], target: int) ->int:
        """
        Find the number of different ways to assign + and - signs to elements
        of nums so that the sum equals target.
        
        Args:
            nums: An integer array
            target: The target sum
            
        Returns:
            int: The number of different ways to achieve the target sum
        """
        total_sum = sum(nums)
        if (target + total_sum) % 2 != 0 or total_sum < abs(target):
            return 0
        subset_sum = (target + total_sum) // 2
        if subset_sum < 0:
            return 0
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[subset_sum]

    def findTargetSumWays_memo(self, nums: List[int], target: int) ->int:
        """
        Recursive approach with memoization.
        
        Args:
            nums: An integer array
            target: The target sum
            
        Returns:
            int: The number of different ways to achieve the target sum
        """
        memo = {}

        def dfs(index, current_sum):
            if index == len(nums):
                return 1 if current_sum == target else 0
            if (index, current_sum) in memo:
                return memo[index, current_sum]
            add = dfs(index + 1, current_sum + nums[index])
            subtract = dfs(index + 1, current_sum - nums[index])
            memo[index, current_sum] = add + subtract
            return memo[index, current_sum]
        return dfs(0, 0)

    def findTargetSumWays_2d(self, nums: List[int], target: int) ->int:
        """
        2D dynamic programming approach.
        
        Args:
            nums: An integer array
            target: The target sum
            
        Returns:
            int: The number of different ways to achieve the target sum
        """
        total_sum = sum(nums)
        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0
        positive_sum = (target + total_sum) // 2
        if positive_sum < 0:
            return 0
        n = len(nums)
        dp = [([0] * (positive_sum + 1)) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(positive_sum + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
        return dp[n][positive_sum]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: nums = [1,1,1,1,1], target = 3
    print("Example 1:")
    result = solution.find_target_sum_ways([1,1,1,1,1], 3)
    print(f"Output: {result}")  # Expected: 5
    
    # Example 2: nums = [1], target = 1
    print("\nExample 2:")
    result = solution.find_target_sum_ways([1], 1)
    print(f"Output: {result}")  # Expected: 1
    
    # Test with alternative implementations
    print("\nAlternative implementations:")
    print("Memoization approach:", solution.findTargetSumWays_memo([1,1,1,1,1], 3))
    print("2D DP approach:", solution.findTargetSumWays_2d([1,1,1,1,1], 3))
