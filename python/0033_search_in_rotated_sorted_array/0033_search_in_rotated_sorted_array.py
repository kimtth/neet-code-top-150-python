from typing import List

"""
LeetCode Search in Rotated Sorted Array

Problem from LeetCode: https://leetcode.com/problems/search-in-rotated-sorted-array/

Description:
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Search for a target in a rotated sorted array.
        Uses modified binary search to achieve O(log n) time complexity.
        
        Args:
            nums: Rotated sorted array
            target: Target value to search for
            
        Returns:
            int: Index of target if found, -1 otherwise
        """
        if not nums:
            return -1
            
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target is in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                # Check if target is in the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1
    
    def search_with_pivot(self, nums: List[int], target: int) -> int:
        """
        Alternative approach: First find the pivot, then perform binary search.
        Still maintains O(log n) time complexity.
        
        Args:
            nums: Rotated sorted array
            target: Target value to search for
            
        Returns:
            int: Index of target if found, -1 otherwise
        """
        if not nums:
            return -1
            
        # Find the pivot (smallest element)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        # Pivot index
        pivot = left
        
        # Perform binary search on the correct portion
        left, right = 0, len(nums) - 1
        
        # Determine which half to search
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1
            
        # Standard binary search
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    result1 = solution.search(nums1, target1)
    print(f"Example 1: nums={nums1}, target={target1}, result={result1}")  # Expected output: 4
    
    # Example 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    result2 = solution.search(nums2, target2)
    print(f"Example 2: nums={nums2}, target={target2}, result={result2}")  # Expected output: -1
    
    # Example 3
    nums3 = [1]
    target3 = 0
    result3 = solution.search(nums3, target3)
    print(f"Example 3: nums={nums3}, target={target3}, result={result3}")  # Expected output: -1
    
    # Additional example
    nums4 = [3, 1]
    target4 = 1
    result4 = solution.search(nums4, target4)
    print(f"Example 4: nums={nums4}, target={target4}, result={result4}")  # Expected output: 1
    
    # Compare with the pivot-finding approach
    print("\nUsing pivot-finding approach:")
    print(f"Example 1: {solution.search_with_pivot(nums1, target1)}")  # Expected output: 4
    print(f"Example 2: {solution.search_with_pivot(nums2, target2)}")  # Expected output: -1
