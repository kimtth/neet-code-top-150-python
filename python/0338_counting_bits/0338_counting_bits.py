from typing import List


"""
LeetCode Counting Bits

Problem from LeetCode: https://leetcode.com/problems/counting-bits/

Description:
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0 (0 '1' bits)
1 --> 1 (1 '1' bit)
2 --> 10 (1 '1' bit)

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0 (0 '1' bits)
1 --> 1 (1 '1' bit)
2 --> 10 (1 '1' bit)
3 --> 11 (2 '1' bits)
4 --> 100 (1 '1' bit)
5 --> 101 (2 '1' bits)

Constraints:
0 <= n <= 10^5

Follow up:
- It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
- Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""

class Solution:

    def count_bits(self, n: int) -> List[int]:
        """
        Count the number of 1's in the binary representation of each integer from 0 to n.
        
        This is the efficient dynamic programming approach with O(n) time complexity.
        
        Args:
            n: Upper limit of the range
            
        Returns:
            List[int]: Array where ans[i] is the count of 1 bits in integer i
        """
        # Initialize the result array
        ans = [0] * (n + 1)
        
        # For each number from 1 to n
        for i in range(1, n + 1):
            # The number of 1's in i is equal to:
            # The number of 1's in i//2 plus 1 if i is odd (has a 1 in the least significant bit)
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans

    def count_bits_dp_offset(self, n: int) -> List[int]:
        """
        Count the number of 1's using a dynamic programming approach with offset.
        
        For a number x, if we know the last power of 2 less than or equal to x,
        we can use it as an offset.
        
        Args:
            n: Upper limit of the range
            
        Returns:
            List[int]: Array where ans[i] is the count of 1 bits in integer i
        """
        ans = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            # If i is a power of 2, update the offset
            if offset * 2 == i:
                offset = i
            
            # Use the offset to calculate the number of 1's
            ans[i] = 1 + ans[i - offset]
        
        return ans

    def count_bits_builtin(self, n: int) -> List[int]:
        """
        Count the number of 1's using Python's built-in bin() function.
        This is the most straightforward but least efficient solution.
        
        Args:
            n: Upper limit of the range
            
        Returns:
            List[int]: Array where ans[i] is the count of 1 bits in integer i
        """
        ans = []
        for i in range(n + 1):
            # Count the number of '1' characters in the binary representation
            ans.append(bin(i).count('1'))
        
        return ans


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    n1 = 2
    result1 = solution.count_bits(n1)
    print(f"Example 1: {result1}")  # Expected output: [0, 1, 1]
    
    # Example 2
    n2 = 5
    result2 = solution.count_bits(n2)
    print(f"Example 2: {result2}")  # Expected output: [0, 1, 1, 2, 1, 2]
    
    # Additional example
    n3 = 10
    result3 = solution.count_bits(n3)
    print(f"Example 3: {result3}")  # Expected output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
    
    # Using offset-based DP approach
    print("\nUsing offset-based DP approach:")
    result4 = solution.count_bits_dp_offset(n2)
    print(f"Example 2: {result4}")  # Expected output: [0, 1, 1, 2, 1, 2]
    
    # Using built-in function approach
    print("\nUsing built-in function approach:")
    result5 = solution.count_bits_builtin(n2)
    print(f"Example 2: {result5}")  # Expected output: [0, 1, 1, 2, 1, 2]
