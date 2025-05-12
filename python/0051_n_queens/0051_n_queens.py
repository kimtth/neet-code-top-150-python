from typing import List

"""
LeetCode N-Queens

Problem from LeetCode: https://leetcode.com/problems/n-queens/

Description:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
"""

class Solution:
    def solve_n_queens(self, n: int) -> List[List[str]]:
        """
        Solve the N-Queens problem and return all distinct solutions.
        
        Args:
            n: The size of the board and number of queens
            
        Returns:
            List[List[str]]: All valid board configurations
        """
        # Initialize the board with empty spaces
        board = [['.'] * n for _ in range(n)]
        result = []
        
        # Sets to keep track of attacked columns and diagonals
        cols = set()
        pos_diag = set()  # Positive diagonals (r+c is constant)
        neg_diag = set()  # Negative diagonals (r-c is constant)
        
        def backtrack(r):
            if r == n:
                # Found a valid configuration, convert board to the required format
                result.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                # Check if this position is under attack
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                
                # Place the queen
                board[r][c] = 'Q'
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                
                # Recursive call for the next row
                backtrack(r+1)
                
                # Backtrack - remove the queen
                board[r][c] = '.'
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
        
        # Start the backtracking process from the first row
        backtrack(0)
        return result
    
    def solve_n_queens_iterative(self, n: int) -> List[List[str]]:
        """
        Solve the N-Queens problem using an iterative approach.
        
        Args:
            n: The size of the board and number of queens
            
        Returns:
            List[List[str]]: All valid board configurations
        """
        result = []
        
        # Use a stack to simulate recursion
        stack = [(0, [], set(), set(), set())]  # (row, queen_positions, cols, pos_diag, neg_diag)
        
        while stack:
            row, queens, cols, pos_diag, neg_diag = stack.pop()
            
            if row == n:
                # Convert the positions to the board representation
                board = [['.' for _ in range(n)] for _ in range(n)]
                for r, c in queens:
                    board[r][c] = 'Q'
                result.append([''.join(row) for row in board])
                continue
            
            for col in range(n - 1, -1, -1):  # Push in reverse order for DFS-like behavior
                if col not in cols and (row+col) not in pos_diag and (row-col) not in neg_diag:
                    # Make copies of the sets to avoid modifying them for sibling branches
                    new_cols = cols.copy()
                    new_pos_diag = pos_diag.copy()
                    new_neg_diag = neg_diag.copy()
                    
                    # Add the queen
                    new_queens = queens + [(row, col)]
                    new_cols.add(col)
                    new_pos_diag.add(row+col)
                    new_neg_diag.add(row-col)
                    
                    stack.append((row + 1, new_queens, new_cols, new_pos_diag, new_neg_diag))
        
        return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    n1 = 4
    result1 = solution.solve_n_queens(n1)
    print(f"Example 1 (n={n1}):")
    for board in result1:
        for row in board:
            print(row)
        print()
    
    # Example 2
    n2 = 1
    result2 = solution.solve_n_queens(n2)
    print(f"Example 2 (n={n2}):")
    for board in result2:
        for row in board:
            print(row)
        print()
    
    # Compare with iterative solution
    print("Using iterative solution (n=4):")
    result_iter = solution.solve_n_queens_iterative(4)
    print(f"Found {len(result_iter)} solutions.")
