from typing import List

"""
LeetCode Largest Rectangle in Histogram

Problem from LeetCode: https://leetcode.com/problems/largest-rectangle-in-histogram/

Description:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
"""

class Solution:
    def largest_rectangle_area(self, heights: List[int]) -> int:
        """
        Find the area of the largest rectangle in the histogram.
        Uses a stack-based approach with O(n) time complexity.
        
        Args:
            heights: Array of integers representing histogram bar heights
            
        Returns:
            int: Area of the largest rectangle
        """
        # Use a stack to track positions of increasing heights
        stack = []
        max_area = 0
        n = len(heights)
        
        # Process all bars of the histogram
        for i, h in enumerate(heights):
            # If current bar is lower than the bars in stack, 
            # calculate area for each bar in stack until we find a lower bar
            while stack and heights[stack[-1]] > h:
                # Pop the last element from stack
                height = heights[stack.pop()]
                
                # Calculate width of the rectangle with height 'height'
                # Width is the distance from current position to the previous element in stack
                # If stack is empty, then width is just the current position
                width = i if not stack else i - stack[-1] - 1
                
                # Update max area
                max_area = max(max_area, height * width)
            
            # Push current position to stack
            stack.append(i)
        
        # Process the remaining elements in stack
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)
            
        return max_area
    
    def largest_rectangle_area_optimized(self, heights: List[int]) -> int:
        """
        Optimized implementation with cleaner code.
        Add sentinel values at start and end to simplify edge cases.
        
        Args:
            heights: Array of integers representing histogram bar heights
            
        Returns:
            int: Area of the largest rectangle
        """
        # Add sentinel values to avoid edge cases
        heights = [0] + heights + [0]
        n = len(heights)
        stack = [0]  # Start with sentinel index
        max_area = 0
        
        for i in range(1, n):
            # While current height is less than height at top of stack
            while heights[i] < heights[stack[-1]]:
                # Calculate area for the bar at the top of stack
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            
            # Push current index to stack
            stack.append(i)
            
        return max_area

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    heights1 = [2, 1, 5, 6, 2, 3]
    result1 = solution.largest_rectangle_area(heights1)
    print(f"Example 1: {result1}")  # Expected output: 10
    
    # Example 2
    heights2 = [2, 4]
    result2 = solution.largest_rectangle_area(heights2)
    print(f"Example 2: {result2}")  # Expected output: 4
    
    # Additional example
    heights3 = [1, 2, 3, 4, 5]
    result3 = solution.largest_rectangle_area(heights3)
    print(f"Example 3: {result3}")  # Expected output: 9
    
    # Compare with optimized approach
    print("\nUsing optimized approach:")
    print(f"Example 1: {solution.largest_rectangle_area_optimized(heights1)}")  # Expected output: 10
    print(f"Example 2: {solution.largest_rectangle_area_optimized(heights2)}")  # Expected output: 4
    print(f"Example 3: {solution.largest_rectangle_area_optimized(heights3)}")  # Expected output: 9
