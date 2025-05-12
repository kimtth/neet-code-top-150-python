from typing import List


"""
LeetCode Coin Change

Problem from LeetCode: https://leetcode.com/problems/coin-change/

Description:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""

class Solution:

    def coin_change(self, coins: List[int], amount: int) -> int:
        """
        Find the fewest number of coins needed to make up the given amount.
        
        This implementation uses dynamic programming with a bottom-up approach.
        
        Args:
            coins: Array of coin denominations
            amount: Target amount to make
            
        Returns:
            int: Minimum number of coins needed, or -1 if amount cannot be made
        """
        # Initialize dp array with amount+1 (larger than any possible result)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0
        
        # Build the dp array bottom-up
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        
        # If dp[amount] is still amount+1, it means amount cannot be made
        return dp[amount] if dp[amount] != amount + 1 else -1

    def coin_change_recursive(self, coins: List[int], amount: int) -> int:
        """
        Find the fewest number of coins needed using a top-down recursive approach with memoization.
        
        Args:
            coins: Array of coin denominations
            amount: Target amount to make
            
        Returns:
            int: Minimum number of coins needed, or -1 if amount cannot be made
        """
        # Memoization cache
        memo = {}
        
        def dfs(remaining):
            # Base cases
            if remaining == 0:
                return 0
            if remaining < 0:
                return -1
            if remaining in memo:
                return memo[remaining]
            
            # Try each coin and find the minimum number of coins needed
            min_coins = float('inf')
            for coin in coins:
                result = dfs(remaining - coin)
                if result != -1:
                    min_coins = min(min_coins, result + 1)
            
            # Cache the result
            memo[remaining] = min_coins if min_coins != float('inf') else -1
            return memo[remaining]
        
        return dfs(amount)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    coins1 = [1, 2, 5]
    amount1 = 11
    result1 = solution.coin_change(coins1, amount1)
    print(f"Example 1: {result1}")  # Expected output: 3
    
    # Example 2
    coins2 = [2]
    amount2 = 3
    result2 = solution.coin_change(coins2, amount2)
    print(f"Example 2: {result2}")  # Expected output: -1
    
    # Example 3
    coins3 = [1]
    amount3 = 0
    result3 = solution.coin_change(coins3, amount3)
    print(f"Example 3: {result3}")  # Expected output: 0
    
    # Additional example
    coins4 = [1, 3, 4, 5]
    amount4 = 7
    result4 = solution.coin_change(coins4, amount4)
    print(f"Example 4: {result4}")  # Expected output: 2 (3 + 4 = 7)
    
    # Using recursive approach
    print("\nUsing recursive approach:")
    result5 = solution.coin_change_recursive(coins1, amount1)
    print(f"Example 1: {result5}")  # Expected output: 3
