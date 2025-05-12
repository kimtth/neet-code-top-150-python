from typing import List
import bisect


"""
LeetCode Longest Increasing Subsequence (Part 2)

Problem from LeetCode: https://leetcode.com/problems/longest-increasing-subsequence/

Description:
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

This implementation focuses on the O(n log n) binary search solution to the problem.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.

Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
"""

class Solution:

    def length_of_l_i_s(self, nums: List[int]) ->int:
        """
        Find the length of the longest strictly increasing subsequence using binary search approach.
        
        This implementation uses the patience sort technique with O(n log n) time complexity.
        
        Args:
            nums: Array of integers
            
        Returns:
            int: Length of the longest increasing subsequence
        """
        if not nums:
            return 0
        sub = [nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            if num > sub[-1]:
                sub.append(num)
            else:
                j = self.binary_search(sub, num)
                sub[j] = num
        return len(sub)

    def binary_search(self, sub: List[int], num: int) ->int:
        """
        Binary search to find the position where num should be placed in sub.
        
        Args:
            sub: Current subsequence
            num: Number to place
            
        Returns:
            int: Index where num should be placed
        """
        left = 0
        right = len(sub) - 1
        while left < right:
            mid = (left + right) // 2
            if sub[mid] == num:
                return mid
            if sub[mid] < num:
                left = mid + 1
            else:
                right = mid
        return left

    def length_of_l_i_s_with_bisect(self, nums: List[int]) ->int:
        """
        Find the length of the longest strictly increasing subsequence using bisect.
        
        Args:
            nums: Array of integers
            
        Returns:
            int: Length of the longest increasing subsequence
        """
        sub = []
        for num in nums:
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    result1 = solution.length_of_l_i_s(nums1)
    print(f"Example 1: {result1}")  # Expected output: 4
    
    # Example 2
    nums2 = [0, 1, 0, 3, 2, 3]
    result2 = solution.length_of_l_i_s(nums2)
    print(f"Example 2: {result2}")  # Expected output: 4
    
    # Example 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    result3 = solution.length_of_l_i_s(nums3)
    print(f"Example 3: {result3}")  # Expected output: 1
    
    # Using bisect implementation
    print("\nUsing bisect implementation:")
    result4 = solution.length_of_l_i_s_with_bisect(nums1)
    print(f"Example 1: {result4}")  # Expected output: 4
