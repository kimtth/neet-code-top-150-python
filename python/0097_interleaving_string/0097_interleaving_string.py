from typing import Dict

"""
LeetCode Interleaving String

Problem from LeetCode: https://leetcode.com/problems/interleaving-string/

Description:
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:
- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <= 1
- The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Determine if s3 is formed by interleaving s1 and s2.
        Uses dynamic programming with a 2D table.
        
        Args:
            s1: First string
            s2: Second string
            s3: Target string
            
        Returns:
            bool: True if s3 is an interleaving of s1 and s2, False otherwise
        """
        m, n = len(s1), len(s2)
        
        # Quick check: s3 must have length equal to s1 + s2
        if len(s3) != m + n:
            return False
            
        # dp[i][j] represents whether s3[0:i+j] is an interleaving of s1[0:i] and s2[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty strings
        dp[0][0] = True
        
        # Fill the first row (s1 is empty)
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
            
        # Fill the first column (s2 is empty)
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
            
        # Fill the rest of the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Current character in s3
                curr = s3[i+j-1]
                
                # Can we match with s1?
                match_s1 = dp[i-1][j] and s1[i-1] == curr
                
                # Can we match with s2?
                match_s2 = dp[i][j-1] and s2[j-1] == curr
                
                dp[i][j] = match_s1 or match_s2
                
        return dp[m][n]
    
    def isInterleave_1d(self, s1: str, s2: str, s3: str) -> bool:
        """
        Space-optimized version using 1D dynamic programming.
        
        Args:
            s1: First string
            s2: Second string
            s3: Target string
            
        Returns:
            bool: True if s3 is an interleaving of s1 and s2, False otherwise
        """
        m, n = len(s1), len(s2)
        
        if len(s3) != m + n:
            return False
            
        # Use a 1D array to save space
        dp = [False] * (n + 1)
        
        # Initialize
        dp[0] = True
        
        # Initial row where s1 is empty
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
            
        # Fill dp array row by row
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            
            for j in range(1, n + 1):
                curr = s3[i+j-1]
                dp[j] = (dp[j] and s1[i-1] == curr) or (dp[j-1] and s2[j-1] == curr)
                
        return dp[n]
    
    def isInterleave_memo(self, s1: str, s2: str, s3: str) -> bool:
        """
        Memoization-based approach using recursion.
        
        Args:
            s1: First string
            s2: Second string
            s3: Target string
            
        Returns:
            bool: True if s3 is an interleaving of s1 and s2, False otherwise
        """
        if len(s1) + len(s2) != len(s3):
            return False
            
        memo = {}
        
        def dp(i: int, j: int) -> bool:
            """Recursive helper function with memoization."""
            # Base case: reached end of both strings
            if i == len(s1) and j == len(s2):
                return True
                
            # Check if this state has been computed before
            if (i, j) in memo:
                return memo[(i, j)]
                
            # Current position in s3
            k = i + j
            
            # Try to match with s1
            if i < len(s1) and s1[i] == s3[k] and dp(i + 1, j):
                memo[(i, j)] = True
                return True
                
            # Try to match with s2
            if j < len(s2) and s2[j] == s3[k] and dp(i, j + 1):
                memo[(i, j)] = True
                return True
                
            memo[(i, j)] = False
            return False
            
        return dp(0, 0)

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1_1 = "aabcc"
    s2_1 = "dbbca"
    s3_1 = "aadbbcbcac"
    result1 = solution.isInterleave(s1_1, s2_1, s3_1)
    print(f"Example 1: s1='{s1_1}', s2='{s2_1}', s3='{s3_1}'")
    print(f"Result: {result1}")  # Expected output: True
    
    # Example 2
    s1_2 = "aabcc"
    s2_2 = "dbbca"
    s3_2 = "aadbbbaccc"
    result2 = solution.isInterleave(s1_2, s2_2, s3_2)
    print(f"\nExample 2: s1='{s1_2}', s2='{s2_2}', s3='{s3_2}'")
    print(f"Result: {result2}")  # Expected output: False
    
    # Example 3
    s1_3 = ""
    s2_3 = ""
    s3_3 = ""
    result3 = solution.isInterleave(s1_3, s2_3, s3_3)
    print(f"\nExample 3: s1='{s1_3}', s2='{s2_3}', s3='{s3_3}'")
    print(f"Result: {result3}")  # Expected output: True
    
    # Compare with other approaches
    print("\nUsing 1D dynamic programming approach:")
    print(f"Example 1: {solution.isInterleave_1d(s1_1, s2_1, s3_1)}")
    print(f"Example 2: {solution.isInterleave_1d(s1_2, s2_2, s3_2)}")
    
    print("\nUsing memoization approach:")
    print(f"Example 1: {solution.isInterleave_memo(s1_1, s2_1, s3_1)}")
    print(f"Example 2: {solution.isInterleave_memo(s1_2, s2_2, s3_2)}")
