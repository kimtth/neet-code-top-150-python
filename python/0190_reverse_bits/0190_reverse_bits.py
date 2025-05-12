from typing import List, Optional

"""
LeetCode Reverse Bits

Problem from LeetCode: https://leetcode.com/problems/reverse-bits/

Description:
Reverse bits of a given 32 bits unsigned integer.

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
"""

class Solution:
    def reverse_bits(self, n: int) -> int:
        """
        Reverse the bits of a 32-bit unsigned integer.
        
        Args:
            n: 32-bit unsigned integer
            
        Returns:
            int: Integer with reversed bits
        """
        reverse = 0
        for i in range(32):
            reverse = reverse << 1
            reverse = reverse | n & 1
            n = n >> 1
        return reverse
    
    def reverse_bits_pythonic(self, n: int) -> int:
        """
        Reverse bits using Python's built-in bin function.
        
        Args:
            n: 32-bit unsigned integer
            
        Returns:
            int: Integer with reversed bits
        """
        # Convert to binary string, remove '0b' prefix, pad to 32 bits, reverse, convert back to int
        binary_str = bin(n)[2:].zfill(32)
        reversed_str = binary_str[::-1]
        return int(reversed_str, 2)
    
    def reverse_bits_divide_conquer(self, n: int) -> int:
        """
        Reverse bits using a divide and conquer approach.
        
        Args:
            n: 32-bit unsigned integer
            
        Returns:
            int: Integer with reversed bits
        """
        # Swap adjacent bits
        n = ((n & 0x55555555) << 1) | ((n & 0xAAAAAAAA) >> 1)
        # Swap adjacent pairs
        n = ((n & 0x33333333) << 2) | ((n & 0xCCCCCCCC) >> 2)
        # Swap adjacent nibbles
        n = ((n & 0x0F0F0F0F) << 4) | ((n & 0xF0F0F0F0) >> 4)
        # Swap adjacent bytes
        n = ((n & 0x00FF00FF) << 8) | ((n & 0xFF00FF00) >> 8)
        # Swap adjacent 16-bit fields
        n = ((n & 0x0000FFFF) << 16) | ((n & 0xFFFF0000) >> 16)
        
        return n


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    n1 = 0b00000010100101000001111010011100  # 43261596 in decimal
    result1 = solution.reverse_bits(n1)
    print(f"Example 1: {n1} ({bin(n1)}) -> {result1} ({bin(result1)})")
    print(f"Expected output: 964176192 (0b111001011110000010100101000000)")
    
    # Example 2
    n2 = 0b11111111111111111111111111111101  # 4294967293 in decimal
    result2 = solution.reverse_bits(n2)
    print(f"Example 2: {n2} -> {result2}")
    print(f"Expected output: 3221225471")
    
    # Compare with Pythonic approach
    print("\nUsing Pythonic approach:")
    print(f"Example 1: {solution.reverse_bits_pythonic(n1)}")
    
    # Compare with divide and conquer approach
    print("\nUsing divide and conquer approach:")
    print(f"Example 1: {solution.reverse_bits_divide_conquer(n1)}")
