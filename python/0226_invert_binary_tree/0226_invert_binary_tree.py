from typing import List, Optional

"""
LeetCode 226. Invert Binary Tree

Problem from LeetCode: https://leetcode.com/problems/invert-binary-tree/

Description:
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invert_tree(self, root: TreeNode) ->TreeNode:
        """
        Invert a binary tree.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            TreeNode: Root of the inverted binary tree
        """
        if root is None:
            return None
        right = self.invert_tree(root.right)
        left = self.invert_tree(root.left)
        root.left = right
        root.right = left
        return root

    def invert_tree_iterative(self, root: TreeNode) ->TreeNode:
        """
        Invert a binary tree using an iterative approach (BFS).
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            TreeNode: Root of the inverted binary tree
        """
        if not root:
            return None
        queue = [root]
        while queue:
            current = queue.pop(0)
            current.left, current.right = current.right, current.left
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root

# Helper function to create a tree from a level-order traversal array
def create_tree(arr):
    if not arr:
        return None
        
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        node = queue.pop(0)
        
        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
        
    return root

# Helper function to convert a tree to a level-order traversal array
def tree_to_array(root):
    if not root:
        return []
        
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
            
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
        
    return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    arr1 = [4, 2, 7, 1, 3, 6, 9]
    root1 = create_tree(arr1)
    print(f"Example 1: root = {arr1}")
    inverted1 = solution.invert_tree(root1)
    result1 = tree_to_array(inverted1)
    print(f"Output: {result1}")  # Expected output: [4, 7, 2, 9, 6, 3, 1]
    
    # Example 2
    arr2 = [2, 1, 3]
    root2 = create_tree(arr2)
    print(f"\nExample 2: root = {arr2}")
    inverted2 = solution.invert_tree(root2)
    result2 = tree_to_array(inverted2)
    print(f"Output: {result2}")  # Expected output: [2, 3, 1]
    
    # Example 3
    arr3 = []
    root3 = create_tree(arr3)
    print(f"\nExample 3: root = {arr3}")
    inverted3 = solution.invert_tree(root3)
    result3 = tree_to_array(inverted3)
    print(f"Output: {result3}")  # Expected output: []
    
    # Using iterative approach
    print("\nUsing iterative approach:")
    root1 = create_tree(arr1)  # Reset the tree
    inverted1_iter = solution.invert_tree_iterative(root1)
    result1_iter = tree_to_array(inverted1_iter)
    print(f"Example 1: {result1_iter}")  # Expected output: [4, 7, 2, 9, 6, 3, 1]
