from typing import List

"""
LeetCode Maximum Product Subarray

Problem from LeetCode: https://leetcode.com/problems/maximum-product-subarray/

Problem Statement:
Given an integer array nums, find a contiguous non-empty subarray within the array 
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Examples:
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def max_product(self, nums: List[int]) -> int:
        """
        Find the contiguous subarray with the largest product.
        
        This solution uses a dynamic programming approach that keeps track of both
        the maximum and minimum products ending at the current position. We need to
        track the minimum because a negative number times a negative number can become
        a positive number and potentially contribute to the maximum product.
        
        Args:
            nums: Array of integers
            
        Returns:
            Maximum product of any contiguous subarray
        """
        if not nums:
            return 0
            
        min_so_far = nums[0]
        max_so_far = nums[0]
        result = max_so_far
        
        for i in range(1, len(nums)):
            curr = nums[i]
            # We need to consider three values: current number, max_so_far * curr, and min_so_far * curr
            # because multiplying by a negative number flips min and max
            temp = max(curr, max(max_so_far * curr, min_so_far * curr))
            min_so_far = min(curr, min(min_so_far * curr, max_so_far * curr))
            max_so_far = temp
            result = max(result, max_so_far)
            
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    sample_input1 = [2, 3, -2, 4]
    result1 = solution.max_product(sample_input1)
    print(f"Example 1: {result1}")  # Expected output: 6
    
    # Example 2
    sample_input2 = [-2, 0, -1]
    result2 = solution.max_product(sample_input2)
    print(f"Example 2: {result2}")  # Expected output: 0
    
    # Additional example with negative numbers
    sample_input3 = [-2, -3, -2, -4]
    result3 = solution.max_product(sample_input3)
    print(f"Example 3: {result3}")  # Expected output: 48