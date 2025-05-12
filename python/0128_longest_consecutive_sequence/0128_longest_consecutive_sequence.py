from typing import List

"""
LeetCode Longest Consecutive Sequence

Problem from LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/

Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        """
        Find the length of the longest consecutive sequence.
        Uses a hash set to achieve O(n) time complexity.
        
        Args:
            nums: Unsorted array of integers
            
        Returns:
            int: Length of longest consecutive sequence
        """
        if not nums:
            return 0
            
        # Convert the list to a set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Only check sequences starting from the smallest number in the sequence
            # Skip if there's already a smaller number before the current number
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                # Update the longest streak
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak
    
    def longest_consecutive_union_find(self, nums: List[int]) -> int:
        """
        Find the longest consecutive sequence using Union-Find.
        
        Args:
            nums: Unsorted array of integers
            
        Returns:
            int: Length of longest consecutive sequence
        """
        if not nums:
            return 0
            
        # Create parent dictionary for Union-Find
        parent = {}
        size = {}
        
        # Initialize parent and size for each number
        for num in nums:
            parent[num] = num
            size[num] = 1
            
        # Find function for Union-Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        # Union function
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x != root_y:
                # Make the larger root the parent of the smaller root
                if size[root_x] < size[root_y]:
                    parent[root_x] = root_y
                    size[root_y] += size[root_x]
                else:
                    parent[root_y] = root_x
                    size[root_x] += size[root_y]
                    
        # Union consecutive numbers
        num_set = set(nums)
        for num in num_set:
            if num + 1 in num_set:
                union(num, num + 1)
                
        # Find the maximum size
        max_size = 0
        for num in num_set:
            if parent[num] == num:  # Only consider roots
                max_size = max(max_size, size[num])
                
        return max_size

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [100, 4, 200, 1, 3, 2]
    result1 = solution.longest_consecutive(nums1)
    print(f"Example 1: nums={nums1}, result={result1}")  # Expected output: 4
    
    # Example 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result2 = solution.longest_consecutive(nums2)
    print(f"Example 2: nums={nums2}, result={result2}")  # Expected output: 9
    
    # Edge case
    nums3 = []
    result3 = solution.longest_consecutive(nums3)
    print(f"Edge case: nums={nums3}, result={result3}")  # Expected output: 0
    
    # Compare with Union-Find approach
    print("\nUsing Union-Find approach:")
    print(f"Example 1: {solution.longest_consecutive_union_find(nums1)}")
    print(f"Example 2: {solution.longest_consecutive_union_find(nums2)}")
