from typing import Optional
from collections import deque

"""
LeetCode Symmetric Tree

Problem from LeetCode: https://leetcode.com/problems/symmetric-tree/

Description:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is symmetric around its center.
        Uses recursive approach.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            bool: True if the tree is symmetric, False otherwise
        """
        if not root:
            return True
            
        return self._isMirror(root.left, root.right)
    
    def _isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """
        Helper function to check if two subtrees are mirrors of each other.
        
        Args:
            left: Left subtree
            right: Right subtree
            
        Returns:
            bool: True if the subtrees are mirrors, False otherwise
        """
        # Both nodes are None - symmetric
        if not left and not right:
            return True
            
        # Only one node is None - not symmetric
        if not left or not right:
            return False
            
        # Both nodes exist, check values and recursive structure
        return (left.val == right.val and
                self._isMirror(left.left, right.right) and
                self._isMirror(left.right, right.left))
    
    def isSymmetric_iterative(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is symmetric using an iterative approach.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            bool: True if the tree is symmetric, False otherwise
        """
        if not root:
            return True
            
        queue = deque([(root.left, root.right)])
        
        while queue:
            left, right = queue.popleft()
            
            # Both None - continue checking other pairs
            if not left and not right:
                continue
                
            # Only one is None or values don't match - not symmetric
            if not left or not right or left.val != right.val:
                return False
                
            # Add mirror pairs to the queue
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
            
        return True

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
    
    # Example 1: Symmetric tree
    root1 = create_tree([1, 2, 2, 3, 4, 4, 3])
    result1 = solution.isSymmetric(root1)
    print(f"Example 1: isSymmetric = {result1}")  # Expected output: True
    
    # Example 2: Non-symmetric tree
    root2 = create_tree([1, 2, 2, None, 3, None, 3])
    result2 = solution.isSymmetric(root2)
    print(f"Example 2: isSymmetric = {result2}")  # Expected output: False
    
    # Example 3: Empty tree
    root3 = None
    result3 = solution.isSymmetric(root3)
    print(f"Example 3 (Empty tree): isSymmetric = {result3}")  # Expected output: True
    
    # Compare with iterative approach
    print("\nUsing iterative approach:")
    print(f"Example 1: {solution.isSymmetric_iterative(root1)}")
    print(f"Example 2: {solution.isSymmetric_iterative(root2)}")
