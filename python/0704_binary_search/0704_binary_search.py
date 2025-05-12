from typing import List


"""
LeetCode Binary Search

Problem from LeetCode: https://leetcode.com/problems/binary-search/

Description:
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i], target <= 10^4
All the integers in nums are unique.
nums is sorted in ascending order.
"""

class Solution:

    def search(self, nums: List[int], target: int) ->int:
        """
        Binary search implementation to find target in a sorted array.
        
        Args:
            nums: A sorted array of distinct integers
            target: The target value to search for
            
        Returns:
            int: The index of target if found, otherwise -1
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search_recursive(self, nums: List[int], target: int) ->int:
        """
        Recursive binary search implementation.
        
        Args:
            nums: A sorted array of distinct integers
            target: The target value to search for
            
        Returns:
            int: The index of target if found, otherwise -1
        """

        def binary_search(left, right):
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid - 1)
        return binary_search(0, len(nums) - 1)

    def search_bisect(self, nums: List[int], target: int) ->int:
        """
        Binary search using Python's bisect module.
        
        Args:
            nums: A sorted array of distinct integers
            target: The target value to search for
            
        Returns:
            int: The index of target if found, otherwise -1
        """
        import bisect
        index = bisect.bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    result1 = solution.search(nums1, target1)
    print(f"Example 1: {result1}")  # Expected: 4
    
    # Example 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    result2 = solution.search(nums2, target2)
    print(f"Example 2: {result2}")  # Expected: -1
    
    # Test recursive method
    print("\nRecursive method:")
    result3 = solution.search_recursive(nums1, target1)
    print(f"Example 1: {result3}")  # Expected: 4
    
    # Test bisect method
    print("\nBisect method:")
    result4 = solution.search_bisect(nums1, target1)
    print(f"Example 1: {result4}")  # Expected: 4
