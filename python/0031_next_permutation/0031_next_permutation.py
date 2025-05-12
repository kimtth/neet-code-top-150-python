from typing import List

"""
LeetCode Next Permutation

Problem from LeetCode: https://leetcode.com/problems/next-permutation/

Description:
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
"""

class Solution:
    def next_permutation(self, nums: List[int]) -> None:
        """
        Rearrange numbers into the lexicographically next greater permutation.
        Modifies the array in-place.
        
        Args:
            nums: List of integers
        """
        # Step 1: Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i >= 0:
            # Step 2: Find the element just larger than nums[i]
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
                
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the subarray starting at i+1
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    def next_permutation_alternate(self, nums: List[int]) -> None:
        """
        Alternative implementation with more descriptive variable names.
        
        Args:
            nums: List of integers
        """
        n = len(nums)
        
        # Find the first pair of adjacent elements where the left is less than the right
        pivot = n - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
            
        # If no such pair is found, the array is in descending order
        # Reverse the entire array to get the lowest permutation
        if pivot < 0:
            nums.reverse()
            return
            
        # Find the rightmost element greater than the pivot
        swap_index = n - 1
        while nums[swap_index] <= nums[pivot]:
            swap_index -= 1
            
        # Swap the pivot with the found element
        nums[pivot], nums[swap_index] = nums[swap_index], nums[pivot]
        
        # Reverse the subarray to the right of the pivot
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [1, 2, 3]
    solution.next_permutation(nums1)
    print(f"Example 1: {nums1}")  # Expected output: [1, 3, 2]
    
    # Example 2
    nums2 = [3, 2, 1]
    solution.next_permutation(nums2)
    print(f"Example 2: {nums2}")  # Expected output: [1, 2, 3]
    
    # Example 3
    nums3 = [1, 1, 5]
    solution.next_permutation(nums3)
    print(f"Example 3: {nums3}")  # Expected output: [1, 5, 1]
    
    # Additional example
    nums4 = [1, 3, 2]
    solution.next_permutation(nums4)
    print(f"Example 4: {nums4}")  # Expected output: [2, 1, 3]
