from typing import Optional
from collections import deque

"""
LeetCode Minimum Depth of Binary Tree

Problem from LeetCode: https://leetcode.com/problems/minimum-depth-of-binary-tree/

Description:
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        """
        Find the minimum depth of a binary tree using DFS.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            int: Minimum depth of the tree
        """
        if not root:
            return 0
            
        # If no left child, recurse on right subtree
        if not root.left:
            return self.min_depth(root.right) + 1
            
        # If no right child, recurse on left subtree
        if not root.right:
            return self.min_depth(root.left) + 1
            
        # Both children exist, take the minimum
        return min(self.min_depth(root.left), self.min_depth(root.right)) + 1
    
    def min_depth_bfs(self, root: Optional[TreeNode]) -> int:
        """
        Find the minimum depth using breadth-first search.
        More efficient for trees with a small minimum depth.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            int: Minimum depth of the tree
        """
        if not root:
            return 0
            
        # Use queue for BFS
        queue = deque([(root, 1)])  # (node, depth)
        
        while queue:
            node, depth = queue.popleft()
            
            # Check if this is a leaf node
            if not node.left and not node.right:
                return depth
                
            # Add children to the queue
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
                
        return 0  # Should not reach here if tree is valid

# Helper function to create a binary tree from a list
def create_tree(values, index=0):
    if not values or index >= len(values) or values[index] is None:
        return None
    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)
    root.right = create_tree(values, 2 * index + 2)
    return root

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    tree1 = create_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.min_depth(tree1)
    print(f"Example 1: {result1}")  # Expected output: 2
    
    # Example 2: Skewed tree
    #    2
    #     \
    #      3
    #       \
    #        4
    #         \
    #          5
    #           \
    #            6
    tree2 = create_tree([2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 6])
    # Alternatively, build the skewed tree manually
    skewed_tree = TreeNode(2)
    skewed_tree.right = TreeNode(3)
    skewed_tree.right.right = TreeNode(4)
    skewed_tree.right.right.right = TreeNode(5)
    skewed_tree.right.right.right.right = TreeNode(6)
    
    result2 = solution.min_depth(skewed_tree)
    print(f"Example 2: {result2}")  # Expected output: 5
    
    # Compare with BFS approach
    print("\nUsing BFS approach:")
    print(f"Example 1: {solution.min_depth_bfs(tree1)}")
    print(f"Example 2: {solution.min_depth_bfs(skewed_tree)}")
