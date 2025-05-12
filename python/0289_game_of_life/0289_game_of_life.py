from typing import List


"""
LeetCode 289. Game of Life

Problem from LeetCode: https://leetcode.com/problems/game-of-life/

Description:
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:

1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. 
Given the current state of the m x n grid board, return the next state.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 25
- board[i][j] is 0 or 1

Follow up:
- Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""

class Solution:

    def game_of_life(self, board: List[List[int]]) ->None:
        """
        Implement Conway's Game of Life.
        
        Rules:
        1. Live cell with fewer than 2 live neighbors dies (underpopulation)
        2. Live cell with 2-3 live neighbors survives
        3. Live cell with more than 3 live neighbors dies (overpopulation)
        4. Dead cell with exactly 3 live neighbors becomes alive (reproduction)
        
        Args:
            board: The grid representing cell states (0 dead, 1 alive)
            
        Modifies the board in-place.
        """
        if not board or not board[0]:
            return
        neighbors = [0, 1, -1]
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for i in range(3):
                    for j in range(3):
                        if not (neighbors[i] == 0 and neighbors[j] == 0):
                            r = row + neighbors[i]
                            c = col + neighbors[j]
                            if 0 <= r < rows and 0 <= c < cols and abs(board
                                [r][c]) == 1:
                                live_neighbors += 1
                if board[row][col] == 1 and (live_neighbors < 2 or 
                    live_neighbors > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0

    def game_of_life_with_copy(self, board: List[List[int]]) ->None:
        """
        Alternative implementation that uses a copy of the board.
        This is more straightforward but uses O(m*n) extra space.
        
        Args:
            board: The grid representing cell states (0 dead, 1 alive)
            
        Modifies the board in-place.
        """
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        copy_board = [[board[row][col] for col in range(cols)] for row in
            range(rows)]
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),
            (1, 0), (1, 1)]
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and copy_board[r][c
                        ] == 1:
                        live_neighbors += 1
                if copy_board[row][col] == 1 and (live_neighbors < 2 or 
                    live_neighbors > 3):
                    board[row][col] = 0
                elif copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    board1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print("Example 1:")
    print(f"Input: board = {board1}")
    solution.game_of_life(board1)
    print(f"Output: {board1}")  # Expected output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    
    # Example 2
    board2 = [[1,1],[1,0]]
    print("\nExample 2:")
    print(f"Input: board = {board2}")
    solution.game_of_life(board2)
    print(f"Output: {board2}")  # Expected output: [[1,1],[1,1]]
    
    # Example using the alternative implementation
    board3 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print("\nExample 1 (with copy):")
    print(f"Input: board = {board3}")
    solution.game_of_life_with_copy(board3)
    print(f"Output: {board3}")  # Expected output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
