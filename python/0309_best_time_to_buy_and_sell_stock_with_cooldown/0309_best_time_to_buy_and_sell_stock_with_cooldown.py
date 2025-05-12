from typing import List


"""
LeetCode Best Time To Buy And Sell Stock With Cooldown

Problem from LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""

class Solution:

    def max_profit(self, prices: List[int]) ->int:
        """
        Calculate the maximum profit with cooldown constraint.
        
        After selling stock, you cannot buy stock on the next day (cooldown).
        
        Args:
            prices: List of stock prices where prices[i] is the price on day i
            
        Returns:
            int: Maximum profit that can be achieved
        """
        if not prices or len(prices) <= 1:
            return 0
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        rest = [0] * n
        buy[0] = -prices[0]
        sell[0] = 0
        rest[0] = 0
        for i in range(1, n):
            buy[i] = max(buy[i - 1], rest[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            rest[i] = max(rest[i - 1], sell[i - 1])
        return max(sell[n - 1], rest[n - 1])

    def max_profit_optimized(self, prices: List[int]) ->int:
        """
        Optimized solution with O(1) space complexity.
        
        Args:
            prices: List of stock prices where prices[i] is the price on day i
            
        Returns:
            int: Maximum profit that can be achieved
        """
        if not prices or len(prices) <= 1:
            return 0
        buy = -prices[0]
        sell = 0
        prev_sell = 0
        for i in range(1, len(prices)):
            old_sell = sell
            sell = max(sell, buy + prices[i])
            buy = max(buy, prev_sell - prices[i])
            prev_sell = old_sell
        return sell


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    prices1 = [1, 2, 3, 0, 2]
    result1 = solution.max_profit(prices1)
    print(f"Example 1: {result1}")  # Expected output: 3
    
    # Example 2
    prices2 = [1]
    result2 = solution.max_profit(prices2)
    print(f"Example 2: {result2}")  # Expected output: 0
    
    # Additional example
    prices3 = [2, 1, 4, 5, 2, 9, 7]
    result3 = solution.max_profit(prices3)
    print(f"Example 3: {result3}")  # Expected output: 11
    
    # Using optimized solution
    print("\nUsing optimized solution:")
    result4 = solution.max_profit_optimized(prices1)
    print(f"Example 1: {result4}")  # Expected output: 3
