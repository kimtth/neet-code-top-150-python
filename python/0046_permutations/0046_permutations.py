from typing import List

"""
LeetCode Permutations

Problem from LeetCode: https://leetcode.com/problems/permutations/

Description:
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible permutations of an array of distinct integers.
        Uses backtracking approach.
        
        Args:
            nums: Array of distinct integers
            
        Returns:
            List[List[int]]: All possible permutations
        """
        result = []
        self._backtrack(nums, [], result)
        return result
    
    def _backtrack(self, nums: List[int], path: List[int], result: List[List[int]]) -> None:
        """
        Helper function for backtracking.
        
        Args:
            nums: Remaining integers to permute
            path: Current permutation being built
            result: List to collect all permutations
        """
        # If no numbers left, we've completed a permutation
        if not nums:
            result.append(path)
            return
            
        for i in range(len(nums)):
            # Choose the current number and recurse
            self._backtrack(nums[:i] + nums[i+1:], path + [nums[i]], result)
    
    def permute_iterative(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all permutations using an iterative approach.
        
        Args:
            nums: Array of distinct integers
            
        Returns:
            List[List[int]]: All possible permutations
        """
        # Start with an empty permutation
        result = [[]]
        
        for num in nums:
            new_perms = []
            for perm in result:
                # Insert the current number at each possible position
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [num] + perm[i:])
            result = new_perms
            
        return result
    
    def permute_swap(self, nums: List[int]) -> List[List[int]]:
        """
        Generate permutations by swapping elements in-place.
        
        Args:
            nums: Array of distinct integers
            
        Returns:
            List[List[int]]: All possible permutations
        """
        result = []
        
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])  # Make a copy of the current state
                return
                
            for i in range(start, len(nums)):
                # Swap elements
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse on the next position
                backtrack(start + 1)
                # Backtrack (undo the swap)
                nums[start], nums[i] = nums[i], nums[start]
                
        backtrack(0)
        return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [1, 2, 3]
    result1 = solution.permute(nums1)
    print(f"Example 1: {result1}")
    # Expected output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    
    # Example 2
    nums2 = [0, 1]
    result2 = solution.permute(nums2)
    print(f"Example 2: {result2}")
    # Expected output: [[0,1],[1,0]]
    
    # Example 3
    nums3 = [1]
    result3 = solution.permute(nums3)
    print(f"Example 3: {result3}")
    # Expected output: [[1]]
    
    # Compare with other implementations
    print("\nUsing iterative approach:")
    print(f"Example 1: {solution.permute_iterative(nums1)}")
    
    print("\nUsing swap approach:")
    print(f"Example 1: {solution.permute_swap(nums1)}")
