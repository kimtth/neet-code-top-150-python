from typing import List

"""
LeetCode Set Matrix Zeroes

Problem from LeetCode: https://leetcode.com/problems/set-matrix-zeroes/

Description:
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

class Solution:
    def set_zeroes(self, matrix: List[List[int]]) -> None:
        """
        Set entire row and column to 0 for each 0 element in the matrix.
        Modifies the matrix in-place with O(1) extra space.
        
        Args:
            matrix: m x n integer matrix
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # Use first row and first column as markers
        first_row_has_zero = False
        first_col_has_zero = False
        
        # Check if first row has any zeroes
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        # Check if first column has any zeroes
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        # Use first row and column as markers for zeroes in other cells
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the row
                    matrix[0][j] = 0  # Mark the column
        
        # Zero out marked rows (except first row)
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        # Zero out marked columns (except first column)
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # Zero out first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
    
    def set_zeroes_using_sets(self, matrix: List[List[int]]) -> None:
        """
        Alternative implementation using sets to track rows and columns.
        Uses O(m+n) extra space but easier to understand.
        
        Args:
            matrix: m x n integer matrix
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # Track which rows and columns need to be zeroed
        zero_rows = set()
        zero_cols = set()
        
        # Find all zeroes in the matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        # Zero out marked rows
        for row in zero_rows:
            for j in range(n):
                matrix[row][j] = 0
        
        # Zero out marked columns
        for col in zero_cols:
            for i in range(m):
                matrix[i][col] = 0

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(f"Original matrix 1:")
    for row in matrix1:
        print(row)
    
    solution.set_zeroes(matrix1)
    print(f"\nAfter setting zeroes:")
    for row in matrix1:
        print(row)
    # Expected output: [[1,0,1],[0,0,0],[1,0,1]]
    
    # Example 2
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print(f"\nOriginal matrix 2:")
    for row in matrix2:
        print(row)
    
    solution.set_zeroes(matrix2)
    print(f"\nAfter setting zeroes:")
    for row in matrix2:
        print(row)
    # Expected output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    
    # Test alternative approach with a new matrix
    matrix3 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution.set_zeroes_using_sets(matrix3)
    print(f"\nUsing sets approach:")
    for row in matrix3:
        print(row)
    # Expected output: [[1,0,1],[0,0,0],[1,0,1]]
