from typing import List

"""
LeetCode Rotate Image

Problem from LeetCode: https://leetcode.com/problems/rotate-image/

Description:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the given matrix by 90 degrees clockwise in-place.
        
        Args:
            matrix: n x n 2D matrix
        """
        n = len(matrix)
        
        # Step 1: Transpose the matrix (swap rows with columns)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
    
    def rotate_layer_by_layer(self, matrix: List[List[int]]) -> None:
        """
        Rotate the matrix by handling each layer (ring) separately.
        
        Args:
            matrix: n x n 2D matrix
        """
        n = len(matrix)
        
        # Handle each layer (ring) of the matrix
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            
            for i in range(first, last):
                offset = i - first
                
                # Save top left
                top = matrix[first][i]
                
                # Move bottom left to top left
                matrix[first][i] = matrix[last - offset][first]
                
                # Move bottom right to bottom left
                matrix[last - offset][first] = matrix[last][last - offset]
                
                # Move top right to bottom right
                matrix[last][last - offset] = matrix[i][last]
                
                # Move top left to top right
                matrix[i][last] = top
    
    def rotate_four_pointers(self, matrix: List[List[int]]) -> None:
        """
        Rotate the matrix using the four-pointers technique.
        
        Args:
            matrix: n x n 2D matrix
        """
        left, right = 0, len(matrix) - 1
        
        while left < right:
            # Loop for each element in the current layer
            for i in range(right - left):
                top, bottom = left, right
                
                # Save top left
                top_left = matrix[top][left + i]
                
                # Move bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]
                
                # Move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                # Move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                # Move top left to top right
                matrix[top + i][right] = top_left
                
            left += 1
            right -= 1

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Original matrix 1: {matrix1}")
    solution.rotate(matrix1)
    print(f"After rotation: {matrix1}")
    # Expected output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    
    # Example 2
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(f"\nOriginal matrix 2: {matrix2}")
    solution.rotate(matrix2)
    print(f"After rotation: {matrix2}")
    # Expected output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    
    # Test the layer-by-layer approach
    matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"\nOriginal matrix 3: {matrix3}")
    solution.rotate_layer_by_layer(matrix3)
    print(f"After layer-by-layer rotation: {matrix3}")
    # Expected output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    
    # Test the four-pointers approach
    matrix4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"\nOriginal matrix 4: {matrix4}")
    solution.rotate_four_pointers(matrix4)
    print(f"After four-pointers rotation: {matrix4}")
    # Expected output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
