from typing import List


"""
LeetCode Number of Islands

Problem from LeetCode: https://leetcode.com/problems/number-of-islands/

Description:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

class Solution:

    def num_islands(self, grid: List[List[str]]) ->int:
        """
        Count the number of islands in a 2D grid.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        
        Args:
            grid: The 2D grid where '1' represents land and '0' represents water.
            
        Returns:
            int: The number of islands.
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    island_count += 1
                    self.dfs(i, j, grid)
        return island_count

    def dfs(self, row: int, col: int, grid: List[List[str]]) ->None:
        """
        Depth-first search to mark all connected lands as visited ('0').
        
        Args:
            row: Current row index
            col: Current column index
            grid: The 2D grid
        """
        rows = len(grid)
        cols = len(grid[0])
        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col
            ] == '0':
            return
        grid[row][col] = '0'
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            self.dfs(row + dr, col + dc, grid)

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    result1 = solution.num_islands(grid1)
    print(f"Example 1: {result1}")  # Expected output: 1
    
    # Example 2
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result2 = solution.num_islands(grid2)
    print(f"Example 2: {result2}")  # Expected output: 3
