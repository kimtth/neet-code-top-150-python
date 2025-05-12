from typing import List

"""
LeetCode Median of Two Sorted Arrays

Problem from LeetCode: https://leetcode.com/problems/median-of-two-sorted-arrays/

Description:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

class Solution:
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays in O(log(m+n)) time.
        
        Args:
            nums1: First sorted array
            nums2: Second sorted array
            
        Returns:
            float: Median of the combined arrays
        """
        # Ensure nums1 is the smaller array for simplicity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            partition_x = (low + high) // 2
            partition_y = (x + y + 1) // 2 - partition_x
            
            # If partition_x is 0, it means there is nothing on the left side of nums1
            max_x_left = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            # If partition_x is x, it means there is nothing on the right side of nums1
            min_x_right = float('inf') if partition_x == x else nums1[partition_x]
            
            # Similar for nums2
            max_y_left = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_y_right = float('inf') if partition_y == y else nums2[partition_y]
            
            if max_x_left <= min_y_right and max_y_left <= min_x_right:
                # Found the correct partition
                # If the combined length is odd
                if (x + y) % 2 != 0:
                    return max(max_x_left, max_y_left)
                # If the combined length is even
                else:
                    return (max(max_x_left, max_y_left) + min(min_x_right, min_y_right)) / 2
            elif max_x_left > min_y_right:
                # Move partition_x to the left
                high = partition_x - 1
            else:
                # Move partition_x to the right
                low = partition_x + 1
                
        raise ValueError("Input arrays are not sorted.")

    def find_median_sorted_arrays_naive(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays using a simpler approach.
        Time complexity: O(m+n), not optimal but easier to understand.
        
        Args:
            nums1: First sorted array
            nums2: Second sorted array
            
        Returns:
            float: Median of the combined arrays
        """
        merged = []
        i, j = 0, 0
        
        # Merge the two arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
                
        # Add remaining elements
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        # Find median
        n = len(merged)
        if n % 2 == 0:
            return (merged[n//2 - 1] + merged[n//2]) / 2
        else:
            return merged[n//2]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1_1 = [1, 3]
    nums2_1 = [2]
    result1 = solution.find_median_sorted_arrays(nums1_1, nums2_1)
    print(f"Example 1: {result1}")  # Expected output: 2.0
    
    # Example 2
    nums1_2 = [1, 2]
    nums2_2 = [3, 4]
    result2 = solution.find_median_sorted_arrays(nums1_2, nums2_2)
    print(f"Example 2: {result2}")  # Expected output: 2.5
    
    # Compare with naive approach
    print("\nUsing naive approach:")
    result1_naive = solution.find_median_sorted_arrays_naive(nums1_1, nums2_1)
    print(f"Example 1: {result1_naive}")
    result2_naive = solution.find_median_sorted_arrays_naive(nums1_2, nums2_2)
    print(f"Example 2: {result2_naive}")
