from typing import Optional

"""
LeetCode Same Tree

Problem from LeetCode: https://leetcode.com/problems/same-tree/

Description:
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are the same (recursive approach).
        
        Args:
            p: Root of the first binary tree
            q: Root of the second binary tree
            
        Returns:
            bool: True if the trees are the same, False otherwise
        """
        # If both nodes are None, they are the same
        if not p and not q:
            return True
            
        # If one is None but the other isn't, they are different
        if not p or not q:
            return False
            
        # Check if values are the same and recursively check subtrees
        return (p.val == q.val and
                self.is_same_tree(p.left, q.left) and
                self.is_same_tree(p.right, q.right))
    
    def is_same_tree_iterative(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are the same (iterative approach).
        
        Args:
            p: Root of the first binary tree
            q: Root of the second binary tree
            
        Returns:
            bool: True if the trees are the same, False otherwise
        """
        # Queue for BFS traversal of both trees
        queue = [(p, q)]
        
        while queue:
            node1, node2 = queue.pop(0)
            
            # If both nodes are None, continue to next pair
            if not node1 and not node2:
                continue
                
            # If one is None but the other isn't, they are different
            if not node1 or not node2:
                return False
                
            # If values are different, they are different trees
            if node1.val != node2.val:
                return False
                
            # Add children to the queue
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
            
        return True
    
    def is_same_tree_preorder(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are the same using preorder traversal.
        
        Args:
            p: Root of the first binary tree
            q: Root of the second binary tree
            
        Returns:
            bool: True if the trees are the same, False otherwise
        """
        def preorder(node):
            if not node:
                return [None]
            return [node.val] + preorder(node.left) + preorder(node.right)
            
        return preorder(p) == preorder(q)

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    # Tree p:     Tree q:
    #   1           1
    #  / \         / \
    # 2   3       2   3
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    result1 = solution.is_same_tree(p1, q1)
    print(f"Example 1: {result1}")  # Expected output: True
    
    # Example 2
    # Tree p:     Tree q:
    #   1           1
    #  /             \
    # 2               2
    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    result2 = solution.is_same_tree(p2, q2)
    print(f"Example 2: {result2}")  # Expected output: False
    
    # Example 3
    # Tree p:     Tree q:
    #   1           1
    #  / \         / \
    # 2   1       1   2
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    result3 = solution.is_same_tree(p3, q3)
    print(f"Example 3: {result3}")  # Expected output: False
    
    # Compare with other implementations
    print("\nUsing iterative approach:")
    print(f"Example 1: {solution.is_same_tree_iterative(p1, q1)}")
    print(f"Example 2: {solution.is_same_tree_iterative(p2, q2)}")
    print(f"Example 3: {solution.is_same_tree_iterative(p3, q3)}")
    
    print("\nUsing preorder traversal approach:")
    print(f"Example 1: {solution.is_same_tree_preorder(p1, q1)}")
    print(f"Example 2: {solution.is_same_tree_preorder(p2, q2)}")
    print(f"Example 3: {solution.is_same_tree_preorder(p3, q3)}")
