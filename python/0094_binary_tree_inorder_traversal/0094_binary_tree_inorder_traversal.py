from typing import List, Optional

"""
LeetCode Binary Tree Inorder Traversal

Problem from LeetCode: https://leetcode.com/problems/binary-tree-inorder-traversal/

Description:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform an inorder traversal of a binary tree (recursive approach).
        Inorder: left -> root -> right
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List[int]: Inorder traversal values
        """
        result = []
        self._inorder_helper(root, result)
        return result
        
    def _inorder_helper(self, node: Optional[TreeNode], result: List[int]) -> None:
        """Helper function for recursive inorder traversal."""
        if not node:
            return
            
        # Traverse left subtree
        self._inorder_helper(node.left, result)
        
        # Visit the node
        result.append(node.val)
        
        # Traverse right subtree
        self._inorder_helper(node.right, result)
    
    def inorder_traversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform an inorder traversal of a binary tree (iterative approach).
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List[int]: Inorder traversal values
        """
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left
                
            # Visit the node at the top of the stack
            current = stack.pop()
            result.append(current.val)
            
            # Move to the right subtree
            current = current.right
            
        return result
    
    def inorder_traversal_morris(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform an inorder traversal using Morris Traversal.
        This approach uses O(1) extra space and doesn't use recursion or a stack.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List[int]: Inorder traversal values
        """
        result = []
        current = root
        
        while current:
            # If there is no left child, visit the node and go right
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                # Find the inorder predecessor (rightmost node in left subtree)
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                # If right pointer is null, make it point to current
                # This creates a temporary link to get back to the root
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    # Revert the change made in the above step
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right
                    
        return result

# Helper function to create a binary tree from a list of values
def create_tree(values):
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

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    # Tree:
    #   1
    #    \
    #     2
    #    /
    #   3
    root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    result1 = solution.inorder_traversal(root1)
    print(f"Example 1: {result1}")  # Expected output: [1, 3, 2]
    
    # Example 2
    root2 = None
    result2 = solution.inorder_traversal(root2)
    print(f"Example 2: {result2}")  # Expected output: []
    
    # Example 3
    root3 = TreeNode(1)
    result3 = solution.inorder_traversal(root3)
    print(f"Example 3: {result3}")  # Expected output: [1]
    
    # Additional example
    # Tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root4 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    result4 = solution.inorder_traversal(root4)
    print(f"Example 4: {result4}")  # Expected output: [4, 2, 5, 1, 3]
    
    # Compare with iterative and Morris traversal
    print("\nUsing iterative approach:")
    print(f"Example 1: {solution.inorder_traversal_iterative(root1)}")
    print(f"Example 4: {solution.inorder_traversal_iterative(root4)}")
    
    print("\nUsing Morris traversal:")
    print(f"Example 1: {solution.inorder_traversal_morris(root1)}")
    print(f"Example 4: {solution.inorder_traversal_morris(root4)}")
