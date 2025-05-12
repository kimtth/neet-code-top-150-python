from typing import List, Optional

"""
LeetCode Construct Binary Tree from Preorder and Inorder Traversal

Problem from LeetCode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Description:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Construct a binary tree from preorder and inorder traversal arrays.
        
        Args:
            preorder: Preorder traversal array
            inorder: Inorder traversal array
            
        Returns:
            TreeNode: Root of the constructed binary tree
        """
        if not preorder or not inorder:
            return None
            
        # Create a mapping of value to index in inorder traversal for O(1) lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_start > preorder_end or inorder_start > inorder_end:
                return None
                
            # The first element in preorder is the root
            root_val = preorder[preorder_start]
            root = TreeNode(root_val)
            
            # Find the root position in inorder traversal
            inorder_root_idx = inorder_map[root_val]
            
            # Calculate the size of left subtree
            left_subtree_size = inorder_root_idx - inorder_start
            
            # Recursively build the left and right subtrees
            root.left = build(
                preorder_start + 1, 
                preorder_start + left_subtree_size,
                inorder_start, 
                inorder_root_idx - 1
            )
            
            root.right = build(
                preorder_start + left_subtree_size + 1, 
                preorder_end,
                inorder_root_idx + 1, 
                inorder_end
            )
            
            return root
            
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
    
    def build_tree_iterative(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Construct a binary tree using an iterative approach.
        
        Args:
            preorder: Preorder traversal array
            inorder: Inorder traversal array
            
        Returns:
            TreeNode: Root of the constructed binary tree
        """
        if not preorder or not inorder:
            return None
            
        # Create the root node from the first preorder element
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_idx = 0
        
        # Process the remaining nodes in preorder
        for i in range(1, len(preorder)):
            current = None
            node = TreeNode(preorder[i])
            
            # Find the parent of the current node
            while stack and stack[-1].val == inorder[inorder_idx]:
                current = stack.pop()
                inorder_idx += 1
                
            # Determine if the current node is a left or right child
            if current:
                # Current node popped from stack, new node is right child
                current.right = node
            else:
                # No node popped, new node is left child of the last node in stack
                stack[-1].left = node
                
            stack.append(node)
            
        return root

# Helper function to print tree in level order
def level_order_traversal(root):
    if not root:
        return []
        
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)
                
        # Remove trailing Nones
        while level and level[-1] is None:
            level.pop()
            
        result.extend(level)
        
    return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    root1 = solution.build_tree(preorder1, inorder1)
    result1 = level_order_traversal(root1)
    print(f"Example 1: {result1}")  # Expected output: [3, 9, 20, None, None, 15, 7]
    
    # Example 2
    preorder2 = [-1]
    inorder2 = [-1]
    root2 = solution.build_tree(preorder2, inorder2)
    result2 = level_order_traversal(root2)
    print(f"Example 2: {result2}")  # Expected output: [-1]
    
    # Compare with iterative implementation
    print("\nUsing iterative implementation:")
    root1_iter = solution.build_tree_iterative(preorder1, inorder1)
    result1_iter = level_order_traversal(root1_iter)
    print(f"Example 1: {result1_iter}")  # Should match the recursive approach
