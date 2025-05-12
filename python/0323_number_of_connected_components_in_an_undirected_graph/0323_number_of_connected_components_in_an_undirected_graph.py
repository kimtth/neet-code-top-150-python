from typing import List
from collections import defaultdict


"""
LeetCode Number Of Connected Components In An Undirected Graph

Problem from LeetCode: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Description:
You have a graph of n nodes. You are given an integer n and an array edges where 
edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""

class Solution:

    def count_components(self, n: int, edges: List[List[int]]) ->int:
        """
        Count the number of connected components in an undirected graph.
        
        Args:
            n: Number of nodes (labeled from 0 to n-1)
            edges: List of undirected edges between nodes
            
        Returns:
            int: The number of connected components
        """
        counter = 0
        visited = [0] * n
        adj_list = [[] for _ in range(n)]
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        for i in range(n):
            if visited[i] == 0:
                counter += 1
                self.dfs(adj_list, visited, i)
        return counter

    def dfs(self, adj_list: List[List[int]], visited: List[int], node: int
        ) ->None:
        """
        Depth-first search to mark all nodes in a connected component.
        
        Args:
            adj_list: Adjacency list representation of the graph
            visited: List to track visited nodes
            node: Current node to visit
        """
        visited[node] = 1
        for neighbor in adj_list[node]:
            if visited[neighbor] == 0:
                self.dfs(adj_list, visited, neighbor)

    def count_components_union_find(self, n: int, edges: List[List[int]]
        ) ->int:
        """
        Count connected components using Union-Find algorithm.
        
        Args:
            n: Number of nodes
            edges: List of undirected edges
            
        Returns:
            int: The number of connected components
        """
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)
        for x, y in edges:
            union(x, y)
        return len(set(find(i) for i in range(n)))


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    n1 = 5
    edges1 = [[0, 1], [1, 2], [3, 4]]
    result1 = solution.count_components(n1, edges1)
    print(f"Example 1: {result1}")  # Expected output: 2
    
    # Example 2
    n2 = 5
    edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    result2 = solution.count_components(n2, edges2)
    print(f"Example 2: {result2}")  # Expected output: 1
    
    # Using Union-Find approach
    print("\nUsing Union-Find approach:")
    result3 = solution.count_components_union_find(n1, edges1)
    print(f"Example 1: {result3}")  # Expected output: 2
    
    result4 = solution.count_components_union_find(n2, edges2)
    print(f"Example 2: {result4}")  # Expected output: 1
