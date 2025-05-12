from typing import List


"""
LeetCode Redundant Connection

Problem from LeetCode: https://leetcode.com/problems/redundant-connection/

Description:
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

Constraints:
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""

class Solution:

    def find_redundant_connection(self, edges: List[List[int]]) ->List[int]:
        """
        In a graph with N nodes and N edges, find the last edge that creates a cycle.
        
        Args:
            edges: A list of edges where edges[i] = [u, v] with u < v
            
        Returns:
            The edge that can be removed to make the graph a tree (no cycles)
        """
        parent = list(range(len(edges) + 1))

        def find(node):
            """Find the root of a node with path compression."""
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            """Union the sets of node1 and node2."""
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return False
            parent[root2] = root1
            return True
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
        return []

    def findRedundantConnection_with_rank(self, edges: List[List[int]]) ->List[
        int]:
        """
        Implementation using Union-Find with rank for better performance.
        
        Args:
            edges: A list of edges where edges[i] = [u, v] with u < v
            
        Returns:
            The edge that can be removed to make the graph a tree
        """
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []

    def findRedundantConnection_dfs(self, edges: List[List[int]]) ->List[int]:
        """
        Alternative implementation using DFS to detect cycles.
        
        Args:
            edges: A list of edges where edges[i] = [u, v] with u < v
            
        Returns:
            The edge that can be removed to make the graph a tree
        """
        n = len(edges)
        graph = [[] for _ in range(n + 1)]

        def has_path(source, target, visited):
            if source == target:
                return True
            visited.add(source)
            for neighbor in graph[source]:
                if neighbor not in visited:
                    if has_path(neighbor, target, visited):
                        return True
            return False
        for u, v in edges:
            if has_path(u, v, set()):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)
        return []


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    edges1 = [[1, 2], [1, 3], [2, 3]]
    result1 = solution.find_redundant_connection(edges1)
    print(f"Example 1: {result1}")  # Expected: [2, 3]
    
    # Example 2
    edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    result2 = solution.find_redundant_connection(edges2)
    print(f"Example 2: {result2}")  # Expected: [1, 4]
    
    # Test with rank optimization
    print("\nWith rank optimization:")
    result3 = solution.findRedundantConnection_with_rank(edges1)
    print(f"Example 1: {result3}")  # Expected: [2, 3]
    
    # Test with DFS
    print("\nWith DFS:")
    result4 = solution.findRedundantConnection_dfs(edges1)
    print(f"Example 1: {result4}")  # Expected: [2, 3]
