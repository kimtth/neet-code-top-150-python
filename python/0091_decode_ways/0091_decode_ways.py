from typing import Dict


"""
LeetCode Decode Ways

Problem from LeetCode: https://leetcode.com/problems/decode-ways/

Description:
A message containing letters from A-Z can be encoded into numbers using the mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
- "AAJF" with the grouping (1 1 10 6)
- "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Calculate the number of ways to decode a string of digits.
        Uses dynamic programming with constant space.
        
        Args:
            s: String containing only digits
            
        Returns:
            int: Number of ways to decode the string
        """
        if not s or s[0] == '0':
            return 0
            
        # Initialize variables to track ways to decode
        # prev2: ways to decode s[0:i-2]
        # prev1: ways to decode s[0:i-1]
        # current: ways to decode s[0:i]
        prev2, prev1 = 1, 1
        
        for i in range(1, len(s)):
            current = 0
            
            # Check if current digit is valid (not '0')
            if s[i] != '0':
                current += prev1
                
            # Check if current and previous digits form a valid code (10-26)
            # Get the value of the two-digit number
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
                
            # Shift values for next iteration
            prev2, prev1 = prev1, current
            
        return prev1
    
    def numDecodings_memo(self, s: str) -> int:
        """
        Calculate the number of ways to decode a string using memoization.
        
        Args:
            s: String containing only digits
            
        Returns:
            int: Number of ways to decode the string
        """
        # Memoization dictionary
        memo = {}
        
        def dp(index: int) -> int:
            """Recursive helper function with memoization."""
            # Base case: reached the end of the string
            if index == len(s):
                return 1
                
            # Base case: invalid leading zero
            if s[index] == '0':
                return 0
                
            # Check if result is already memoized
            if index in memo:
                return memo[index]
                
            # Decode current digit
            ways = dp(index + 1)
            
            # Decode two digits if possible
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                ways += dp(index + 2)
                
            # Memoize and return
            memo[index] = ways
            return ways
            
        return dp(0)
    
    def numDecodings_tabulation(self, s: str) -> int:
        """
        Calculate the number of ways to decode a string using tabulation.
        
        Args:
            s: String containing only digits
            
        Returns:
            int: Number of ways to decode the string
        """
        n = len(s)
        # dp[i] represents the number of ways to decode s[0:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty string has 1 way to decode
        
        for i in range(1, n + 1):
            # Single digit decode
            if s[i-1] != '0':
                dp[i] += dp[i-1]
                
            # Two digit decode
            if i > 1 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "12"
    result1 = solution.numDecodings(s1)
    print(f"Example 1: s='{s1}', result={result1}")  # Expected output: 2
    
    # Example 2
    s2 = "226"
    result2 = solution.numDecodings(s2)
    print(f"Example 2: s='{s2}', result={result2}")  # Expected output: 3
    
    # Example 3
    s3 = "06"
    result3 = solution.numDecodings(s3)
    print(f"Example 3: s='{s3}', result={result3}")  # Expected output: 0
    
    # Additional example
    s4 = "10"
    result4 = solution.numDecodings(s4)
    print(f"Example 4: s='{s4}', result={result4}")  # Expected output: 1
    
    # Compare with other approaches
    print("\nUsing memoization approach:")
    print(f"Example 1: {solution.numDecodings_memo(s1)}")
    print(f"Example 2: {solution.numDecodings_memo(s2)}")
    
    print("\nUsing tabulation approach:")
    print(f"Example 1: {solution.numDecodings_tabulation(s1)}")
    print(f"Example 2: {solution.numDecodings_tabulation(s2)}")
