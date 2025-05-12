from typing import List


"""
LeetCode Longest Increasing Subsequence

Problem from LeetCode: https://leetcode.com/problems/longest-increasing-subsequence/

Description:
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

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
"""

class Solution:

    def length_of_l_i_s(self, nums: List[int]) ->int:
        """
        Find the length of the longest strictly increasing subsequence.
        
        This implementation uses dynamic programming with O(n²) time complexity.
        
        Args:
            nums: Array of integers
            
        Returns:
            int: Length of the longest increasing subsequence
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        max_length = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            max_length = max(max_length, dp[i])
        return max_length

    def length_of_l_i_s_patience(self, nums: List[int]) ->int:
        """
        Find the length of the longest strictly increasing subsequence.
        
        This implementation uses patience sort technique with O(n log n) time complexity.
        
        Args:
            nums: Array of integers
            
        Returns:
            int: Length of the longest increasing subsequence
        """
        if not nums:
            return 0
        tails = []
        for num in nums:
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num
        return len(tails)

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
    
    # Compare with optimized solution
    print("\nOptimized solution (O(n log n)):")
    result1_opt = solution.length_of_l_i_s_patience(nums1)
    print(f"Example 1: {result1_opt}")  # Expected output: 4
