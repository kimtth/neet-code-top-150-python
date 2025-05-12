from typing import List

"""
LeetCode Plus One

Problem from LeetCode: https://leetcode.com/problems/plus-one/

Description:
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

class Solution:

    def plus_one(self, digits: List[int]) ->List[int]:
        """
        Add one to the integer represented by the digits array.
        
        The array represents a non-negative integer, where each element
        is a single digit, and the most significant digit is at the start.
        
        Args:
            digits: Array of digits representing a non-negative integer
            
        Returns:
            List[int]: The resulting array after adding one
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        result = [0] * (len(digits) + 1)
        result[0] = 1
        return result

    def plusOne_pythonic(self, digits: List[int]) ->List[int]:
        """
        Add one using a more Pythonic approach by converting to integer and back.
        
        Args:
            digits: Array of digits representing a non-negative integer
            
        Returns:
            List[int]: The resulting array after adding one
        """
        num = 0
        for digit in digits:
            num = num * 10 + digit
        num += 1
        return [int(digit) for digit in str(num)]

    def plusOne_direct(self, digits: List[int]) ->List[int]:
        """
        Add one directly to the array with explicit carry handling.
        
        Args:
            digits: Array of digits representing a non-negative integer
            
        Returns:
            List[int]: The resulting array after adding one
        """
        result = digits.copy()
        carry = 1
        for i in range(len(result) - 1, -1, -1):
            result[i] += carry
            carry = result[i] // 10
            result[i] %= 10
            if carry == 0:
                break
        if carry > 0:
            result.insert(0, carry)
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    digits1 = [1, 2, 3]
    result1 = solution.plus_one(digits1)
    print(f"Example 1: {digits1} + 1 = {result1}")  # Expected output: [1, 2, 4]
    
    # Example 2
    digits2 = [4, 3, 2, 1]
    result2 = solution.plus_one(digits2)
    print(f"Example 2: {digits2} + 1 = {result2}")  # Expected output: [4, 3, 2, 2]
    
    # Example 3
    digits3 = [9]
    result3 = solution.plus_one(digits3)
    print(f"Example 3: {digits3} + 1 = {result3}")  # Expected output: [1, 0]
    
    # Additional example with all 9s
    digits4 = [9, 9, 9]
    result4 = solution.plus_one(digits4)
    print(f"Example 4: {digits4} + 1 = {result4}")  # Expected output: [1, 0, 0, 0]
    
    # Compare different implementations
    print("\nComparing implementations:")
    digits5 = [4, 9, 9, 9]
    print(f"Standard: {solution.plus_one(digits5.copy())}")
    print(f"Pythonic: {solution.plusOne_pythonic(digits5.copy())}")
    print(f"Direct: {solution.plusOne_direct(digits5.copy())}")
