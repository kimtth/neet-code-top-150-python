from typing import List, Optional

"""
LeetCode 153. Find Minimum in Rotated Sorted Array

Problem from LeetCode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Description:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results 
in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times.
"""

class Solution:

    def find_min(self, nums: list[int]) ->int:
        left = 0
        right = len(nums) - 1
        ans = nums[0]
        if len(nums) == 1:
            return nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                ans = min(ans, nums[left])
            mid = (left + right) // 2
            ans = min(ans, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return ans


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [3,4,5,1,2]
    result1 = solution.find_min(nums1)
    print(f"Input: nums = {nums1}")
    print(f"Output: {result1}")  # Expected output: 1
    
    # Example 2
    nums2 = [4,5,6,7,0,1,2]
    result2 = solution.find_min(nums2)
    print(f"Input: nums = {nums2}")
    print(f"Output: {result2}")  # Expected output: 0
    
    # Example 3
    nums3 = [11,13,15,17]
    result3 = solution.find_min(nums3)
    print(f"Input: nums = {nums3}")
    print(f"Output: {result3}")  # Expected output: 11
