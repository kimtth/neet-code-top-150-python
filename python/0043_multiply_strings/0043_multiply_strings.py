from typing import List, Optional

"""
LeetCode Multiply Strings

Problem from LeetCode: https://leetcode.com/problems/multiply-strings/

Description:
Given two non-negative integers represented as strings, return their product.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Multiply two numbers represented as strings without converting to integers.
        
        Args:
            num1: First number as a string
            num2: Second number as a string
            
        Returns:
            str: Product of num1 and num2 as a string
        """
        # Handle edge cases
        if num1 == "0" or num2 == "0":
            return "0"
            
        # Initialize result array with zeros
        # The product of two numbers can have at most len(num1) + len(num2) digits
        result = [0] * (len(num1) + len(num2))
        
        # Perform multiplication digit by digit
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Convert characters to integers
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # Calculate position in the result array
                pos_low = i + j + 1
                pos_high = i + j
                
                # Multiply and add to current result
                product = digit1 * digit2
                total = product + result[pos_low]
                
                # Update the result array
                result[pos_low] = total % 10
                result[pos_high] += total // 10
                
        # Convert the result array to a string
        result_str = ""
        for digit in result:
            # Skip leading zeros
            if not (result_str == "" and digit == 0):
                result_str += str(digit)
                
        return result_str if result_str else "0"
    
    def multiply_simplify(self, num1: str, num2: str) -> str:
        """
        Alternative implementation with cleaner approach.
        
        Args:
            num1: First number as a string
            num2: Second number as a string
            
        Returns:
            str: Product of num1 and num2 as a string
        """
        if num1 == "0" or num2 == "0":
            return "0"
            
        # Ensure num1 is the shorter number for optimization
        if len(num1) > len(num2):
            num1, num2 = num2, num1
            
        # Initialize the product as 0
        product = 0
        
        # Process each digit of num1
        for i, digit1 in enumerate(num1):
            # Convert the digit to integer
            d1 = int(digit1)
            
            # Multiply with each digit of num2
            for j, digit2 in enumerate(num2):
                d2 = int(digit2)
                
                # Calculate positional value - working with integers for clarity
                pos_value = d1 * d2 * 10 ** (len(num1) - i - 1 + len(num2) - j - 1)
                product += pos_value
                
        return str(product)

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    num1_1 = "2"
    num2_1 = "3"
    result1 = solution.multiply(num1_1, num2_1)
    print(f"Example 1: {num1_1} * {num2_1} = {result1}")  # Expected output: "6"
    
    # Example 2
    num1_2 = "123"
    num2_2 = "456"
    result2 = solution.multiply(num1_2, num2_2)
    print(f"Example 2: {num1_2} * {num2_2} = {result2}")  # Expected output: "56088"
    
    # Additional example
    num1_3 = "999"
    num2_3 = "999"
    result3 = solution.multiply(num1_3, num2_3)
    print(f"Example 3: {num1_3} * {num2_3} = {result3}")  # Expected output: "998001"
    
    # Edge case
    num1_4 = "0"
    num2_4 = "52"
    result4 = solution.multiply(num1_4, num2_4)
    print(f"Example 4: {num1_4} * {num2_4} = {result4}")  # Expected output: "0"
    
    # Note: The simplified approach converts to integers internally,
    # so it doesn't strictly follow the problem constraints,
    # but it demonstrates an alternative approach.
