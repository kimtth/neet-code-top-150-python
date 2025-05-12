from typing import List
import heapq


"""
LeetCode 215: Kth Largest Element in an Array

Problem from LeetCode: https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

class Solution:

    def find_kth_largest(self, nums: List[int], k: int) ->int:
        """
        Find the kth largest element in an unsorted array.
        
        Args:
            nums: Array of integers
            k: Position to find (1-indexed)
            
        Returns:
            int: The kth largest element
        """
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

    def find_kth_largest_sort(self, nums: List[int], k: int) ->int:
        """Alternative method using sorting - O(n log n)."""
        nums.sort(reverse=True)
        return nums[k - 1]

    def find_kth_largest_quick_select(self, nums: List[int], k: int) ->int:
        """
        Alternative method using QuickSelect algorithm - O(n) average, O(n²) worst case.
        Implementation of the Hoare's selection algorithm.
        """
        k = len(nums) - k

        def quick_select(l: int, r: int) ->int:
            """Quick select algorithm partitioning the array and recursively selecting."""
            pivot, ptr = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[ptr], nums[r] = nums[r], nums[ptr]
            if ptr > k:
                return quick_select(l, ptr - 1)
            elif ptr < k:
                return quick_select(ptr + 1, r)
            else:
                return nums[ptr]
        return quick_select(0, len(nums) - 1)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = solution.find_kth_largest(nums, k)
    print(result)  # Output: 5
    
    # Example 2
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    result = solution.find_kth_largest(nums, k)
    print(result)  # Output: 4
