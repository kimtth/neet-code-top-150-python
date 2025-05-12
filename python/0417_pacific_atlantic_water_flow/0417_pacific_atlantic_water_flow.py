from typing import List


"""
LeetCode Pacific Atlantic Water Flow

Problem from LeetCode: https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches 
the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix 
heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly 
north, south, east, and west if the neighboring cell's height is less than or equal to the 
current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water 
can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
    Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    Explanation: The following cells can flow to both the Pacific and Atlantic oceans:
    - [0,4]: [0,4] -> Pacific Ocean 
             [0,4] -> Atlantic Ocean
    - [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
             [1,3] -> [1,4] -> Atlantic Ocean
    - [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
             [1,4] -> Atlantic Ocean
    - [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
             [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
    - [3,0]: [3,0] -> Pacific Ocean 
             [3,0] -> [4,0] -> Atlantic Ocean
    - [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
             [3,1] -> [4,1] -> Atlantic Ocean
    - [4,0]: [4,0] -> Pacific Ocean 
             [4,0] -> Atlantic Ocean

Example 2:
    Input: heights = [[2,1],[1,2]]
    Output: [[0,0],[0,1],[1,0],[1,1]]
    Explanation: Water can flow to both the Pacific and Atlantic Ocean from all cells.

Constraints:
    m == heights.length
    n == heights[r].length
    1 <= m, n <= 200
    0 <= heights[r][c] <= 10^5
"""

class Solution:

    def pacific_atlantic(self, heights: List[List[int]]) ->List[List[int]]:
        """
        Find all points where water can flow to both the Pacific and Atlantic oceans.
        
        Pacific Ocean touches the top and left edges of the matrix.
        Atlantic Ocean touches the bottom and right edges of the matrix.
        Water can flow from a cell to adjacent cells with heights <= the current cell height.
        
        Args:
            heights: A 2D matrix representing the heights of the land
            
        Returns:
            List[List[int]]: A list of [row, col] coordinates that can flow to both oceans
        """
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        pacific_reachable = [([False] * cols) for _ in range(rows)]
        atlantic_reachable = [([False] * cols) for _ in range(rows)]
        for i in range(rows):
            self.dfs(i, 0, pacific_reachable, heights)
            self.dfs(i, cols - 1, atlantic_reachable, heights)
        for j in range(cols):
            self.dfs(0, j, pacific_reachable, heights)
            self.dfs(rows - 1, j, atlantic_reachable, heights)
        result = []
        for i in range(rows):
            for j in range(cols):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])
        return result

    def dfs(self, row: int, col: int, reachable: List[List[bool]], heights:
        List[List[int]]) ->None:
        """
        DFS helper function to mark cells that can reach a certain ocean.
        
        Args:
            row: Current row
            col: Current column
            reachable: Matrix to mark cells that can reach an ocean
            heights: The height matrix
        """
        reachable[row][col] = True
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if new_row < 0 or new_row >= len(heights
                ) or new_col < 0 or new_col >= len(heights[0]):
                continue
            if reachable[new_row][new_col]:
                continue
            if heights[new_row][new_col] < heights[row][col]:
                continue
            self.dfs(new_row, new_col, reachable, heights)

    def pacificAtlantic_bfs(self, heights: List[List[int]]) ->List[List[int]]:
        """
        BFS approach to solve the problem.
        
        Args:
            heights: A 2D matrix representing the heights of the land
            
        Returns:
            List[List[int]]: A list of [row, col] coordinates that can flow to both oceans
        """
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        pacific_queue = []
        atlantic_queue = []
        for i in range(rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, cols - 1))
        for j in range(cols):
            pacific_queue.append((0, j))
            atlantic_queue.append((rows - 1, j))
        pacific_reachable = self.bfs(pacific_queue, heights)
        atlantic_reachable = self.bfs(atlantic_queue, heights)
        return [[i, j] for i in range(rows) for j in range(cols) if 
            pacific_reachable[i][j] and atlantic_reachable[i][j]]

    def bfs(self, queue: List[tuple], heights: List[List[int]]) ->List[List
        [bool]]:
        """
        BFS helper function.
        
        Args:
            queue: Initial cells to start BFS from
            heights: The height matrix
            
        Returns:
            List[List[bool]]: Matrix marking cells that can reach an ocean
        """
        rows, cols = len(heights), len(heights[0])
        reachable = [([False] * cols) for _ in range(rows)]
        for r, c in queue:
            reachable[r][c] = True
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while queue:
            row, col = queue.pop(0)
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (0 <= new_row < rows and 0 <= new_col < cols and not
                    reachable[new_row][new_col] and heights[new_row][
                    new_col] >= heights[row][col]):
                    reachable[new_row][new_col] = True
                    queue.append((new_row, new_col))
        return reachable


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print("Example 1:")
    heights1 = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    result = solution.pacific_atlantic(heights1)
    print(f"Output: {result}")  # Expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    
    # Example 2: heights = [[2,1],[1,2]]
    print("\nExample 2:")
    heights2 = [
        [2,1],
        [1,2]
    ]
    result = solution.pacific_atlantic(heights2)
    print(f"Output: {result}")  # Expected: [[0,0],[0,1],[1,0],[1,1]]
    
    # Test with alternative implementation
    print("\nBFS approach:")
    print(solution.pacificAtlantic_bfs(heights1))
