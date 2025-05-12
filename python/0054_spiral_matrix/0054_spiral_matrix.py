from typing import List

"""
LeetCode Spiral Matrix

Problem from LeetCode: https://leetcode.com/problems/spiral-matrix/

Description:
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        """
        Traverse the matrix in spiral order.
        
        Args:
            matrix: m x n matrix of integers
            
        Returns:
            List[int]: Elements of the matrix in spiral order
        """
        if not matrix:
            return []
        
        result = []
        m, n = len(matrix), len(matrix[0])
        
        # Define the boundaries
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right:
            # Traverse right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            
            # Traverse down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # Traverse left (if there are rows left)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            
            # Traverse up (if there are columns left)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result
    
    def spiral_order_direction(self, matrix: List[List[int]]) -> List[int]:
        """
        Alternative implementation using direction changes.
        
        Args:
            matrix: m x n matrix of integers
            
        Returns:
            List[int]: Elements of the matrix in spiral order
        """
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        result = []
        
        # Direction vectors: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0
        
        # Starting position
        row, col = 0, 0
        
        # Matrix to track visited cells
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        for _ in range(m * n):
            result.append(matrix[row][col])
            visited[row][col] = True
            
            # Calculate next position
            next_row = row + directions[direction_idx][0]
            next_col = col + directions[direction_idx][1]
            
            # Check if we need to change direction
            if (next_row < 0 or next_row >= m or 
                next_col < 0 or next_col >= n or 
                visited[next_row][next_col]):
                # Change direction
                direction_idx = (direction_idx + 1) % 4
                next_row = row + directions[direction_idx][0]
                next_col = col + directions[direction_idx][1]
            
            row, col = next_row, next_col
        
        return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = solution.spiral_order(matrix1)
    print(f"Example 1: {result1}")  # Expected output: [1,2,3,6,9,8,7,4,5]
    
    # Example 2
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result2 = solution.spiral_order(matrix2)
    print(f"Example 2: {result2}")  # Expected output: [1,2,3,4,8,12,11,10,9,5,6,7]
    
    # Compare with direction-based approach
    print("\nUsing direction-based approach:")
    print(f"Example 1: {solution.spiral_order_direction(matrix1)}")
    print(f"Example 2: {solution.spiral_order_direction(matrix2)}")
