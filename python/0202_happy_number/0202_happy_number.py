from typing import List, Optional

"""
LeetCode 202. Happy Number

Problem from LeetCode: https://leetcode.com/problems/happy-number/

Description:
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy numbers.

Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1

Example 2:
Input: n = 2
Output: false

Constraints:
- 1 <= n <= 2³¹ - 1
"""

class Solution:

    def is_happy(self, n: int) ->bool:
        """
        Determine if a number is "happy".
        
        A happy number is defined by the following process:
        - Starting with any positive integer, replace the number by the sum of the squares of its digits.
        - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle.
        - Those numbers for which this process ends in 1 are happy numbers.
        
        Args:
            n: A positive integer
            
        Returns:
            bool: True if n is a happy number, False otherwise
        """
        seen_numbers = set()
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = self._get_sum_of_squares(n)
        return n == 1

    def _get_sum_of_squares(self, n: int) ->int:
        """
        Calculate the sum of squares of digits in a number.
        
        Args:
            n: A positive integer
            
        Returns:
            int: Sum of squares of digits
        """
        sum_squares = 0
        while n > 0:
            digit = n % 10
            sum_squares += digit * digit
            n //= 10
        return sum_squares


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    n1 = 19
    result1 = solution.is_happy(n1)
    print(f"Input: n = {n1}")
    print(f"Output: {result1}")  # Expected output: True
    
    # Example 2
    n2 = 2
    result2 = solution.is_happy(n2)
    print(f"Input: n = {n2}")
    print(f"Output: {result2}")  # Expected output: False
    
    # Additional example
    n3 = 7
    result3 = solution.is_happy(n3)
    print(f"Input: n = {n3}")
    print(f"Output: {result3}")  # Expected output: True
