from typing import List
from collections import deque


"""
LeetCode 286. Walls and Gates

Problem from LeetCode: https://leetcode.com/problems/walls-and-gates/

Description:
You are given an m x n grid rooms initialized with these three possible values:
- -1: A wall or an obstacle
- 0: A gate
- INF (2^31 - 1): Empty room

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example 1:
Input: rooms = [
  [2147483647, -1, 0, 2147483647],
  [2147483647, 2147483647, 2147483647, -1],
  [2147483647, -1, 2147483647, -1],
  [0, -1, 2147483647, 2147483647]
]
Output: [
  [3, -1, 0, 1],
  [2, 2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3, 4]
]
Explanation: 
- The gate at (0,2) can reach empty rooms at (0,0), (0,3), (1,0), (1,1), (1,2), (2,0), (2,2), (3,2), (3,3)
- The gate at (3,0) can reach empty rooms at (0,0), (1,0), (2,0), (3,2), (3,3)
- The closest gate for the room at (0,0) is at (3,0), which is 3 steps away
"""

class Solution:

    def walls_and_gates(self, rooms: List[List[int]]) ->None:
        """
        Fill each empty room with the distance to its nearest gate.
        
        Args:
            rooms: 2D grid where:
                  -1 represents a wall
                  0 represents a gate
                  INF (2147483647) represents an empty room
                  
        Modifies rooms in-place.
        """
        if not rooms or not rooms[0]:
            return
        INF = 2147483647
        m, n = len(rooms), len(rooms[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and rooms[new_row][new_col] == INF:
                    rooms[new_row][new_col] = rooms[row][col] + 1
                    queue.append((new_row, new_col))

    def walls_and_gates_d_f_s(self, rooms: List[List[int]]) ->None:
        """
        Fill each empty room with the distance to its nearest gate using DFS.
        
        Args:
            rooms: 2D grid where:
                  -1 represents a wall
                  0 represents a gate
                  INF (2147483647) represents an empty room
                  
        Modifies rooms in-place.
        """
        if not rooms or not rooms[0]:
            return
        INF = 2147483647
        m, n = len(rooms), len(rooms[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col, distance):
            if row < 0 or row >= m or col < 0 or col >= n or rooms[row][col] < distance:
                return
            rooms[row][col] = distance
            for dr, dc in directions:
                dfs(row + dr, col + dc, distance + 1)
                
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    INF = 2147483647
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF]
    ]
    
    print("Input rooms:")
    for row in rooms:
        print(row)
    
    solution.walls_and_gates(rooms)
    
    print("\nAfter filling distances:")
    for row in rooms:
        print(row)
    
    # Expected output:
    # [3, -1, 0, 1]
    # [2, 2, 1, -1]
    # [1, -1, 2, -1]
    # [0, -1, 3, 4]
    
    # Example using DFS approach
    rooms_dfs = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF]
    ]
    
    print("\nInput rooms for DFS approach:")
    for row in rooms_dfs:
        print(row)
    
    solution.walls_and_gates_d_f_s(rooms_dfs)
    
    print("\nAfter filling distances (DFS):")
    for row in rooms_dfs:
        print(row)
