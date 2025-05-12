from typing import List


"""
LeetCode Max Area Of Island

Problem from LeetCode: https://leetcode.com/problems/max-area-of-island/

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical). You may assume all four edges of the 
grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
    Input: grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.
"""

class Solution:

    def max_area_of_island(self, grid: List[List[int]]) ->int:
        """
        Find the maximum area of an island in the grid.
        An island is a group of 1's (representing land) connected 4-directionally.
        
        Args:
            grid: A 2D grid where 1 represents land and 0 represents water
            
        Returns:
            int: The maximum area of an island (0 if no island)
        """
        if not grid or not grid[0]:
            return 0
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            """
            Depth-first search to find the area of an island.
            
            Args:
                r: Row index
                c: Column index
                
            Returns:
                int: Area of the island
            """
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        return max_area

    def maxAreaOfIsland_bfs(self, grid: List[List[int]]) ->int:
        """
        Find the maximum area of an island using breadth-first search.
        
        Args:
            grid: A 2D grid where 1 represents land and 0 represents water
            
        Returns:
            int: The maximum area of an island (0 if no island)
        """
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    queue = [(r, c)]
                    grid[r][c] = 0
                    while queue:
                        curr_r, curr_c = queue.pop(0)
                        area += 1
                        for dr, dc in directions:
                            new_r, new_c = curr_r + dr, curr_c + dc
                            if (0 <= new_r < rows and 0 <= new_c < cols and
                                grid[new_r][new_c] == 1):
                                grid[new_r][new_c] = 0
                                queue.append((new_r, new_c))
                    max_area = max(max_area, area)
        return max_area

    def maxAreaOfIsland_preserve_grid(self, grid: List[List[int]]) ->int:
        """
        Find the maximum area of an island without modifying the input grid.
        
        Args:
            grid: A 2D grid where 1 represents land and 0 represents water
            
        Returns:
            int: The maximum area of an island (0 if no island)
        """
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (
                r, c) in visited:
                return 0
            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r,
                c - 1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        return max_area


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    grid1 = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    result1 = solution.max_area_of_island(grid1)
    print(f"Example 1: {result1}")  # Output: 6
    
    # Create a copy of grid1 for alternative implementations
    import copy
    grid1_copy1 = copy.deepcopy(grid1)
    grid1_copy2 = copy.deepcopy(grid1)
    
    # Example 2
    grid2 = [[0,0,0,0,0,0,0,0]]
    result2 = solution.max_area_of_island(grid2)
    print(f"Example 2: {result2}")  # Output: 0
    
    # Test with alternative implementations
    print("\nAlternative implementations:")
    print(f"BFS approach: {solution.maxAreaOfIsland_bfs(grid1_copy1)}")
    print(f"Preserve grid approach: {solution.maxAreaOfIsland_preserve_grid(grid1_copy2)}")
