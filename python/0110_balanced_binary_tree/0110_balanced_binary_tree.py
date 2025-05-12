from typing import Optional

"""
LeetCode Balanced Binary Tree

Problem from LeetCode: https://leetcode.com/problems/balanced-binary-tree/

Description:
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if the binary tree is height-balanced.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            bool: True if the tree is height-balanced, False otherwise
        """
        # Helper function to calculate height and check balance
        def check_height(node):
            if not node:
                return 0
                
            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced
                
            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced
                
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1  # Current node is unbalanced
                
            # Return height of current subtree
            return max(left_height, right_height) + 1
            
        return check_height(root) != -1
    
    def is_balanced_separate(self, root: Optional[TreeNode]) -> bool:
        """
        Alternative implementation with separate height calculation.
        Less efficient but more straightforward.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            bool: True if the tree is height-balanced, False otherwise
        """
        if not root:
            return True
            
        # Helper function to calculate height
        def height(node):
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1
            
        # Check if current node is balanced
        if abs(height(root.left) - height(root.right)) > 1:
            return False
            
        # Check if both subtrees are balanced
        return self.is_balanced_separate(root.left) and self.is_balanced_separate(root.right)

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
    
    # Example 1: Balanced tree
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    tree1 = create_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.is_balanced(tree1)
    print(f"Example 1: {result1}")  # Expected output: True
    
    # Example 2: Unbalanced tree
    #        1
    #       / \
    #      2   2
    #     / \
    #    3   3
    #   / \
    #  4   4
    tree2 = create_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    result2 = solution.is_balanced(tree2)
    print(f"Example 2: {result2}")  # Expected output: False
    
    # Example 3: Empty tree
    tree3 = None
    result3 = solution.is_balanced(tree3)
    print(f"Example 3: {result3}")  # Expected output: True
    
    # Compare with alternative implementation
    print("\nUsing alternative implementation:")
    print(f"Example 1: {solution.is_balanced_separate(tree1)}")
    print(f"Example 2: {solution.is_balanced_separate(tree2)}")
    print(f"Example 3: {solution.is_balanced_separate(tree3)}")
