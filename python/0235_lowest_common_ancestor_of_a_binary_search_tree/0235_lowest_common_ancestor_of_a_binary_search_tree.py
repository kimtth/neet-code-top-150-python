from typing import Optional


"""
LeetCode 235: Lowest Common Ancestor of a Binary Search Tree

Problem from LeetCode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the BST.
"""

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q:
        'TreeNode') ->'TreeNode':
        """
        Find the lowest common ancestor (LCA) node of two given nodes in a binary search tree.
        
        The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
        that has both p and q as descendants (where we allow a node to be a descendant of itself).
        
        Args:
            root: Root node of the BST
            p: First node
            q: Second node
            
        Returns:
            TreeNode: The LCA node
        """
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val > parent_val and q_val > parent_val:
            return self.lowest_common_ancestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowest_common_ancestor(root.left, p, q)
        else:
            return root

    def lowest_common_ancestor_iterative(self, root: 'TreeNode', p:
        'TreeNode', q: 'TreeNode') ->'TreeNode':
        """
        Find the lowest common ancestor using an iterative approach.
        
        Args:
            root: Root node of the BST
            p: First node
            q: Second node
            
        Returns:
            TreeNode: The LCA node
        """
        current = root
        p_val = p.val
        q_val = q.val
        while current:
            parent_val = current.val
            if p_val > parent_val and q_val > parent_val:
                current = current.right
            elif p_val < parent_val and q_val < parent_val:
                current = current.left
            else:
                return current
        return None


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    # Creating the BST from Example 1: [6,2,8,0,4,7,9,null,null,3,5]
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    
    solution = Solution()
    # Example 1: p = 2, q = 8
    p = root.left  # Node with value 2
    q = root.right  # Node with value 8
    result = solution.lowest_common_ancestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {result.val}")  # Output: 6
    
    # Example 2: p = 2, q = 4
    p = root.left  # Node with value 2
    q = root.left.right  # Node with value 4
    result = solution.lowest_common_ancestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {result.val}")  # Output: 2
