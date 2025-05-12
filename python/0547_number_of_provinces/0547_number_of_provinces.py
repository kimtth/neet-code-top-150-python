from typing import List
from collections import deque


"""
LeetCode Number Of Provinces

Problem from LeetCode: https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are 
directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2

Example 2:
    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3

Constraints:
    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]
"""

class Solution:

    def find_circle_num(self, isConnected: List[List[int]]) ->int:
        """
        Find the number of provinces (connected components) in the graph.
        
        Args:
            isConnected: Adjacency matrix where isConnected[i][j] = 1 if the ith city and the jth city are
                         directly connected, and isConnected[i][j] = 0 otherwise.
            
        Returns:
            int: The number of provinces (connected components)
        """
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        for i in range(n):
            if not visited[i]:
                self._bfs(isConnected, visited, i)
                provinces += 1
        return provinces

    def _bfs(self, isConnected: List[List[int]], visited: List[bool], start:
        int) ->None:
        """
        Perform BFS to mark all cities in the current province as visited.
        
        Args:
            isConnected: Adjacency matrix
            visited: Array to track visited nodes
            start: Starting city for BFS
        """
        queue = deque([start])
        visited[start] = True
        while queue:
            city = queue.popleft()
            for i in range(len(isConnected)):
                if isConnected[city][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)

    def findCircleNum_dfs(self, isConnected: List[List[int]]) ->int:
        """
        Find the number of provinces using DFS.
        
        Args:
            isConnected: Adjacency matrix
            
        Returns:
            int: The number of provinces
        """
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(node: int) ->None:
            visited[node] = True
            for i in range(n):
                if isConnected[node][i] == 1 and not visited[i]:
                    dfs(i)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1
        return provinces

    def findCircleNum_union_find(self, isConnected: List[List[int]]) ->int:
        """
        Find the number of provinces using Union-Find (Disjoint Set).
        
        Args:
            isConnected: Adjacency matrix
            
        Returns:
            int: The number of provinces
        """
        n = len(isConnected)
        parent = list(range(n))

        def find(x: int) ->int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) ->None:
            parent[find(x)] = find(y)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        return sum(1 for i in range(n) if parent[i] == i)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print("Example 1:")
    result = solution.find_circle_num([[1,1,0],[1,1,0],[0,0,1]])
    print(f"Output: {result}")  # Expected: 2
    
    # Example 2: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print("\nExample 2:")
    result = solution.find_circle_num([[1,0,0],[0,1,0],[0,0,1]])
    print(f"Output: {result}")  # Expected: 3
    
    # Test with alternative implementations
    print("\nAlternative implementations:")
    print("DFS approach:", solution.findCircleNum_dfs([[1,1,0],[1,1,0],[0,0,1]]))
    print("Union-Find approach:", solution.findCircleNum_union_find([[1,1,0],[1,1,0],[0,0,1]]))
