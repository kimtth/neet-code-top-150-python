from typing import List


"""
LeetCode Min Cost Climbing Stairs

Problem from LeetCode: https://leetcode.com/problems/min-cost-climbing-stairs/

Description:
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb two steps to reach index 8.
- Pay 1 and climb two steps to reach the top.
The total cost is 6.

Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""

class Solution:

    def min_cost_climbing_stairs(self, cost: List[int]) ->int:
        """
        Calculate the minimum cost to reach the top of the floor.
        You can either start from the step with index 0, or the step with index 1.
        You can climb 1 or 2 steps at a time.
        
        Args:
            cost: Cost associated with each step
            
        Returns:
            int: Minimum cost to reach the top
        """
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        first = cost[0]
        second = cost[1]
        for i in range(2, len(cost)):
            current = min(first, second) + cost[i]
            first, second = second, current
        return min(first, second)

    def minCostClimbingStairs_dp_array(self, cost: List[int]) ->int:
        """
        Dynamic programming approach using an array.
        
        Args:
            cost: Cost associated with each step
            
        Returns:
            int: Minimum cost to reach the top
        """
        n = len(cost)
        if n == 1:
            return cost[0]
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[n - 1], dp[n - 2])

    def minCostClimbingStairs_optimized(self, cost: List[int]) ->int:
        """
        Space-optimized approach without using an array.
        
        Args:
            cost: Cost associated with each step
            
        Returns:
            int: Minimum cost to reach the top
        """
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        prev1 = cost[0]
        prev2 = cost[1]
        for i in range(2, n):
            current = min(prev1, prev2) + cost[i]
            prev1, prev2 = prev2, current
        return min(prev1, prev2)

    def minCostClimbingStairs_recursive(self, cost: List[int]) ->int:
        """
        Recursive approach with memoization.
        
        Args:
            cost: Cost associated with each step
            
        Returns:
            int: Minimum cost to reach the top
        """
        n = len(cost)
        memo = {}

        def dp(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]
        return dp(n)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    cost1 = [10, 15, 20]
    result1 = solution.min_cost_climbing_stairs(cost1)
    print(f"Example 1: {result1}")  # Expected: 15
    
    # Example 2
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    result2 = solution.min_cost_climbing_stairs(cost2)
    print(f"Example 2: {result2}")  # Expected: 6
