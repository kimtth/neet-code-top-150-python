from typing import List
from collections import defaultdict, deque


"""
LeetCode 261. Graph Valid Tree

Problem from LeetCode: https://leetcode.com/problems/graph-valid-tree/

Description:
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

A graph is a valid tree if:
- It is connected (there is a path between every pair of nodes).
- It has n - 1 edges.
- It has no cycles.

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Explanation: The graph is a valid tree with 5 nodes and 4 edges.

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
Explanation: The graph has a cycle: 1-2-3-1.

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no self-loops or repeated edges.
"""

class Solution:

    def valid_tree(self, n: int, edges: List[List[int]]) ->bool:
        """
        Determine if the given edges form a valid tree.
        
        For a graph to be a valid tree:
        1. It must be fully connected (one component)
        2. It must have no cycles (edges = nodes - 1)
        
        Args:
            n: Number of nodes (labeled from 0 to n-1)
            edges: List of undirected edges
            
        Returns:
            bool: True if the given edges form a valid tree, False otherwise
        """
        # Quick check: a tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
            
        # Build adjacency list
        adj_list = defaultdict(list)
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
            
        # DFS to check if all nodes are connected
        stack = [0]
        visited = {0}
        while stack:
            node = stack.pop()
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    
        # If all nodes are connected, the graph is a valid tree
        return len(visited) == n

    def valid_tree_b_f_s(self, n: int, edges: List[List[int]]) ->bool:
        """
        Determine if the given edges form a valid tree using BFS.
        
        Args:
            n: Number of nodes (labeled from 0 to n-1)
            edges: List of undirected edges
            
        Returns:
            bool: True if the given edges form a valid tree, False otherwise
        """
        # Quick check: a tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
            
        # Build adjacency list
        adj_list = defaultdict(list)
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
            
        # BFS to check if all nodes are connected
        queue = deque([0])
        visited = {0}
        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        # If all nodes are connected, the graph is a valid tree
        return len(visited) == n

    def valid_tree_union_find(self, n: int, edges: List[List[int]]) ->bool:
        """
        Determine if the given edges form a valid tree using Union-Find.
        
        Args:
            n: Number of nodes (labeled from 0 to n-1)
            edges: List of undirected edges
            
        Returns:
            bool: True if the given edges form a valid tree, False otherwise
        """
        # Quick check: a tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
            
        # Initialize parent array for union-find
        parent = list(range(n))

        # Find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union function
        def union(x, y):
            parent[find(x)] = find(y)
            
        # Process each edge
        for x, y in edges:
            # If nodes are already in the same set, adding this edge creates a cycle
            if find(x) == find(y):
                return False
            union(x, y)
            
        return True

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    n1 = 5
    edges1 = [[0,1],[0,2],[0,3],[1,4]]
    result1 = solution.valid_tree(n1, edges1)
    print(f"Example 1: n = {n1}, edges = {edges1}")
    print(f"Output (DFS): {result1}")  # Expected output: True
    
    # Example 2
    n2 = 5
    edges2 = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    result2 = solution.valid_tree(n2, edges2)
    print(f"\nExample 2: n = {n2}, edges = {edges2}")
    print(f"Output (DFS): {result2}")  # Expected output: False
    
    # Using BFS approach
    print("\nUsing BFS approach:")
    print(f"Example 1: {solution.valid_tree_b_f_s(n1, edges1)}")  # Expected output: True
    print(f"Example 2: {solution.valid_tree_b_f_s(n2, edges2)}")  # Expected output: False
    
    # Using Union-Find approach
    print("\nUsing Union-Find approach:")
    print(f"Example 1: {solution.valid_tree_union_find(n1, edges1)}")  # Expected output: True
    print(f"Example 2: {solution.valid_tree_union_find(n2, edges2)}")  # Expected output: False
