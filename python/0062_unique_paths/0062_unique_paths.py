from typing import List

"""
LeetCode Unique Paths

Problem from LeetCode: https://leetcode.com/problems/unique-paths/

Description:
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        """
        Calculate the number of unique paths from top-left to bottom-right.
        Uses dynamic programming with O(m*n) time and space complexity.
        
        Args:
            m: Number of rows in the grid
            n: Number of columns in the grid
            
        Returns:
            int: Number of unique paths
        """
        # Initialize dp table with 1s for the first row and column
        dp = [[1] * n for _ in range(m)]
        
        # Fill the dp table
        for i in range(1, m):
            for j in range(1, n):
                # Number of ways to reach (i,j) = ways to reach from above + ways to reach from left
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
    
    def unique_paths_optimized(self, m: int, n: int) -> int:
        """
        Calculate unique paths with optimized space complexity O(n).
        
        Args:
            m: Number of rows
            n: Number of columns
            
        Returns:
            int: Number of unique paths
        """
        # Use a single row of the dp table
        dp = [1] * n
        
        # Update the dp array m-1 times
        for i in range(1, m):
            for j in range(1, n):
                # dp[j] now represents the number of ways to reach cell (i,j)
                dp[j] += dp[j-1]
        
        return dp[n-1]
    
    def unique_paths_math(self, m: int, n: int) -> int:
        """
        Calculate unique paths using mathematical combination formula.
        The problem is equivalent to choosing which steps to go down (or right).
        
        Args:
            m: Number of rows
            n: Number of columns
            
        Returns:
            int: Number of unique paths
        """
        # Total steps needed: (m-1) down steps + (n-1) right steps = (m+n-2) total steps
        # We need to choose which of these steps are down (or right)
        # This is equivalent to choosing (m-1) positions from (m+n-2) positions
        # The formula is C(m+n-2, m-1) = (m+n-2)! / ((m-1)! * (n-1)!)
        
        import math
        return math.comb(m + n - 2, m - 1)

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    m1, n1 = 3, 7
    result1 = solution.unique_paths(m1, n1)
    print(f"Example 1: m={m1}, n={n1}, paths={result1}")  # Expected output: 28
    
    # Example 2
    m2, n2 = 3, 2
    result2 = solution.unique_paths(m2, n2)
    print(f"Example 2: m={m2}, n={n2}, paths={result2}")  # Expected output: 3
    
    # Additional example
    m3, n3 = 10, 10
    result3 = solution.unique_paths(m3, n3)
    print(f"Example 3: m={m3}, n={n3}, paths={result3}")  # Expected output: 48620
    
    # Compare different implementations
    print("\nComparing implementations:")
    print(f"Standard DP: {solution.unique_paths(m1, n1)}")
    print(f"Optimized space: {solution.unique_paths_optimized(m1, n1)}")
    print(f"Math formula: {solution.unique_paths_math(m1, n1)}")
