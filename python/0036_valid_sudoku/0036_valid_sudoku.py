from typing import List

"""
LeetCode Valid Sudoku

Problem from LeetCode: https://leetcode.com/problems/valid-sudoku/

Description:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""

class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9 x 9 Sudoku board is valid.
        
        Args:
            board: 9x9 Sudoku board
            
        Returns:
            bool: True if the board is valid, False otherwise
        """
        n = 9
        
        # Initialize sets to keep track of numbers in each row, column, and box
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                # Skip empty cells
                if board[r][c] == '.':
                    continue
                    
                val = board[r][c]
                
                # Check if the value is already in the current row
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # Check if the value is already in the current column
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # Check if the value is already in the current 3x3 box
                # Calculate box index (0-8) from row and column
                box_idx = (r // 3) * 3 + (c // 3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)
                
        return True
    
    def is_valid_sudoku_one_pass(self, board: List[List[str]]) -> bool:
        """
        Alternative implementation checking all conditions in a single pass.
        
        Args:
            board: 9x9 Sudoku board
            
        Returns:
            bool: True if the board is valid, False otherwise
        """
        # Use dictionaries with tuples as keys to track seen numbers
        seen = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = board[i][j]
                    # Try to add all three types of entries at once
                    row_entry = (i, 'r', val)
                    col_entry = (j, 'c', val)
                    box_entry = (i//3, j//3, 'b', val)
                    
                    if row_entry in seen or col_entry in seen or box_entry in seen:
                        return False
                    
                    seen.add(row_entry)
                    seen.add(col_entry)
                    seen.add(box_entry)
                    
        return True

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: Valid Sudoku
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    result1 = solution.is_valid_sudoku(board1)
    print(f"Example 1: {result1}")  # Expected output: True
    
    # Example 2: Invalid Sudoku
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    result2 = solution.is_valid_sudoku(board2)
    print(f"Example 2: {result2}")  # Expected output: False
    
    # Compare with one-pass approach
    print("\nUsing one-pass approach:")
    print(f"Example 1: {solution.is_valid_sudoku_one_pass(board1)}")  # Expected output: True
    print(f"Example 2: {solution.is_valid_sudoku_one_pass(board2)}")  # Expected output: False
