from typing import List, Optional

"""
LeetCode Flatten Binary Tree To Linked List

Problem from LeetCode: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Problem Statement:
Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child pointer 
  points to the next node in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flatten a binary tree to a linked list in-place.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            None (modifies the tree in-place)
        """
        self.flatten_tree(root)

    def flatten_tree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Helper method that flattens the tree and returns the tail of the flattened list.
        
        Args:
            node: Current node being processed
            
        Returns:
            The tail node of the flattened list
        """
        # Base cases
        if node is None:
            return None
        if node.left is None and node.right is None:
            return node
            
        # Recursively flatten left and right subtrees
        left_tail = self.flatten_tree(node.left)
        right_tail = self.flatten_tree(node.right)
        
        # If there's a left subtree, attach it between the node and its right child
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
            
        # Return the rightmost node
        return right_tail if right_tail else left_tail


def build_tree(values):
    """Helper function to build a tree from a list of values."""
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
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

def tree_to_list(root):
    """Convert the flattened tree to a list for display."""
    result = []
    current = root
    
    while current:
        result.append(current.val)
        if current.left:
            result.append("Error: left child should be None")
        current = current.right
        
    return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example: [1,2,5,3,4,null,6]
    values = [1, 2, 5, 3, 4, None, 6]
    root = build_tree(values)
    
    # Flatten the tree
    solution.flatten(root)
    
    # Display the flattened tree
    flattened = tree_to_list(root)
    print(f"Flattened tree: {flattened}")  # Expected: [1, 2, 3, 4, 5, 6]