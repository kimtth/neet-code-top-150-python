from typing import List

"""
LeetCode Palindrome Number

Problem from LeetCode: https://leetcode.com/problems/palindrome-number/

Description:
Given an integer x, return true if x is a palindrome, and false otherwise.
An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    def is_palindrome(self, x: int) -> bool:
        """
        Determine if an integer is a palindrome.
        
        Args:
            x: Input integer
            
        Returns:
            bool: True if x is a palindrome, False otherwise
        """
        # Negative numbers are not palindromes due to the minus sign
        if x < 0:
            return False
            
        # Single digit numbers are palindromes
        if x < 10:
            return True
            
        # If the last digit is 0, the first digit must also be 0
        # The only number that satisfies this is 0 itself
        if x % 10 == 0 and x != 0:
            return False
            
        # Reverse the second half of the number and compare with the first half
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
            
        # When the length is odd, we need to divide reversed_half by 10
        # For example: 12321, at the end of the loop x = 12, reversed_half = 123
        # So we need to remove the middle digit from reversed_half
        return x == reversed_half or x == reversed_half // 10
    
    def is_palindrome_string(self, x: int) -> bool:
        """
        Determine if an integer is a palindrome using string conversion.
        
        Args:
            x: Input integer
            
        Returns:
            bool: True if x is a palindrome, False otherwise
        """
        # Convert to string and check if it equals its reverse
        s = str(x)
        return s == s[::-1]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    x1 = 121
    result1 = solution.is_palindrome(x1)
    print(f"Example 1: {x1} -> {result1}")  # Expected output: True
    
    # Example 2
    x2 = -121
    result2 = solution.is_palindrome(x2)
    print(f"Example 2: {x2} -> {result2}")  # Expected output: False
    
    # Example 3
    x3 = 10
    result3 = solution.is_palindrome(x3)
    print(f"Example 3: {x3} -> {result3}")  # Expected output: False
    
    # Additional examples
    x4 = 12321
    result4 = solution.is_palindrome(x4)
    print(f"Example 4: {x4} -> {result4}")  # Expected output: True
    
    # Compare with string method
    print("\nUsing string conversion method:")
    print(f"Example 1: {x1} -> {solution.is_palindrome_string(x1)}")
    print(f"Example 2: {x2} -> {solution.is_palindrome_string(x2)}")
    print(f"Example 3: {x3} -> {solution.is_palindrome_string(x3)}")
