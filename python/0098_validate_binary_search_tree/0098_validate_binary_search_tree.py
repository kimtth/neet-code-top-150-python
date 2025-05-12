from typing import Optional

"""
LeetCode Validate Binary Search Tree

Problem from LeetCode: https://leetcode.com/problems/validate-binary-search-tree/

Description:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if a binary tree is a valid binary search tree.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            bool: True if the tree is a valid BST, False otherwise
        """
        # Helper function for recursive validation with min/max boundaries
        def validate(node, lower=float('-inf'), upper=float('inf')):
            # Empty trees are valid BSTs
            if not node:
                return True
                
            # Check if current node's value violates the BST property
            if node.val <= lower or node.val >= upper:
                return False
                
            # Recursively check left and right subtrees
            # Left subtree must have values less than the current node
            # Right subtree must have values greater than the current node
            return (validate(node.left, lower, node.val) and
                    validate(node.right, node.val, upper))
                    
        return validate(root)
    
    def is_valid_bst_inorder(self, root: Optional[TreeNode]) -> bool:
        """
        Validate BST using inorder traversal.
        In a BST, inorder traversal should yield a sorted array.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            bool: True if the tree is a valid BST, False otherwise
        """
        prev = float('-inf')
        
        # Helper function for inorder traversal
        def inorder(node):
            nonlocal prev
            
            if not node:
                return True
                
            # Check left subtree
            if not inorder(node.left):
                return False
                
            # Check current node's value against the previous value
            if node.val <= prev:
                return False
                
            # Update previous value
            prev = node.val
            
            # Check right subtree
            return inorder(node.right)
            
        return inorder(root)
    
    def is_valid_bst_iterative(self, root: Optional[TreeNode]) -> bool:
        """
        Validate BST using iterative inorder traversal.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            bool: True if the tree is a valid BST, False otherwise
        """
        if not root:
            return True
            
        stack = []
        prev = float('-inf')
        current = root
        
        while stack or current:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left
                
            # Check the current node
            current = stack.pop()
            
            # If current value is less than or equal to previous, it's not a BST
            if current.val <= prev:
                return False
                
            # Update previous value
            prev = current.val
            
            # Move to the right subtree
            current = current.right
            
        return True

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    # Tree:
    #   2
    #  / \
    # 1   3
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    result1 = solution.is_valid_bst(root1)
    print(f"Example 1: {result1}")  # Expected output: True
    
    # Example 2
    # Tree:
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    result2 = solution.is_valid_bst(root2)
    print(f"Example 2: {result2}")  # Expected output: False
    
    # Additional example
    # Tree:
    #     10
    #    /  \
    #   5    15
    #       /  \
    #      12   20
    root3 = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(12), TreeNode(20)))
    result3 = solution.is_valid_bst(root3)
    print(f"Example 3: {result3}")  # Expected output: True
    
    # Compare with other implementations
    print("\nUsing inorder traversal approach:")
    print(f"Example 1: {solution.is_valid_bst_inorder(root1)}")
    print(f"Example 2: {solution.is_valid_bst_inorder(root2)}")
    print(f"Example 3: {solution.is_valid_bst_inorder(root3)}")
    
    print("\nUsing iterative approach:")
    print(f"Example 1: {solution.is_valid_bst_iterative(root1)}")
    print(f"Example 2: {solution.is_valid_bst_iterative(root2)}")
    print(f"Example 3: {solution.is_valid_bst_iterative(root3)}")
