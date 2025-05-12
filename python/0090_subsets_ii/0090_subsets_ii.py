from typing import List

"""
LeetCode Subsets II

Problem from LeetCode: https://leetcode.com/problems/subsets-ii/

Description:
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique subsets of an array that may contain duplicates.
        
        Args:
            nums: Array of integers (may contain duplicates)
            
        Returns:
            List[List[int]]: All unique subsets
        """
        # Sort to handle duplicates correctly
        nums.sort()
        result = []
        self._backtrack(nums, 0, [], result)
        return result
    
    def _backtrack(self, nums: List[int], start: int, path: List[int], result: List[List[int]]) -> None:
        """
        Helper function for backtracking.
        
        Args:
            nums: Sorted array of integers
            start: Starting index for current recursion
            path: Current subset being built
            result: List to collect all unique subsets
        """
        # Add current subset to result
        result.append(path[:])
        
        # Try each number as the next element in the subset
        for i in range(start, len(nums)):
            # Skip duplicates to avoid duplicate subsets
            if i > start and nums[i] == nums[i-1]:
                continue
                
            # Include current number in the subset
            path.append(nums[i])
            self._backtrack(nums, i + 1, path, result)
            path.pop()  # Backtrack
    
    def subsetsWithDup_iterative(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique subsets using an iterative approach.
        
        Args:
            nums: Array of integers (may contain duplicates)
            
        Returns:
            List[List[int]]: All unique subsets
        """
        # Sort to handle duplicates correctly
        nums.sort()
        result = [[]]
        
        # Process each number
        i = 0
        while i < len(nums):
            # Count duplicates
            count = 1
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                count += 1
                
            # Number of existing subsets
            n = len(result)
            
            # For each existing subset, create new subsets by adding the current number 1 to count times
            for j in range(n):
                subset = result[j].copy()
                for k in range(1, count + 1):
                    subset.append(nums[i])
                    result.append(subset.copy())
                    
            i += 1
            
        return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [1, 2, 2]
    result1 = solution.subsetsWithDup(nums1)
    print(f"Example 1: nums={nums1}")
    print(f"Result: {result1}")  # Expected output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
    
    # Example 2
    nums2 = [0]
    result2 = solution.subsetsWithDup(nums2)
    print(f"\nExample 2: nums={nums2}")
    print(f"Result: {result2}")  # Expected output: [[],[0]]
    
    # Additional example
    nums3 = [4, 4, 4, 1, 4]
    result3 = solution.subsetsWithDup(nums3)
    print(f"\nExample 3: nums={nums3}")
    print(f"Result: {result3}")
    
    # Compare with iterative approach
    print("\nUsing iterative approach:")
    print(f"Example 1: {solution.subsetsWithDup_iterative(nums1)}")
