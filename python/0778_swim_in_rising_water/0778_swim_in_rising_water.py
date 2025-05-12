from typing import List
import heapq


"""
LeetCode Swim In Rising Water

Problem from LeetCode: https://leetcode.com/problems/swim-in-rising-water

Description:
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

Example 1:
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are at position (0, 0).
You cannot swim to (0, 1) because the water depth at (0, 1) is 2.
You cannot swim to (1, 0) because the water depth at (1, 0) is 1.
You must wait until time 1, when you can swim anywhere in the grid.
At time 1, you can swim to (1, 0).
At time 2, you cannot swim to (1, 1), again because the water depth at (1, 1) is 3.
You must wait until time 3 to swim to the bottom right corner.

Example 2:
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown in the grid.

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n^2
Each value grid[i][j] is unique.
"""

class Solution:

    def swim_in_water(self, grid: List[List[int]]) ->int:
        """
        Find the least time until you can reach the bottom right square (n-1, n-1).
        
        Args:
            grid: An n x n grid where grid[i][j] represents the elevation at that square
            
        Returns:
            int: The least time until you can reach the bottom right square
        """
        n = len(grid)
        if n == 1:
            return grid[0][0]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        while min_heap:
            height, row, col = heapq.heappop(min_heap)
            if row == n - 1 and col == n - 1:
                return height
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col
                    ) not in visited:
                    new_height = max(height, grid[new_row][new_col])
                    heapq.heappush(min_heap, (new_height, new_row, new_col))
                    visited.add((new_row, new_col))
        return -1

    def swimInWater_binary_search(self, grid: List[List[int]]) ->int:
        """
        Uses binary search to find the minimum time needed.
        
        Args:
            grid: An n x n grid where grid[i][j] represents the elevation at that square
            
        Returns:
            int: The least time until you can reach the bottom right square
        """
        n = len(grid)

        def can_reach_destination(t: int) ->bool:
            if grid[0][0] > t:
                return False
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            visited = set([(0, 0)])
            queue = [(0, 0)]
            while queue:
                row, col = queue.pop(0)
                if row == n - 1 and col == n - 1:
                    return True
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < n and 0 <= new_col < n and (new_row,
                        new_col) not in visited and grid[new_row][new_col
                        ] <= t:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
            return False
        left, right = grid[0][0], n * n - 1
        while left < right:
            mid = (left + right) // 2
            if can_reach_destination(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def swimInWater_dijkstra(self, grid: List[List[int]]) ->int:
        """
        Uses Dijkstra's algorithm to find the path with minimum maximum height.
        
        Args:
            grid: An n x n grid where grid[i][j] represents the elevation at that square
            
        Returns:
            int: The least time until you can reach the bottom right square
        """
        n = len(grid)
        dist = [([float('inf')] * n) for _ in range(n)]
        dist[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while pq:
            height, row, col = heapq.heappop(pq)
            if height > dist[row][col]:
                continue
            if row == n - 1 and col == n - 1:
                return height
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < n and 0 <= new_col < n:
                    new_height = max(height, grid[new_row][new_col])
                    if new_height < dist[new_row][new_col]:
                        dist[new_row][new_col] = new_height
                        heapq.heappush(pq, (new_height, new_row, new_col))
        return dist[n - 1][n - 1]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    grid1 = [[0, 2], [1, 3]]
    result1 = solution.swim_in_water(grid1)
    print(f"Example 1: {result1}")  # Expected: 3
    
    # Example 2
    grid2 = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6]
    ]
    result2 = solution.swim_in_water(grid2)
    print(f"Example 2: {result2}")  # Expected: 16
