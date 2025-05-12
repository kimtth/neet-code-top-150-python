from typing import List, Optional
from collections import deque


"""
LeetCode Binary Tree Zigzag Level Order Traversal

Problem from LeetCode: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Description:
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzag_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Return the zigzag level order traversal of a binary tree's values.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List[List[int]]: Zigzag level order traversal
        """
        if not root:
            return []
            
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add the level values in zigzag order
            if not left_to_right:
                level.reverse()
                
            result.append(level)
            left_to_right = not left_to_right
            
        return result
    
    def zigzag_level_order_alternative(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Alternative implementation using a deque for each level.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List[List[int]]: Zigzag level order traversal
        """
        if not root:
            return []
            
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level = deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # Add values in zigzag order using a deque
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(level))
            left_to_right = not left_to_right
            
        return result
    
    def zigzag_level_order_dfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        DFS-based implementation for zigzag level order traversal.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List[List[int]]: Zigzag level order traversal
        """
        result = []
        
        def dfs(node, level):
            if not node:
                return
                
            # Add new level if needed
            if len(result) <= level:
                result.append([])
                
            # Add node value to the current level
            result[level].append(node.val)
            
            # Process children
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        
        # Reverse alternate levels for zigzag ordering
        for i in range(1, len(result), 2):
            result[i].reverse()
            
        return result

# Helper function to create a binary tree from level order list
def create_tree(values):
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Add left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Add right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
        
    return root

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    root1 = create_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.zigzag_level_order(root1)
    print(f"Example 1: {result1}")  # Expected output: [[3],[20,9],[15,7]]
    
    # Example 2
    root2 = create_tree([1])
    result2 = solution.zigzag_level_order(root2)
    print(f"Example 2: {result2}")  # Expected output: [[1]]
    
    # Example 3
    root3 = create_tree([])
    result3 = solution.zigzag_level_order(root3)
    print(f"Example 3: {result3}")  # Expected output: []
    
    # Compare with alternative implementations
    print("\nUsing alternative implementation:")
    print(f"Example 1: {solution.zigzag_level_order_alternative(root1)}")
    
    print("\nUsing DFS-based implementation:")
    print(f"Example 1: {solution.zigzag_level_order_dfs(root1)}")
