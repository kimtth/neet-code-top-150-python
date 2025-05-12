from typing import List, Optional

"""
LeetCode 191. Number of 1 Bits

Problem from LeetCode: https://leetcode.com/problems/number-of-1-bits/

Description:
Write a function that takes an unsigned integer and returns the number of '1' bits it has 
(also known as the Hamming weight).

Note:
- Note that in some languages, such as Java, there is no unsigned integer type. 
  In this case, the input will be given as a signed integer type. 
  It should not affect your implementation, as the integer's internal binary representation is the same, 
  whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement notation. 
  Therefore, in Example 3, the input represents the signed integer -3.

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Constraints:
- The input must be a binary string of length 32.

Follow up: If this function is called many times, how would you optimize it?
"""

class Solution:

    def hamming_weight(self, n: int) ->int:
        """
        Returns the number of '1' bits in the binary representation of n.
        
        This uses Brian Kernighan's algorithm:
        n & (n-1) clears the least significant '1' bit in n.
        We count how many times we can do this until n becomes 0.
        """
        count = 0
        while n != 0:
            count += 1
            n = n & n - 1
        return count

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    n1 = 0b00000000000000000000000000001011  # 11 in decimal
    result1 = solution.hamming_weight(n1)
    print(f"Input: n = {bin(n1)} ({n1})")
    print(f"Output: {result1}")  # Expected output: 3
    
    # Example 2
    n2 = 0b00000000000000000000000010000000  # 128 in decimal
    result2 = solution.hamming_weight(n2)
    print(f"Input: n = {bin(n2)} ({n2})")
    print(f"Output: {result2}")  # Expected output: 1
    
    # Example 3
    n3 = 0b11111111111111111111111111111101  # -3 as signed 32-bit int
    result3 = solution.hamming_weight(n3)
    print(f"Input: n = {bin(n3)} ({n3})")
    print(f"Output: {result3}")  # Expected output: 31
