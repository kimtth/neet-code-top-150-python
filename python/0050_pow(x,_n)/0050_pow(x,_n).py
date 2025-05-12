from typing import List, Optional

"""
LeetCode Pow(x, n)

Problem from LeetCode: https://leetcode.com/problems/powx-n/

Description:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
"""

class Solution:

    def my_pow(self, x: float, n: int) ->float:
        """
        Implement pow(x, n), which calculates x raised to the power n.
        
        Uses fast power algorithm (binary exponentiation) for efficiency.
        
        Args:
            x: Base (floating-point number)
            n: Exponent (integer)
            
        Returns:
            float: Result of x^n
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        current_product = x
        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2
        return result

    def myPow_recursive(self, x: float, n: int) ->float:
        """
        Recursive implementation of pow(x, n).
        
        Args:
            x: Base (floating-point number)
            n: Exponent (integer)
            
        Returns:
            float: Result of x^n
        """
        if n < 0:
            return self.myPow_recursive(1 / x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        half = self.myPow_recursive(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half

    def myPow_pythonic(self, x: float, n: int) ->float:
        """
        Pythonic implementation using the built-in ** operator.
        
        Args:
            x: Base (floating-point number)
            n: Exponent (integer)
            
        Returns:
            float: Result of x^n
        """
        return x ** n


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    x1, n1 = 2.00000, 10
    result1 = solution.my_pow(x1, n1)
    print(f"Example 1: {x1}^{n1} = {result1}")  # Expected output: 1024.00000
    
    # Example 2
    x2, n2 = 2.10000, 3
    result2 = solution.my_pow(x2, n2)
    print(f"Example 2: {x2}^{n2} = {result2}")  # Expected output: 9.26100
    
    # Example 3
    x3, n3 = 2.00000, -2
    result3 = solution.my_pow(x3, n3)
    print(f"Example 3: {x3}^{n3} = {result3}")  # Expected output: 0.25000
    
    # Compare different implementations
    print("\nComparing implementations:")
    x4, n4 = 3.00000, 4
    print(f"Iterative: {x4}^{n4} = {solution.my_pow(x4, n4)}")
    print(f"Recursive: {x4}^{n4} = {solution.myPow_recursive(x4, n4)}")
    print(f"Pythonic: {x4}^{n4} = {solution.myPow_pythonic(x4, n4)}")
