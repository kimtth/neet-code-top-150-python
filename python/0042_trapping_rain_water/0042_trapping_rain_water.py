from typing import List

"""
LeetCode Trapping Rain Water

Problem from LeetCode: https://leetcode.com/problems/trapping-rain-water/

Description:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate how much water can be trapped after raining.
        Uses a two-pointer approach for O(n) time and O(1) space complexity.
        
        Args:
            height: Array of non-negative integers representing heights
            
        Returns:
            int: Total amount of trapped water
        """
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]
        trapped_water = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                trapped_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                trapped_water += right_max - height[right]
                
        return trapped_water
    
    def trap_using_arrays(self, height: List[int]) -> int:
        """
        Calculate trapped water using pre-computed arrays.
        Uses O(n) time and O(n) space complexity.
        
        Args:
            height: Array of non-negative integers representing heights
            
        Returns:
            int: Total amount of trapped water
        """
        if not height:
            return 0
            
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        # Fill left_max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
            
        # Fill right_max array
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
            
        # Calculate trapped water
        trapped_water = 0
        for i in range(n):
            trapped_water += min(left_max[i], right_max[i]) - height[i]
            
        return trapped_water
    
    def trap_stack(self, height: List[int]) -> int:
        """
        Calculate trapped water using a stack approach.
        
        Args:
            height: Array of non-negative integers representing heights
            
        Returns:
            int: Total amount of trapped water
        """
        stack = []
        trapped_water = 0
        
        for current in range(len(height)):
            # While the current bar is higher than the stack top
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                
                if not stack:
                    break
                
                # Calculate width and height of the trap
                width = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                
                # Add water for this trap
                trapped_water += width * bounded_height
                
            stack.append(current)
            
        return trapped_water

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result1 = solution.trap(height1)
    print(f"Example 1: {result1}")  # Expected output: 6
    
    # Example 2
    height2 = [4, 2, 0, 3, 2, 5]
    result2 = solution.trap(height2)
    print(f"Example 2: {result2}")  # Expected output: 9
    
    # Compare with other implementations
    print("\nUsing arrays implementation:")
    print(f"Example 1: {solution.trap_using_arrays(height1)}")  # Expected output: 6
    print(f"Example 2: {solution.trap_using_arrays(height2)}")  # Expected output: 9
    
    print("\nUsing stack implementation:")
    print(f"Example 1: {solution.trap_stack(height1)}")  # Expected output: 6
    print(f"Example 2: {solution.trap_stack(height2)}")  # Expected output: 9
