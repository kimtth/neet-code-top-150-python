from typing import List

"""
LeetCode Maximum Subarray

Problem from LeetCode: https://leetcode.com/problems/maximum-subarray/

Description:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""

class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        """
        Find the contiguous subarray with the largest sum using Kadane's algorithm.
        
        Args:
            nums: Array of integers
            
        Returns:
            int: The largest sum of a contiguous subarray
        """
        if not nums:
            return 0
        
        # Initialize variables to track current sum and maximum sum
        curr_sum = max_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Either start a new subarray or extend the existing one
            curr_sum = max(num, curr_sum + num)
            # Update the maximum sum if necessary
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
    
    def max_sub_array_divide_conquer(self, nums: List[int]) -> int:
        """
        Find the maximum subarray sum using a divide and conquer approach.
        
        Args:
            nums: Array of integers
            
        Returns:
            int: The largest sum of a contiguous subarray
        """
        def find_max_crossing(nums, left, mid, right):
            """Find the maximum sum crossing the middle element."""
            # Find maximum subarray sum including the middle element and extending to the left
            left_sum = float('-inf')
            curr_sum = 0
            for i in range(mid, left - 1, -1):
                curr_sum += nums[i]
                left_sum = max(left_sum, curr_sum)
            
            # Find maximum subarray sum including the middle element and extending to the right
            right_sum = float('-inf')
            curr_sum = 0
            for i in range(mid + 1, right + 1):
                curr_sum += nums[i]
                right_sum = max(right_sum, curr_sum)
            
            # Return the sum of the two parts
            return left_sum + right_sum
        
        def find_max_subarray(nums, left, right):
            """Recursively find the maximum subarray sum."""
            # Base case: single element
            if left == right:
                return nums[left]
            
            # Divide the array
            mid = (left + right) // 2
            
            # Find max in left half, right half, and crossing the middle
            left_max = find_max_subarray(nums, left, mid)
            right_max = find_max_subarray(nums, mid + 1, right)
            cross_max = find_max_crossing(nums, left, mid, right)
            
            # Return the maximum of the three
            return max(left_max, right_max, cross_max)
        
        return find_max_subarray(nums, 0, len(nums) - 1)

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = solution.max_sub_array(nums1)
    print(f"Example 1: {result1}")  # Expected output: 6
    
    # Example 2
    nums2 = [1]
    result2 = solution.max_sub_array(nums2)
    print(f"Example 2: {result2}")  # Expected output: 1
    
    # Example 3
    nums3 = [5, 4, -1, 7, 8]
    result3 = solution.max_sub_array(nums3)
    print(f"Example 3: {result3}")  # Expected output: 23
    
    # Compare with divide and conquer approach
    print("\nUsing divide and conquer approach:")
    print(f"Example 1: {solution.max_sub_array_divide_conquer(nums1)}")
    print(f"Example 3: {solution.max_sub_array_divide_conquer(nums3)}")
