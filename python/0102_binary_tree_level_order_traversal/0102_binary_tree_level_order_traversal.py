from typing import List, Optional
from collections import deque

"""
LeetCode Binary Tree Level Order Traversal

Problem from LeetCode: https://leetcode.com/problems/binary-tree-level-order-traversal/

Description:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform level order traversal of a binary tree.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List[List[int]]: Values of nodes in level order (level by level)
        """
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            # Get the size of the current level
            level_size = len(queue)
            level_values = []
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # Add the current level's values to the result
            result.append(level_values)
            
        return result
    
    def levelOrder_recursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform level order traversal using a recursive approach.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List[List[int]]: Values of nodes in level order
        """
        result = []
        
        def dfs(node, level):
            """Recursive DFS helper function."""
            if not node:
                return
                
            # If this is a new level, add a new empty list
            if level == len(result):
                result.append([])
                
            # Add the current node's value to the appropriate level
            result[level].append(node.val)
            
            # Recursively process children
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root, 0)
        return result

# Helper function to create a binary tree from a level-order traversal list
def create_tree(values):
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
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
    result1 = solution.levelOrder(root1)
    print(f"Example 1: {result1}")  # Expected output: [[3], [9, 20], [15, 7]]
    
    # Example 2
    root2 = create_tree([1])
    result2 = solution.levelOrder(root2)
    print(f"Example 2: {result2}")  # Expected output: [[1]]
    
    # Example 3
    root3 = create_tree([])
    result3 = solution.levelOrder(root3)
    print(f"Example 3: {result3}")  # Expected output: []
    
    # Compare with recursive approach
    print("\nUsing recursive approach:")
    print(f"Example 1: {solution.levelOrder_recursive(root1)}")
    print(f"Example 2: {solution.levelOrder_recursive(root2)}")
