from typing import List

"""
LeetCode First Missing Positive

Problem from LeetCode: https://leetcode.com/problems/first-missing-positive/

Description:
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
"""

class Solution:
    def first_missing_positive(self, nums: List[int]) -> int:
        """
        Find the smallest missing positive integer in an unsorted array.
        Uses O(n) time and O(1) extra space by modifying the array in-place.
        
        Args:
            nums: Unsorted array of integers
            
        Returns:
            int: Smallest missing positive integer
        """
        n = len(nums)
        
        # Step 1: Ensure 1 is present in the array
        contains_one = False
        for num in nums:
            if num == 1:
                contains_one = True
                break
                
        if not contains_one:
            return 1
            
        # Step 2: Replace non-positive numbers and numbers greater than n with 1
        # This simplifies the problem to finding the first missing in range [1, n+1]
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
                
        # Step 3: Use the array itself as a hash table
        # Mark presence of values by negating the value at corresponding index
        for i in range(n):
            num = abs(nums[i])
            # If num is in range [1, n]
            if num <= n:
                # Make nums[num-1] negative to mark num as present
                # Use abs() in case it's already negative
                nums[num - 1] = -abs(nums[num - 1])
                
        # Step 4: Find the first positive value in the array
        # Its index + 1 will be the first missing positive
        for i in range(n):
            if nums[i] > 0:
                return i + 1
                
        # If all values in range [1, n] are present, return n+1
        return n + 1
    
    def first_missing_positive_cyclic_sort(self, nums: List[int]) -> int:
        """
        Find the smallest missing positive integer using cyclic sort.
        Places each number in its correct position, then finds the first mismatch.
        
        Args:
            nums: Unsorted array of integers
            
        Returns:
            int: Smallest missing positive integer
        """
        n = len(nums)
        
        # Place each number in its correct position
        # nums[i] should be at position nums[i] - 1 if 1 <= nums[i] <= n
        i = 0
        while i < n:
            correct_pos = nums[i] - 1
            # If the number is positive, in range, and not already in correct position
            if 0 < nums[i] <= n and nums[i] != nums[correct_pos]:
                # Swap to place it in the correct position
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
                
        # Find the first position where the number doesn't match its index + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If all positions are filled correctly, the answer is n+1
        return n + 1

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [1, 2, 0]
    result1 = solution.first_missing_positive(nums1.copy())  # Use copy to preserve original for comparison
    print(f"Example 1: nums={nums1}, result={result1}")  # Expected output: 3
    
    # Example 2
    nums2 = [3, 4, -1, 1]
    result2 = solution.first_missing_positive(nums2.copy())
    print(f"Example 2: nums={nums2}, result={result2}")  # Expected output: 2
    
    # Example 3
    nums3 = [7, 8, 9, 11, 12]
    result3 = solution.first_missing_positive(nums3.copy())
    print(f"Example 3: nums={nums3}, result={result3}")  # Expected output: 1
    
    # Compare with cyclic sort approach
    print("\nUsing cyclic sort approach:")
    print(f"Example 1: {solution.first_missing_positive_cyclic_sort(nums1.copy())}")
    print(f"Example 2: {solution.first_missing_positive_cyclic_sort(nums2.copy())}")
    print(f"Example 3: {solution.first_missing_positive_cyclic_sort(nums3.copy())}")
