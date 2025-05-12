from typing import List


"""
LeetCode Coin Change II

Problem from LeetCode: https://leetcode.com/problems/coin-change-ii/

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
    Input: amount = 5, coins = [1,2,5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1

Example 2:
    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
    Input: amount = 10, coins = [10]
    Output: 1

Constraints:
    1 <= coins.length <= 300
    1 <= coins[i] <= 5000
    All the values of coins are unique.
    0 <= amount <= 5000
"""

class Solution:

    def change(self, amount: int, coins: List[int]) ->int:
        """
        Return the number of combinations that make up the given amount.
        
        Args:
            amount: Target amount to make up
            coins: Available coin denominations
            
        Returns:
            int: Number of combinations that make up the amount
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[amount]

    def change_2d(self, amount: int, coins: List[int]) ->int:
        """
        Return the number of combinations using 2D DP approach.
        
        Args:
            amount: Target amount to make up
            coins: Available coin denominations
            
        Returns:
            int: Number of combinations that make up the amount
        """
        n = len(coins)
        dp = [([0] * (amount + 1)) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
        return dp[n][amount]

    def change_recursive(self, amount: int, coins: List[int]) ->int:
        """
        Return the number of combinations using recursive approach with memoization.
        
        Args:
            amount: Target amount to make up
            coins: Available coin denominations
            
        Returns:
            int: Number of combinations that make up the amount
        """
        memo = {}

        def dfs(index: int, remaining: int) ->int:
            if remaining == 0:
                return 1
            if remaining < 0 or index >= len(coins):
                return 0
            if (index, remaining) in memo:
                return memo[index, remaining]
            result = dfs(index, remaining - coins[index]) + dfs(index + 1,
                remaining)
            memo[index, remaining] = result
            return result
        return dfs(0, amount)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: amount = 5, coins = [1,2,5]
    print("Example 1:")
    result = solution.change(5, [1, 2, 5])
    print(f"Output: {result}")  # Expected: 4
    
    # Example 2: amount = 3, coins = [2]
    print("\nExample 2:")
    result = solution.change(3, [2])
    print(f"Output: {result}")  # Expected: 0
    
    # Example 3: amount = 10, coins = [10]
    print("\nExample 3:")
    result = solution.change(10, [10])
    print(f"Output: {result}")  # Expected: 1
    
    # Test with alternative implementations
    print("\nAlternative implementations:")
    print("2D DP approach:", solution.change_2d(5, [1, 2, 5]))
    print("Recursive approach:", solution.change_recursive(5, [1, 2, 5]))
