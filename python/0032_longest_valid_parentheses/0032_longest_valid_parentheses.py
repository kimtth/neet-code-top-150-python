from typing import List

"""
LeetCode Longest Valid Parentheses

Problem from LeetCode: https://leetcode.com/problems/longest-valid-parentheses/

Description:
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
"""

class Solution:
    def longest_valid_parentheses(self, s: str) -> int:
        """
        Find the length of the longest valid parentheses substring.
        Uses a stack-based approach.
        
        Args:
            s: String containing only parentheses characters
            
        Returns:
            int: Length of the longest valid parentheses substring
        """
        stack = [-1]  # Initialize with -1 as a base index
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:  # s[i] == ')'
                stack.pop()
                if not stack:
                    # No matching opening parenthesis, use current index as new base
                    stack.append(i)
                else:
                    # Calculate length of current valid substring
                    max_length = max(max_length, i - stack[-1])
                    
        return max_length
    
    def longest_valid_parentheses_dp(self, s: str) -> int:
        """
        Find the length of the longest valid parentheses substring using dynamic programming.
        
        Args:
            s: String containing only parentheses characters
            
        Returns:
            int: Length of the longest valid parentheses substring
        """
        if not s:
            return 0
            
        n = len(s)
        # dp[i] represents the length of the longest valid substring ending at i
        dp = [0] * n
        max_length = 0
        
        for i in range(1, n):
            if s[i] == ')':
                # Case 1: ()
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                # Case 2: ))
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + 2
                    # Add any valid parentheses substring before this one
                    if i - dp[i-1] - 2 >= 0:
                        dp[i] += dp[i - dp[i-1] - 2]
                        
                max_length = max(max_length, dp[i])
                
        return max_length
    
    def longest_valid_parentheses_two_pass(self, s: str) -> int:
        """
        Find the length of the longest valid parentheses substring using two passes.
        
        Args:
            s: String containing only parentheses characters
            
        Returns:
            int: Length of the longest valid parentheses substring
        """
        max_length = 0
        left = right = 0
        
        # Left to right pass
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_length = max(max_length, 2 * right)
            elif right > left:
                # Invalid sequence, reset counters
                left = right = 0
                
        left = right = 0
        
        # Right to left pass
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
                
            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                # Invalid sequence, reset counters
                left = right = 0
                
        return max_length

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "(()"
    result1 = solution.longest_valid_parentheses(s1)
    print(f"Example 1: s='{s1}', result={result1}")  # Expected output: 2
    
    # Example 2
    s2 = ")()())"
    result2 = solution.longest_valid_parentheses(s2)
    print(f"Example 2: s='{s2}', result={result2}")  # Expected output: 4
    
    # Example 3
    s3 = ""
    result3 = solution.longest_valid_parentheses(s3)
    print(f"Example 3: s='{s3}', result={result3}")  # Expected output: 0
    
    # Additional example
    s4 = "()(())"
    result4 = solution.longest_valid_parentheses(s4)
    print(f"Example 4: s='{s4}', result={result4}")  # Expected output: 6
    
    # Compare with other implementations
    print("\nUsing dynamic programming approach:")
    print(f"Example 1: {solution.longest_valid_parentheses_dp(s1)}")  # Expected output: 2
    print(f"Example 2: {solution.longest_valid_parentheses_dp(s2)}")  # Expected output: 4
    
    print("\nUsing two-pass approach:")
    print(f"Example 1: {solution.longest_valid_parentheses_two_pass(s1)}")  # Expected output: 2
    print(f"Example 2: {solution.longest_valid_parentheses_two_pass(s2)}")  # Expected output: 4
