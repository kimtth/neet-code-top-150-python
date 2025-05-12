from typing import Dict


"""
LeetCode Climbing Stairs

Problem from LeetCode: https://leetcode.com/problems/climbing-stairs/

Description:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:

    def climb_stairs(self, n: int) ->int:
        """
        You are climbing a staircase that takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps.
        Return the number of distinct ways you can climb to the top.
        
        Args:
            n: Number of steps to reach the top
            
        Returns:
            int: Number of distinct ways to climb to the top
        """
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs_optimized(self, n: int) ->int:
        """
        Space-optimized solution using only two variables instead of an array.
        
        Args:
            n: Number of steps to reach the top
            
        Returns:
            int: Number of distinct ways to climb to the top
        """
        if n <= 2:
            return n
        one_step_before = 2
        two_steps_before = 1
        current_ways = 0
        for i in range(3, n + 1):
            current_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current_ways
        return current_ways

    def climbStairs_recursive(self, n: int) ->int:
        """
        Recursive solution with memoization to avoid redundant calculations.
        
        Args:
            n: Number of steps to reach the top
            
        Returns:
            int: Number of distinct ways to climb to the top
        """
        memo: Dict[int, int] = {}

        def climb(i: int) ->int:
            if i in memo:
                return memo[i]
            if i <= 2:
                return i
            memo[i] = climb(i - 1) + climb(i - 2)
            return memo[i]
        return climb(n)

    def climbStairs_fibonacci(self, n: int) ->int:
        """
        Mathematical solution using the Fibonacci formula.
        
        Args:
            n: Number of steps to reach the top
            
        Returns:
            int: Number of distinct ways to climb to the top
        """
        import math
        sqrt5 = math.sqrt(5)
        fibn = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2,
            n + 1)
        return int(fibn / sqrt5)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    n1 = 2
    result1 = solution.climb_stairs(n1)
    print(f"Example 1: n={n1}, ways={result1}")  # Expected output: 2
    
    # Example 2
    n2 = 3
    result2 = solution.climb_stairs(n2)
    print(f"Example 2: n={n2}, ways={result2}")  # Expected output: 3
    
    # Additional examples
    n3 = 5
    result3 = solution.climb_stairs(n3)
    print(f"Example 3: n={n3}, ways={result3}")  # Expected output: 8
    
    n4 = 10
    result4 = solution.climb_stairs(n4)
    print(f"Example 4: n={n4}, ways={result4}")  # Expected output: 89
    
    # Compare different implementations
    print("\nComparing implementations:")
    print(f"DP with array: {solution.climb_stairs(n3)}")
    print(f"Space optimized: {solution.climbStairs_optimized(n3)}")
    print(f"Recursive with memoization: {solution.climbStairs_recursive(n3)}")
    print(f"Fibonacci formula: {solution.climbStairs_fibonacci(n3)}")
