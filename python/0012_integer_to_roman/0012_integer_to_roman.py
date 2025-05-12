from typing import List

"""
LeetCode Integer to Roman

Problem from LeetCode: https://leetcode.com/problems/integer-to-roman/

Description:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I            1
V            5
X            10
L            50
C            100
D            500
M            1000

For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution:
    def int_to_roman(self, num: int) -> str:
        """
        Convert an integer to its Roman numeral representation.
        
        Args:
            num: An integer in the range [1, 3999]
            
        Returns:
            str: Roman numeral representation of the input
        """
        # Define the mapping of values to Roman numerals
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = ""
        # Iterate through each value-numeral pair
        for i in range(len(values)):
            # Add the numeral as many times as possible
            while num >= values[i]:
                result += numerals[i]
                num -= values[i]
                
        return result
    
    def int_to_roman_direct_mapping(self, num: int) -> str:
        """
        Alternative implementation using direct mapping of digit positions.
        
        Args:
            num: An integer in the range [1, 3999]
            
        Returns:
            str: Roman numeral representation of the input
        """
        # Define mappings for each place value
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        # Combine the Roman numerals for each place value
        return (thousands[num // 1000] + 
                hundreds[(num % 1000) // 100] + 
                tens[(num % 100) // 10] + 
                ones[num % 10])


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    num1 = 3
    result1 = solution.int_to_roman(num1)
    print(f"Example 1: {num1} -> {result1}")  # Expected output: "III"
    
    # Example 2
    num2 = 58
    result2 = solution.int_to_roman(num2)
    print(f"Example 2: {num2} -> {result2}")  # Expected output: "LVIII"
    
    # Example 3
    num3 = 1994
    result3 = solution.int_to_roman(num3)
    print(f"Example 3: {num3} -> {result3}")  # Expected output: "MCMXCIV"
    
    # Additional examples
    num4 = 2023
    result4 = solution.int_to_roman(num4)
    print(f"Example 4: {num4} -> {result4}")  # Expected output: "MMXXIII"
    
    # Compare with direct mapping implementation
    print("\nUsing direct mapping approach:")
    print(f"Example 1: {num1} -> {solution.int_to_roman_direct_mapping(num1)}")
    print(f"Example 2: {num2} -> {solution.int_to_roman_direct_mapping(num2)}")
    print(f"Example 3: {num3} -> {solution.int_to_roman_direct_mapping(num3)}")
