from typing import List, Optional

"""
LeetCode Sum Of Two Integers

Problem from LeetCode: https://leetcode.com/problems/sum-of-two-integers/

Description:
Given two integers a and b, return the sum of the two integers without using the + and - operators.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:
-1000 <= a, b <= 1000
"""

class Solution:

    def get_sum(self, a: int, b: int) ->int:
        """
        Calculate the sum of two integers a and b without using the + and - operators.
        
        Args:
            a: First integer
            b: Second integer
            
        Returns:
            int: Sum of a and b
        """
        mask = 4294967295
        while b != 0:
            temp = (a ^ b) & mask
            carry = (a & b) << 1 & mask
            a = temp
            b = carry
        if a > mask // 2:
            return ~(a ^ mask)
        return a

    def get_sum_recursive(self, a: int, b: int) ->int:
        """
        Calculate the sum using a recursive approach.
        
        Args:
            a: First integer
            b: Second integer
            
        Returns:
            int: Sum of a and b
        """
        mask = 4294967295
        if b == 0:
            if a > mask // 2:
                return ~(a ^ mask)
            return a
        sum_without_carry = (a ^ b) & mask
        carry = (a & b) << 1 & mask
        return self.get_sum_recursive(sum_without_carry, carry)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    a1, b1 = 1, 2
    result1 = solution.get_sum(a1, b1)
    print(f"Example 1: {a1} + {b1} = {result1}")  # Expected output: 3
    
    # Example 2
    a2, b2 = 2, 3
    result2 = solution.get_sum(a2, b2)
    print(f"Example 2: {a2} + {b2} = {result2}")  # Expected output: 5
    
    # Example 3 - with negative numbers
    a3, b3 = -1, 1
    result3 = solution.get_sum(a3, b3)
    print(f"Example 3: {a3} + {b3} = {result3}")  # Expected output: 0
    
    # Recursive approach
    print("\nRecursive approach:")
    result4 = solution.get_sum_recursive(a1, b1)
    print(f"Example 1: {a1} + {b1} = {result4}")  # Expected output: 3
