from typing import List

"""
LeetCode Search a 2D Matrix

Problem from LeetCode: https://leetcode.com/problems/search-a-2d-matrix/

Description:
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

class Solution:
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Search for a target value in a sorted 2D matrix.
        Uses a single binary search treating the matrix as a 1D array.
        
        Args:
            matrix: m x n sorted matrix
            target: Value to search for
            
        Returns:
            bool: True if target is in the matrix, False otherwise
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        # Treat the matrix as a 1D sorted array
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Convert 1D index to 2D coordinates
            row, col = mid // n, mid % n
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
    
    def search_matrix_two_binary_searches(self, matrix: List[List[int]], target: int) -> bool:
        """
        Search using two binary searches: first for the row, then for the column.
        
        Args:
            matrix: m x n sorted matrix
            target: Value to search for
            
        Returns:
            bool: True if target is in the matrix, False otherwise
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        # First binary search to find the potential row
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                # Target could be in this row, search it
                return self._binary_search_row(matrix[mid], target)
            elif matrix[mid][0] > target:
                right = mid - 1
            else:  # matrix[mid][n-1] < target
                left = mid + 1
        
        return False
    
    def _binary_search_row(self, row: List[int], target: int) -> bool:
        """Helper function for binary search in a row."""
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target1 = 3
    result1 = solution.search_matrix(matrix1, target1)
    print(f"Example 1: target={target1}, result={result1}")  # Expected: True
    
    # Example 2
    matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target2 = 13
    result2 = solution.search_matrix(matrix2, target2)
    print(f"Example 2: target={target2}, result={result2}")  # Expected: False
    
    # Additional example
    matrix3 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target3 = 60
    result3 = solution.search_matrix(matrix3, target3)
    print(f"Example 3: target={target3}, result={result3}")  # Expected: True
    
    # Compare with two binary searches approach
    print("\nUsing two binary searches approach:")
    print(f"Example 1: {solution.search_matrix_two_binary_searches(matrix1, target1)}")  # Expected: True
    print(f"Example 2: {solution.search_matrix_two_binary_searches(matrix2, target2)}")  # Expected: False
