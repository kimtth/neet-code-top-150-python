from typing import List

"""
LeetCode Longest Palindromic Substring

Problem from LeetCode: https://leetcode.com/problems/longest-palindromic-substring/

Description:
Given a string s, return the longest palindromic substring in s.
A palindrome is a string that reads the same backward as forward.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"
"""

class Solution:
    def longest_palindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring in a string.
        
        Args:
            s: Input string
            
        Returns:
            str: Longest palindromic substring
        """
        if not s:
            return ""
            
        start = 0
        max_length = 1
        
        # Helper function to expand around center
        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            # Expand for odd length palindromes
            odd_length = expand_around_center(i, i)
            # Expand for even length palindromes
            even_length = expand_around_center(i, i + 1)
            
            # Find the maximum length palindrome
            curr_length = max(odd_length, even_length)
            if curr_length > max_length:
                max_length = curr_length
                # Calculate the starting position of the palindrome
                start = i - (curr_length - 1) // 2
                
        return s[start:start + max_length]

    def longest_palindrome_dp(self, s: str) -> str:
        """
        Find the longest palindromic substring using dynamic programming.
        
        Args:
            s: Input string
            
        Returns:
            str: Longest palindromic substring
        """
        if not s:
            return ""
            
        n = len(s)
        # dp[i][j] will be True if substring s[i:j+1] is a palindrome
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        # All single characters are palindromes
        for i in range(n):
            dp[i][i] = True
            
        start = 0
        max_length = 1
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2
                
        # Check for palindromes of length > 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index
                # Check if s[i:j+1] is a palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length
                    
        return s[start:start + max_length]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "babad"
    result1 = solution.longest_palindrome(s1)
    print(f"Example 1: '{s1}' -> '{result1}'")  # Expected output: "bab" or "aba"
    
    # Example 2
    s2 = "cbbd"
    result2 = solution.longest_palindrome(s2)
    print(f"Example 2: '{s2}' -> '{result2}'")  # Expected output: "bb"
    
    # Example 3
    s3 = "a"
    result3 = solution.longest_palindrome(s3)
    print(f"Example 3: '{s3}' -> '{result3}'")  # Expected output: "a"
    
    # Compare with DP approach
    print("\nUsing dynamic programming approach:")
    result1_dp = solution.longest_palindrome_dp(s1)
    print(f"Example 1 DP: '{s1}' -> '{result1_dp}'")
