from typing import List
from collections import deque


"""
LeetCode Rotting Oranges

Problem from LeetCode: https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:
- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or
"""

class Solution:

    def oranges_rotting(self, grid: List[List[int]]) ->int:
        """
        Find the minimum number of minutes to rot all fresh oranges.
        
        Args:
            grid: A 2D grid where:
                 0 represents an empty cell
                 1 represents a fresh orange
                 2 represents a rotten orange
                 
        Returns:
            int: The minimum number of minutes until all oranges are rotten,
                 or -1 if it's impossible
        """
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        fresh_count = 0
        rotten_queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten_queue.append((i, j))
        if fresh_count == 0:
            return 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0
        while rotten_queue and fresh_count > 0:
            size = len(rotten_queue)
            for _ in range(size):
                r, c = rotten_queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c
                        ] == 1:
                        grid[new_r][new_c] = 2
                        fresh_count -= 1
                        rotten_queue.append((new_r, new_c))
            minutes += 1
        return minutes if fresh_count == 0 else -1

    def orangesRotting_alt(self, grid: List[List[int]]) ->int:
        """
        Alternative implementation with a different approach to track time.
        
        Args:
            grid: A 2D grid representing oranges
                 
        Returns:
            int: The minimum number of minutes until all oranges are rotten,
                 or -1 if it's impossible
        """
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        max_time = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            r, c, time = queue.popleft()
            max_time = max(max_time, time)
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c
                    ] == 1:
                    grid[new_r][new_c] = 2
                    fresh -= 1
                    queue.append((new_r, new_c, time + 1))
        return max_time if fresh == 0 else -1


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    result = solution.oranges_rotting(grid)
    print(f"Example 1: {result}")  # Expected: 4
    
    # Example 2
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    result = solution.oranges_rotting(grid)
    print(f"Example 2: {result}")  # Expected: -1
    
    # Example 3
    grid = [[0,2]]
    result = solution.oranges_rotting(grid)
    print(f"Example 3: {result}")  # Expected: 0
