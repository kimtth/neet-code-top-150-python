from typing import List

"""
LeetCode Regular Expression Matching

Problem from LeetCode: https://leetcode.com/problems/regular-expression-matching/

Description:
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
"""

class Solution:
    def is_match(self, s: str, p: str) -> bool:
        """
        Check if a string matches a pattern with '.' and '*' wildcard characters.
        
        Args:
            s: Input string
            p: Pattern string with '.' and '*'
            
        Returns:
            bool: True if the string matches the pattern, False otherwise
        """
        # Create a memoization cache
        memo = {}
        
        def dp(i, j):
            # If we've seen this state before, return the cached result
            if (i, j) in memo:
                return memo[(i, j)]
                
            # If pattern is exhausted, string must also be exhausted
            if j == len(p):
                return i == len(s)
                
            # Check if the current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            # If the next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two options: 
                # 1. Skip the pattern element with '*' (use zero occurrences)
                # 2. Use the pattern element if it matches, and then try again from the next string position
                memo[(i, j)] = dp(i, j + 2) or (first_match and dp(i + 1, j))
                return memo[(i, j)]
            
            # Without '*', must match current character and proceed
            memo[(i, j)] = first_match and dp(i + 1, j + 1)
            return memo[(i, j)]
            
        return dp(0, 0)
    
    def is_match_bottom_up(self, s: str, p: str) -> bool:
        """
        Check if a string matches a pattern using bottom-up dynamic programming.
        
        Args:
            s: Input string
            p: Pattern string with '.' and '*'
            
        Returns:
            bool: True if the string matches the pattern, False otherwise
        """
        # dp[i][j] represents if s[0:i] matches p[0:j]
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* matching empty string
        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
                
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    # If we consider zero occurrences of the preceding element
                    dp[i][j] = dp[i][j-2]
                    
                    # If the pattern character before '*' matches the current string character
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                        
                elif p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                    
        return dp[len(s)][len(p)]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1, p1 = "aa", "a"
    result1 = solution.is_match(s1, p1)
    print(f"Example 1: s='{s1}', p='{p1}' -> {result1}")  # Expected output: False
    
    # Example 2
    s2, p2 = "aa", "a*"
    result2 = solution.is_match(s2, p2)
    print(f"Example 2: s='{s2}', p='{p2}' -> {result2}")  # Expected output: True
    
    # Example 3
    s3, p3 = "ab", ".*"
    result3 = solution.is_match(s3, p3)
    print(f"Example 3: s='{s3}', p='{p3}' -> {result3}")  # Expected output: True
    
    # Additional examples
    s4, p4 = "aab", "c*a*b"
    result4 = solution.is_match(s4, p4)
    print(f"Example 4: s='{s4}', p='{p4}' -> {result4}")  # Expected output: True
    
    # Compare with bottom-up approach
    print("\nUsing bottom-up dynamic programming:")
    print(f"Example 1: {solution.is_match_bottom_up(s1, p1)}")
    print(f"Example 2: {solution.is_match_bottom_up(s2, p2)}")
    print(f"Example 3: {solution.is_match_bottom_up(s3, p3)}")
