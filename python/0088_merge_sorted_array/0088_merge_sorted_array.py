from typing import List

"""
LeetCode Merge Sorted Array

Problem from LeetCode: https://leetcode.com/problems/merge-sorted-array/

Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums1 and nums2 into a single sorted array in-place.
        Fills nums1 with the result of the merge.
        
        Args:
            nums1: First sorted array with extra space at the end
            m: Number of elements in nums1
            nums2: Second sorted array
            n: Number of elements in nums2
        """
        # Start from the end of both arrays
        i, j, k = m - 1, n - 1, m + n - 1
        
        # While there are elements in both arrays
        while i >= 0 and j >= 0:
            # Place the larger element at the end of nums1
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            
        # If there are remaining elements in nums2, add them to nums1
        # (No need to check nums1 as those elements are already in place)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
    
    def merge_pythonic(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        A more pythonic solution using slicing.
        
        Args:
            nums1: First sorted array with extra space at the end
            m: Number of elements in nums1
            nums2: Second sorted array
            n: Number of elements in nums2
        """
        # Replace the trailing zeros in nums1 with nums2 elements
        nums1[m:] = nums2[:n]
        
        # Sort the entire array
        nums1.sort()
    
    def merge_two_pointers(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Alternative approach using two pointers from the beginning of each array.
        Uses a temporary array to store results, then copies back to nums1.
        
        Args:
            nums1: First sorted array with extra space at the end
            m: Number of elements in nums1
            nums2: Second sorted array
            n: Number of elements in nums2
        """
        # Create a copy of the first m elements of nums1
        nums1_copy = nums1[:m]
        
        # Pointers for nums1_copy and nums2
        p1, p2 = 0, 0
        
        # Merge elements back into nums1
        for p in range(m + n):
            # If we've exhausted nums1_copy or if nums2 element is smaller
            if p1 >= m or (p2 < n and nums2[p2] < nums1_copy[p1]):
                nums1[p] = nums2[p2]
                p2 += 1
            else:
                nums1[p] = nums1_copy[p1]
                p1 += 1

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1_1 = [1, 2, 3, 0, 0, 0]
    m1 = 3
    nums2_1 = [2, 5, 6]
    n1 = 3
    solution.merge(nums1_1, m1, nums2_1, n1)
    print(f"Example 1: {nums1_1}")  # Expected output: [1, 2, 2, 3, 5, 6]
    
    # Example 2
    nums1_2 = [1]
    m2 = 1
    nums2_2 = []
    n2 = 0
    solution.merge(nums1_2, m2, nums2_2, n2)
    print(f"Example 2: {nums1_2}")  # Expected output: [1]
    
    # Example 3
    nums1_3 = [0]
    m3 = 0
    nums2_3 = [1]
    n3 = 1
    solution.merge(nums1_3, m3, nums2_3, n3)
    print(f"Example 3: {nums1_3}")  # Expected output: [1]
    
    # Compare with other implementations
    nums1_4 = [1, 2, 3, 0, 0, 0]
    solution.merge_pythonic(nums1_4, 3, [2, 5, 6], 3)
    print(f"\nPythonic approach: {nums1_4}")  # Expected output: [1, 2, 2, 3, 5, 6]
    
    nums1_5 = [1, 2, 3, 0, 0, 0]
    solution.merge_two_pointers(nums1_5, 3, [2, 5, 6], 3)
    print(f"Two-pointers approach: {nums1_5}")  # Expected output: [1, 2, 2, 3, 5, 6]
