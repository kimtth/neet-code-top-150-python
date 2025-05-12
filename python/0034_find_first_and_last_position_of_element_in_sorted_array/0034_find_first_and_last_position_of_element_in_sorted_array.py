from typing import List

"""
LeetCode Find First and Last Position of Element in Sorted Array

Problem from LeetCode: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Description:
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""

class Solution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        """
        Find the starting and ending position of a target value in a sorted array.
        Uses two binary searches to find the leftmost and rightmost occurrences.
        
        Args:
            nums: Sorted array of integers
            target: Target value to search for
            
        Returns:
            List[int]: [starting position, ending position], or [-1, -1] if not found
        """
        # Find the leftmost position
        left_idx = self._binary_search_leftmost(nums, target)
        
        # If target is not found, return [-1, -1]
        if left_idx == -1:
            return [-1, -1]
            
        # Find the rightmost position
        right_idx = self._binary_search_rightmost(nums, target)
        
        return [left_idx, right_idx]
    
    def _binary_search_leftmost(self, nums: List[int], target: int) -> int:
        """Helper function to find the leftmost occurrence of target."""
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid
                right = mid - 1  # Continue searching to the left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return result
    
    def _binary_search_rightmost(self, nums: List[int], target: int) -> int:
        """Helper function to find the rightmost occurrence of target."""
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid
                left = mid + 1  # Continue searching to the right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return result
    
    def search_range_simplified(self, nums: List[int], target: int) -> List[int]:
        """
        Alternative implementation using a common binary search function.
        
        Args:
            nums: Sorted array of integers
            target: Target value to search for
            
        Returns:
            List[int]: [starting position, ending position], or [-1, -1] if not found
        """
        def binary_search(nums, target, find_left):
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    result = mid
                    if find_left:
                        right = mid - 1  # Find leftmost
                    else:
                        left = mid + 1  # Find rightmost
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return result
        
        left_idx = binary_search(nums, target, True)
        
        if left_idx == -1:
            return [-1, -1]
            
        right_idx = binary_search(nums, target, False)
        
        return [left_idx, right_idx]

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    result1 = solution.search_range(nums1, target1)
    print(f"Example 1: nums={nums1}, target={target1}, result={result1}")  # Expected output: [3, 4]
    
    # Example 2
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    result2 = solution.search_range(nums2, target2)
    print(f"Example 2: nums={nums2}, target={target2}, result={result2}")  # Expected output: [-1, -1]
    
    # Example 3
    nums3 = []
    target3 = 0
    result3 = solution.search_range(nums3, target3)
    print(f"Example 3: nums={nums3}, target={target3}, result={result3}")  # Expected output: [-1, -1]
    
    # Additional example with repeated elements
    nums4 = [1, 1, 1, 1, 1, 1]
    target4 = 1
    result4 = solution.search_range(nums4, target4)
    print(f"Example 4: nums={nums4}, target={target4}, result={result4}")  # Expected output: [0, 5]
    
    # Compare with simplified implementation
    print("\nUsing simplified implementation:")
    print(f"Example 1: {solution.search_range_simplified(nums1, target1)}")  # Expected output: [3, 4]
    print(f"Example 2: {solution.search_range_simplified(nums2, target2)}")  # Expected output: [-1, -1]
