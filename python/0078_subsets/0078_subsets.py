from typing import List

"""
LeetCode Subsets

Problem from LeetCode: https://leetcode.com/problems/subsets/

Description:
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets of the given array.
        Uses backtracking approach.
        
        Args:
            nums: Array of unique integers
            
        Returns:
            List[List[int]]: All possible subsets (power set)
        """
        result = []
        self._backtrack(nums, 0, [], result)
        return result
    
    def _backtrack(self, nums: List[int], start: int, subset: List[int], result: List[List[int]]) -> None:
        """
        Helper function for backtracking.
        
        Args:
            nums: Original array
            start: Current index to start from
            subset: Current subset being built
            result: List to collect all subsets
        """
        # Add the current subset to the result
        result.append(subset[:])
        
        # Explore further options
        for i in range(start, len(nums)):
            # Include nums[i] in the subset
            subset.append(nums[i])
            # Recursively generate subsets with nums[i] included
            self._backtrack(nums, i + 1, subset, result)
            # Backtrack by removing nums[i]
            subset.pop()
    
    def subsets_iterative(self, nums: List[int]) -> List[List[int]]:
        """
        Generate subsets using an iterative approach.
        
        Args:
            nums: Array of unique integers
            
        Returns:
            List[List[int]]: All possible subsets
        """
        result = [[]]  # Start with empty subset
        
        for num in nums:
            # For each number, add it to all existing subsets to create new subsets
            result.extend([subset + [num] for subset in result])
            
        return result
    
    def subsets_bitwise(self, nums: List[int]) -> List[List[int]]:
        """
        Generate subsets using bitwise approach.
        Uses binary representation of numbers from 0 to 2^n - 1.
        
        Args:
            nums: Array of unique integers
            
        Returns:
            List[List[int]]: All possible subsets
        """
        n = len(nums)
        result = []
        
        # There are 2^n possible subsets
        for i in range(1 << n):  # equivalent to 2^n
            subset = []
            for j in range(n):
                # Check if the jth bit is set in i
                if i & (1 << j):
                    subset.append(nums[j])
            result.append(subset)
            
        return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [1, 2, 3]
    result1 = solution.subsets(nums1)
    print(f"Example 1: nums={nums1}")
    print(f"Result: {result1}")  # Expected: [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
    
    # Example 2
    nums2 = [0]
    result2 = solution.subsets(nums2)
    print(f"\nExample 2: nums={nums2}")
    print(f"Result: {result2}")  # Expected: [[],[0]]
    
    # Compare with iterative approach
    print("\nUsing iterative approach:")
    print(f"Example 1: {solution.subsets_iterative(nums1)}")
    
    # Compare with bitwise approach
    print("\nUsing bitwise approach:")
    print(f"Example 1: {solution.subsets_bitwise(nums1)}")
