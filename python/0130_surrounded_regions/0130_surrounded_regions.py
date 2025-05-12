from typing import List, Optional

"""
LeetCode Surrounded Regions

Problem from LeetCode: https://leetcode.com/problems/surrounded-regions/

Description:
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
"""

class Solution:

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][
                    j] == 'O':
                    dfs(i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'


def print_board(board):
    """Helper function to print the board in a readable format"""
    for row in board:
        print(''.join(row))

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    print("Example 1:")
    print("Original board:")
    print_board(board1)
    
    solution.solve(board1)
    
    print("\nAfter capturing surrounded regions:")
    print_board(board1)
    # Expected output:
    # XXXX
    # XXXX
    # XXXX
    # XOXX
    
    # Example 2
    board2 = [["X"]]
    print("\nExample 2:")
    print("Original board:")
    print_board(board2)
    
    solution.solve(board2)
    
    print("\nAfter capturing surrounded regions:")
    print_board(board2)
    # Expected output: X
    
    # Additional example
    board3 = [
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "X", "O"]
    ]
    print("\nExample 3:")
    print("Original board:")
    print_board(board3)
    
    solution.solve(board3)
    
    print("\nAfter capturing surrounded regions:")
    print_board(board3)
    # Expected: 'O's on border remain 'O', inner surrounded 'O's become 'X'
