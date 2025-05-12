from collections import deque
from typing import List, Optional


"""
LeetCode Binary Tree Right Side View

Problem from LeetCode: https://leetcode.com/problems/binary-tree-right-side-view/

Description:
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation: The right side view of the tree is [1,3,4].

Example 2:
Input: root = [1,null,3]
Output: [1,3]

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
    def right_side_view(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the values of nodes visible from the right side of the binary tree.
        Uses a level-order traversal (BFS) approach.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List[int]: Values of nodes visible from the right side
        """
        result = []
        if not root:
            return result
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                current_node = queue.popleft()
                if i == level_size - 1:
                    result.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return result
    
    def right_side_view_dfs(self, root: Optional[TreeNode]) -> List[int]:
        """
        Alternative implementation using DFS approach.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List[int]: Values of nodes visible from the right side
        """
        result = []
        
        def dfs(node, level):
            if not node:
                return
                
            # If this is the first node we've seen at this level
            if len(result) == level:
                result.append(node.val)
                
            # Visit right first, then left (to get rightmost nodes first)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
            
        dfs(root, 0)
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: [1,2,3,null,5,null,4]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    
    result1 = solution.right_side_view(root1)
    print(f"Example 1: {result1}")  # Expected output: [1, 3, 4]
    
    # Example 2: [1,null,3]
    root2 = TreeNode(1)
    root2.right = TreeNode(3)
    
    result2 = solution.right_side_view(root2)
    print(f"Example 2: {result2}")  # Expected output: [1, 3]
    
    # Example 3: []
    result3 = solution.right_side_view(None)
    print(f"Example 3: {result3}")  # Expected output: []
    
    # Compare with DFS approach
    print("\nUsing DFS approach:")
    print(f"Example 1: {solution.right_side_view_dfs(root1)}")  # Expected output: [1, 3, 4]
    print(f"Example 2: {solution.right_side_view_dfs(root2)}")  # Expected output: [1, 3]
