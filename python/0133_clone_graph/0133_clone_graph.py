from typing import Optional
from collections import deque

"""
LeetCode Clone Graph

Problem from LeetCode: https://leetcode.com/problems/clone-graph/

Description:
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """
        Deep clone a graph using DFS.
        
        Args:
            node: Reference to a node in the graph
            
        Returns:
            Node: Reference to the corresponding node in the cloned graph
        """
        if not node:
            return None
            
        # Dictionary to map original nodes to their clones
        clones = {}
        
        def dfs(original: Node) -> Node:
            # If node is already cloned, return its clone
            if original in clones:
                return clones[original]
                
            # Create a clone of the current node
            clone = Node(original.val)
            
            # Map the original node to its clone
            clones[original] = clone
            
            # Clone all neighbors and connect them to the current clone
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
            
        return dfs(node)
    
    def cloneGraph_bfs(self, node: Optional[Node]) -> Optional[Node]:
        """
        Deep clone a graph using BFS.
        
        Args:
            node: Reference to a node in the graph
            
        Returns:
            Node: Reference to the corresponding node in the cloned graph
        """
        if not node:
            return None
            
        # Dictionary to map original nodes to their clones
        clones = {}
        
        # Create a clone of the starting node
        clones[node] = Node(node.val)
        
        # Initialize queue with the starting node
        queue = deque([node])
        
        while queue:
            original = queue.popleft()
            
            # Process each neighbor of the original node
            for neighbor in original.neighbors:
                if neighbor not in clones:
                    # Create clone for this neighbor if not already cloned
                    clones[neighbor] = Node(neighbor.val)
                    # Add neighbor to queue for further processing
                    queue.append(neighbor)
                    
                # Connect the clone of the current node to the clone of the neighbor
                clones[original].neighbors.append(clones[neighbor])
                
        return clones[node]

# Helper function to create a graph from an adjacency list
def create_graph_from_adj_list(adj_list):
    if not adj_list:
        return None
        
    # Create nodes
    nodes = [Node(i+1) for i in range(len(adj_list))]
    
    # Connect neighbors
    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            nodes[i].neighbors.append(nodes[neighbor-1])
            
    return nodes[0] if nodes else None

# Helper function to convert a graph to an adjacency list
def graph_to_adj_list(node):
    if not node:
        return []
        
    visited = {}
    result = []
    
    def dfs(n):
        if n.val in visited:
            return
            
        # Mark as visited
        visited[n.val] = True
        
        # Ensure result list is long enough
        while len(result) < n.val:
            result.append([])
            
        # Add neighbors to adjacency list
        for neighbor in n.neighbors:
            result[n.val-1].append(neighbor.val)
            dfs(neighbor)
            
    dfs(node)
    return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    adj_list1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    graph1 = create_graph_from_adj_list(adj_list1)
    cloned1 = solution.cloneGraph(graph1)
    result1 = graph_to_adj_list(cloned1)
    print(f"Example 1: {result1}")  # Expected: [[2, 4], [1, 3], [2, 4], [1, 3]]
    
    # Example 2
    adj_list2 = [[]]
    graph2 = create_graph_from_adj_list(adj_list2)
    cloned2 = solution.cloneGraph(graph2)
    result2 = graph_to_adj_list(cloned2)
    print(f"Example 2: {result2}")  # Expected: [[]]
    
    # Example 3
    adj_list3 = []
    graph3 = create_graph_from_adj_list(adj_list3)
    cloned3 = solution.cloneGraph(graph3)
    result3 = graph_to_adj_list(cloned3)
    print(f"Example 3: {result3}")  # Expected: []
    
    # Compare with BFS approach
    cloned4 = solution.cloneGraph_bfs(graph1)
    result4 = graph_to_adj_list(cloned4)
    print(f"\nBFS approach for Example 1: {result4}")
