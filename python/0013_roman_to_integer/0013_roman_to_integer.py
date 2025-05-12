from typing import List

"""
LeetCode Roman to Integer

Problem from LeetCode: https://leetcode.com/problems/roman-to-integer/

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

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution:
    def roman_to_int(self, s: str) -> int:
        """
        Convert a Roman numeral to an integer.
        
        Args:
            s: A string representing a valid Roman numeral in the range [1, 3999]
            
        Returns:
            int: The integer value of the Roman numeral
        """
        # Define the mapping of Roman numerals to integers
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        i = 0
        
        while i < len(s):
            # If this is the subtractive case
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # Else this is regular case
            else:
                total += values[s[i]]
                i += 1
                
        return total
    
    def roman_to_int_simpler(self, s: str) -> int:
        """
        A simpler implementation that processes the string from right to left.
        
        Args:
            s: A string representing a valid Roman numeral
            
        Returns:
            int: The integer value of the Roman numeral
        """
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Process the string from right to left
        for char in reversed(s):
            current_value = values[char]
            # If current value is greater than or equal to previous value, add it
            if current_value >= prev_value:
                total += current_value
            # Otherwise, subtract it (handles cases like IV, IX, etc.)
            else:
                total -= current_value
            prev_value = current_value
            
        return total


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "III"
    result1 = solution.roman_to_int(s1)
    print(f"Example 1: '{s1}' -> {result1}")  # Expected output: 3
    
    # Example 2
    s2 = "LVIII"
    result2 = solution.roman_to_int(s2)
    print(f"Example 2: '{s2}' -> {result2}")  # Expected output: 58
    
    # Example 3
    s3 = "MCMXCIV"
    result3 = solution.roman_to_int(s3)
    print(f"Example 3: '{s3}' -> {result3}")  # Expected output: 1994
    
    # Additional examples
    s4 = "MMXXIII"
    result4 = solution.roman_to_int(s4)
    print(f"Example 4: '{s4}' -> {result4}")  # Expected output: 2023
    
    # Compare with simpler implementation
    print("\nUsing simpler approach (right to left):")
    print(f"Example 1: '{s1}' -> {solution.roman_to_int_simpler(s1)}")
    print(f"Example 2: '{s2}' -> {solution.roman_to_int_simpler(s2)}")
    print(f"Example 3: '{s3}' -> {solution.roman_to_int_simpler(s3)}")
