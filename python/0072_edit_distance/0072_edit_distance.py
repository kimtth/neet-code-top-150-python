from typing import List, Dict

"""
LeetCode Edit Distance

Problem from LeetCode: https://leetcode.com/problems/edit-distance/

Description:
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution:
    def min_distance(self, word1: str, word2: str) -> int:
        """
        Calculate the minimum edit distance between two strings.
        Uses dynamic programming with a 2D table.
        
        Args:
            word1: First string
            word2: Second string
            
        Returns:
            int: Minimum number of operations to convert word1 to word2
        """
        m, n = len(word1), len(word2)
        
        # Initialize DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: empty string to non-empty string
        for i in range(m + 1):
            dp[i][0] = i  # Delete all characters from word1
        
        for j in range(n + 1):
            dp[0][j] = j  # Insert all characters from word2
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # If characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Minimum of three operations:
                    # Replace: dp[i-1][j-1] + 1
                    # Delete: dp[i-1][j] + 1
                    # Insert: dp[i][j-1] + 1
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
    
    def min_distance_memoization(self, word1: str, word2: str) -> int:
        """
        Calculate edit distance using recursive approach with memoization.
        
        Args:
            word1: First string
            word2: Second string
            
        Returns:
            int: Minimum number of operations
        """
        memo = {}
        
        def dp(i: int, j: int) -> int:
            """Recursive helper function with memoization."""
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base cases
            if i == 0:
                return j  # Insert j characters
            if j == 0:
                return i  # Delete i characters
            
            if word1[i - 1] == word2[j - 1]:
                # Characters match, no operation needed
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                # Minimum of three operations
                memo[(i, j)] = 1 + min(
                    dp(i - 1, j - 1),  # Replace
                    dp(i - 1, j),      # Delete
                    dp(i, j - 1)       # Insert
                )
            
            return memo[(i, j)]
        
        return dp(len(word1), len(word2))

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    word1_1, word2_1 = "horse", "ros"
    result1 = solution.min_distance(word1_1, word2_1)
    print(f"Example 1: word1='{word1_1}', word2='{word2_1}', result={result1}")  # Expected: 3
    
    # Example 2
    word1_2, word2_2 = "intention", "execution"
    result2 = solution.min_distance(word1_2, word2_2)
    print(f"Example 2: word1='{word1_2}', word2='{word2_2}', result={result2}")  # Expected: 5
    
    # Compare with memoization approach
    print("\nUsing memoization approach:")
    print(f"Example 1: {solution.min_distance_memoization(word1_1, word2_1)}")  # Expected: 3
    print(f"Example 2: {solution.min_distance_memoization(word1_2, word2_2)}")  # Expected: 5
