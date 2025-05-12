from typing import List

"""
LeetCode Best Time to Buy and Sell Stock

Problem from LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

class Solution:
    def max_profit(self, prices: List[int]) -> int:
        """
        Find the maximum profit from buying and selling a stock.
        
        Args:
            prices: Array of stock prices
            
        Returns:
            int: Maximum profit possible
        """
        if not prices or len(prices) < 2:
            return 0
            
        max_profit = 0
        min_price = prices[0]
        
        for price in prices:
            # Update the minimum price seen so far
            min_price = min(min_price, price)
            
            # Calculate potential profit with current price
            current_profit = price - min_price
            
            # Update maximum profit if current profit is higher
            max_profit = max(max_profit, current_profit)
            
        return max_profit
    
    def max_profit_brute_force(self, prices: List[int]) -> int:
        """
        Brute force approach (inefficient, for illustration only).
        
        Args:
            prices: Array of stock prices
            
        Returns:
            int: Maximum profit possible
        """
        max_profit = 0
        n = len(prices)
        
        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
                
        return max_profit
    
    def max_profit_dp(self, prices: List[int]) -> int:
        """
        Dynamic programming approach.
        
        Args:
            prices: Array of stock prices
            
        Returns:
            int: Maximum profit possible
        """
        if not prices or len(prices) < 2:
            return 0
            
        n = len(prices)
        # dp[i] represents the maximum profit up to day i
        dp = [0] * n
        
        min_price = prices[0]
        
        for i in range(1, n):
            # Calculate profit if selling on day i
            dp[i] = max(dp[i-1], prices[i] - min_price)
            
            # Update minimum price
            min_price = min(min_price, prices[i])
            
        return dp[n-1]

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = solution.max_profit(prices1)
    print(f"Example 1: prices={prices1}")
    print(f"Maximum profit: {result1}")  # Expected output: 5
    
    # Example 2
    prices2 = [7, 6, 4, 3, 1]
    result2 = solution.max_profit(prices2)
    print(f"\nExample 2: prices={prices2}")
    print(f"Maximum profit: {result2}")  # Expected output: 0
    
    # Additional example
    prices3 = [2, 4, 1]
    result3 = solution.max_profit(prices3)
    print(f"\nExample 3: prices={prices3}")
    print(f"Maximum profit: {result3}")  # Expected output: 2
    
    # Compare approaches (using a small array for brute force)
    small_prices = [7, 1, 5, 3, 6]
    print("\nComparing approaches:")
    print(f"Optimal approach: {solution.max_profit(small_prices)}")
    print(f"Brute force approach: {solution.max_profit_brute_force(small_prices)}")
    print(f"DP approach: {solution.max_profit_dp(small_prices)}")
