from typing import List


"""
LeetCode 238. Product of Array Except Self

Problem from LeetCode: https://leetcode.com/problems/product-of-array-except-self/

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm running in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

class Solution:

    def product_except_self(self, nums: List[int]) ->List[int]:
        """
        Return an array where each element is the product of all elements in the input array except itself.
        
        Args:
            nums: Array of integers
            
        Returns:
            List[int]: Product array
        """
        n = len(nums)
        result = [1] * n
        
        # Calculate products of all elements to the left of each element
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
            
        # Calculate products of all elements to the right and multiply with left products
        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
            
        return result

    def product_except_self_with_division(self, nums: List[int]) ->List[int]:
        """
        Using division (note: this approach fails if there are zeros in the array)
        
        Args:
            nums: Array of integers (with no zeros)
            
        Returns:
            List[int]: Product array
        """
        total_product = 1
        for num in nums:
            total_product *= num
            
        return [(total_product // num) for num in nums]

    def product_except_self_optimized(self, nums: List[int]) ->List[int]:
        """
        Same algorithm but with O(1) extra space complexity.
        
        Args:
            nums: Array of integers
            
        Returns:
            List[int]: Product array
        """
        n = len(nums)
        result = [1] * n
        
        # Calculate products of all elements to the left of each element
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]
            
        # Calculate products of all elements to the right and multiply with left products
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
            
        return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [1, 2, 3, 4]
    result1 = solution.product_except_self(nums1)
    print(f"Example 1: nums = {nums1}")
    print(f"Output: {result1}")  # Expected output: [24, 12, 8, 6]
    
    # Example 2
    nums2 = [-1, 1, 0, -3, 3]
    result2 = solution.product_except_self(nums2)
    print(f"\nExample 2: nums = {nums2}")
    print(f"Output: {result2}")  # Expected output: [0, 0, 9, 0, 0]
    
    # Test optimized version
    print("\nOptimized version (O(1) extra space):")
    result1_opt = solution.product_except_self_optimized(nums1)
    print(f"Example 1: {result1_opt}")
    
    result2_opt = solution.product_except_self_optimized(nums2)
    print(f"Example 2: {result2_opt}")
    
    # Test with division (only for arrays without zeros)
    try:
        print("\nUsing division (only works without zeros):")
        result1_div = solution.product_except_self_with_division(nums1)
        print(f"Example 1: {result1_div}")
        
        result2_div = solution.product_except_self_with_division(nums2)
        print(f"Example 2: {result2_div}")
    except ZeroDivisionError:
        print("Division approach fails with zeros in the array.")
