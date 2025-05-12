from typing import Optional
from collections import deque

"""
LeetCode Maximum Depth of Binary Tree

Problem from LeetCode: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Description:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum depth of a binary tree using recursive DFS.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            int: Maximum depth of the binary tree
        """
        if not root:
            return 0
            
        # Maximum depth = 1 (current node) + max depth of left or right subtree
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
    
    def max_depth_iterative_dfs(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum depth using iterative DFS with a stack.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            int: Maximum depth of the binary tree
        """
        if not root:
            return 0
            
        stack = [(root, 1)]  # (node, depth)
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
                
        return max_depth
    
    def max_depth_bfs(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum depth using BFS level order traversal.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            int: Maximum depth of the binary tree
        """
        if not root:
            return 0
            
        queue = deque([root])
        depth = 0
        
        while queue:
            # Process all nodes at the current level
            level_size = len(queue)
            depth += 1
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return depth

# Helper function to create a binary tree from level order list
def create_tree(values):
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Add left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Add right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
        
    return root

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    root1 = create_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.max_depth(root1)
    print(f"Example 1: {result1}")  # Expected output: 3
    
    # Example 2
    root2 = create_tree([1, None, 2])
    result2 = solution.max_depth(root2)
    print(f"Example 2: {result2}")  # Expected output: 2
    
    # Compare with other implementations
    print("\nUsing iterative DFS:")
    print(f"Example 1: {solution.max_depth_iterative_dfs(root1)}")
    print(f"Example 2: {solution.max_depth_iterative_dfs(root2)}")
    
    print("\nUsing BFS:")
    print(f"Example 1: {solution.max_depth_bfs(root1)}")
    print(f"Example 2: {solution.max_depth_bfs(root2)}")
