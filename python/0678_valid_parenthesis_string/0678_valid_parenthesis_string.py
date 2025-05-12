from typing import List, Optional

"""
LeetCode Valid Parenthesis String

Problem from LeetCode: https://leetcode.com/problems/valid-parenthesis-string/

Description:
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:
1. Any left parenthesis '(' must have a corresponding right parenthesis ')'. 
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'. 
4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "". 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true

Constraints:
1 <= s.length <= 100
s consists of characters '(', ')' and '*'. 
"""

class Solution:

    def check_valid_string(self, s: str) ->bool:
        """
        Determine if the input string is valid.
        An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
        
        Args:
            s: The input string containing only '(', ')' and '*'
            
        Returns:
            bool: True if the string is valid, False otherwise
        """
        min_open = 0
        max_open = 0
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:
                min_open -= 1
                max_open += 1
            if max_open < 0:
                return False
            min_open = max(min_open, 0)
        return min_open == 0

    def checkValidString_dp(self, s: str) ->bool:
        """
        Alternative implementation using dynamic programming.
        
        Args:
            s: The input string containing only '(', ')' and '*'
            
        Returns:
            bool: True if the string is valid, False otherwise
        """
        n = len(s)
        if n == 0:
            return True
        dp = [([False] * n) for _ in range(n)]
        for i in range(n):
            if s[i] == '*':
                dp[i][i] = True
        for i in range(n - 1):
            if (s[i] == '(' or s[i] == '*') and (s[i + 1] == ')' or s[i + 1
                ] == '*'):
                dp[i][i + 1] = True
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == '*' and dp[i + 1][j]:
                    dp[i][j] = True
                    continue
                if (s[i] == '(' or s[i] == '*') and (s[j] == ')' or s[j] == '*'
                    ):
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        continue
                for k in range(i, j):
                    if dp[i][k] and dp[k + 1][j]:
                        dp[i][j] = True
                        break
        return dp[0][n - 1]

    def checkValidString_greedy(self, s: str) ->bool:
        """
        Greedy approach with two passes to check for validity.
        
        Args:
            s: The input string containing only '(', ')' and '*'
            
        Returns:
            bool: True if the string is valid, False otherwise
        """
        balance = 0
        for char in s:
            if char == '(' or char == '*':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        if balance == 0:
            return True
        balance = 0
        for char in reversed(s):
            if char == ')' or char == '*':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return True


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "()"
    result1 = solution.check_valid_string(s1)
    print(f"Example 1: {result1}")  # Expected: True
    
    # Example 2
    s2 = "(*)"
    result2 = solution.check_valid_string(s2)
    print(f"Example 2: {result2}")  # Expected: True
    
    # Example 3
    s3 = "(*))"
    result3 = solution.check_valid_string(s3)
    print(f"Example 3: {result3}")  # Expected: True
    
    # Test with DP approach
    print("\nWith DP approach:")
    result4 = solution.checkValidString_dp(s3)
    print(f"Example 3: {result4}")  # Expected: True
    
    # Test with greedy approach
    print("\nWith greedy approach:")
    result5 = solution.checkValidString_greedy(s3)
    print(f"Example 3: {result5}")  # Expected: True
