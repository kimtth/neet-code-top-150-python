from typing import List


"""
LeetCode Missing Number

Problem from LeetCode: https://leetcode.com/problems/missing-number/

Description:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
"""

class Solution:

    def missing_number(self, nums: List[int]) ->int:
        """
        Find the missing number in the range [0, n] from nums.
        
        Uses XOR operations where:
        - XOR of a number with itself is 0
        - XOR of a number with 0 is the number itself
        - XOR is commutative and associative
        
        Args:
            nums: List of n distinct numbers in the range [0, n]
            
        Returns:
            int: The missing number in the range
        """
        xor = 0
        for i in range(len(nums) + 1):
            xor ^= i
        for num in nums:
            xor ^= num
        return xor

    def missing_number_using_sum(self, nums: List[int]) ->int:
        """
        Find the missing number using mathematical approach.
        
        Args:
            nums: List of n distinct numbers in the range [0, n]
            
        Returns:
            int: The missing number in the range
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    def missing_number_using_set(self, nums: List[int]) ->int:
        """
        Find the missing number using a set.
        
        Args:
            nums: List of n distinct numbers in the range [0, n]
            
        Returns:
            int: The missing number in the range
        """
        num_set = set(nums)
        n = len(nums)
        for i in range(n + 1):
            if i not in num_set:
                return i
        return -1


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [3, 0, 1]
    result1 = solution.missing_number(nums1)
    print(f"Example 1: {result1}")  # Expected output: 2
    
    # Example 2
    nums2 = [0, 1]
    result2 = solution.missing_number(nums2)
    print(f"Example 2: {result2}")  # Expected output: 2
    
    # Example 3
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    result3 = solution.missing_number(nums3)
    print(f"Example 3: {result3}")  # Expected output: 8
