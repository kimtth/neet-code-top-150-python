from typing import Optional


"""
LeetCode Diameter Of Binary Tree

Problem from LeetCode: https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
    Input: root = [1,2]
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    -100 <= Node.val <= 100
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameter_of_binary_tree(self, root: Optional[TreeNode]) ->int:
        """
        Calculate the diameter of a binary tree (the length of the longest path between any two nodes).
        
        Args:
            root: Root of the binary tree
            
        Returns:
            int: The diameter of the tree
        """
        self.max_diameter = 0

        def get_height(node: Optional[TreeNode]) ->int:
            """
            Calculate the height of a node and update the max_diameter.
            
            Args:
                node: Current tree node
                
            Returns:
                int: Height of the node
            """
            if not node:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            self.max_diameter = max(self.max_diameter, left_height +
                right_height)
            return 1 + max(left_height, right_height)
        get_height(root)
        return self.max_diameter

    def diameterOfBinaryTree_explicit(self, root: Optional[TreeNode]) ->int:
        """
        Calculate the diameter using an explicit calculation for each node.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            int: The diameter of the tree
        """
        if not root:
            return 0
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        diameter_through_root = left_height + right_height
        left_diameter = self.diameterOfBinaryTree_explicit(root.left)
        right_diameter = self.diameterOfBinaryTree_explicit(root.right)
        return max(diameter_through_root, left_diameter, right_diameter)

    def _height(self, node: Optional[TreeNode]) ->int:
        """
        Calculate the height of a node.
        
        Args:
            node: Current tree node
            
        Returns:
            int: Height of the node
        """
        if not node:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: [1,2,3,4,5]
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    
    print("Example 1:")
    result = solution.diameter_of_binary_tree(root1)
    print(f"Output: {result}")  # Expected: 3
    
    # Example 2: [1,2]
    #   1
    #  /
    # 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    
    print("\nExample 2:")
    result = solution.diameter_of_binary_tree(root2)
    print(f"Output: {result}")  # Expected: 1
    
    # Test with alternative implementation
    print("\nAlternative implementation:")
    print("Explicit calculation:", solution.diameterOfBinaryTree_explicit(root1))
