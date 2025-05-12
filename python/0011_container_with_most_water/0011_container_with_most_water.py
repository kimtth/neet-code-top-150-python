from typing import List, Optional

"""
LeetCode Container With Most Water

Problem from LeetCode: https://leetcode.com/problems/container-with-most-water/

Description:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

class Solution:
    def max_area(self, height: List[int]) -> int:
        """
        Find the maximum area (water volume) that can be contained between two vertical lines.
        Uses a two-pointer approach for O(n) time complexity.
        
        Args:
            height: Array of heights representing vertical lines
            
        Returns:
            int: Maximum water area that can be contained
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate width between lines
            width = right - left
            # Use the shorter line as height
            container_height = min(height[left], height[right])
            # Calculate current area
            current_area = width * container_height
            # Update maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointer at the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
    
    def max_area_brute_force(self, height: List[int]) -> int:
        """
        Find the maximum area using a brute force approach.
        Time complexity: O(n²) - less efficient but easier to understand.
        
        Args:
            height: Array of heights representing vertical lines
            
        Returns:
            int: Maximum water area that can be contained
        """
        max_area = 0
        n = len(height)
        
        for i in range(n):
            for j in range(i+1, n):
                # Calculate width and height
                width = j - i
                h = min(height[i], height[j])
                # Update maximum area
                max_area = max(max_area, width * h)
                
        return max_area


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result1 = solution.max_area(height1)
    print(f"Example 1: {result1}")  # Expected output: 49
    
    # Example 2
    height2 = [1, 1]
    result2 = solution.max_area(height2)
    print(f"Example 2: {result2}")  # Expected output: 1
    
    # Additional test case
    height3 = [4, 3, 2, 1, 4]
    result3 = solution.max_area(height3)
    print(f"Additional example: {result3}")  # Expected output: 16
    
    # Compare with brute force (for small inputs)
    small_height = [1, 8, 6, 2, 5]
    optimal = solution.max_area(small_height)
    brute_force = solution.max_area_brute_force(small_height)
    print(f"\nComparison for small input:")
    print(f"Optimal solution: {optimal}")
    print(f"Brute force solution: {brute_force}")
