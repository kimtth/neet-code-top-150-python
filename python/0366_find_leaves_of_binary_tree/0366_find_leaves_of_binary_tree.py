from typing import List, Optional


"""
LeetCode Find Leaves of Binary Tree

Problem from LeetCode: https://leetcode.com/problems/find-leaves-of-binary-tree/

Description:
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
1. Collect all the leaf nodes.
2. Remove all the leaf nodes.
3. Repeat until the tree is empty.

Example 1:
Input: root = [1,2,3,4,5]
    1
   / \
  2   3
 / \
4   5
Output: [[4,5,3],[2],[1]]
Explanation:
[[4,5,3]] represents the leaves in the first round.
[[2]] represents the leaves in the second round.
[[1]] represents the leaves in the third round.

Example 2:
Input: root = [1]
Output: [[1]]

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def find_leaves(self, root: Optional[TreeNode]) ->List[List[int]]:
        """
        Find and remove all leaf nodes from a binary tree until the tree is empty.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List[List[int]]: List of leaves at each level, from leaves to root
        """
        result = []
        while root:
            leaves = []
            root = self.removeLeaves(root, leaves)
            result.append(leaves)
        return result

    def removeLeaves(self, node: Optional[TreeNode], leaves: List[int]
        ) ->Optional[TreeNode]:
        """
        Remove leaf nodes and collect their values.
        
        Args:
            node: Current node in the tree
            leaves: List to collect leaf node values
            
        Returns:
            TreeNode: The new tree after removing leaves, or None if tree becomes empty
        """
        if not node:
            return None
        if not node.left and not node.right:
            leaves.append(node.val)
            return None
        node.left = self.removeLeaves(node.left, leaves)
        node.right = self.removeLeaves(node.right, leaves)
        return node

    def find_leaves_by_height(self, root: Optional[TreeNode]) ->List[List[int]
        ]:
        """
        Alternative implementation that groups nodes by their height from bottom.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List[List[int]]: List of nodes grouped by their height from bottom
        """
        result = []

        def getHeight(node):
            if not node:
                return -1
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            height = 1 + max(left_height, right_height)
            if len(result) <= height:
                result.append([])
            result[height].append(node.val)
            return height
        getHeight(root)
        return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Create example tree for Example 1:
    #    1
    #   / \
    #  2   3
    # / \
    #4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Using the iterative approach
    result1 = solution.find_leaves(root)
    print("Example 1 (iterative):")
    print(result1)  # Expected: [[4,5,3],[2],[1]]
    
    # Recreate the tree for the alternative approach
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Using the height-based approach
    result2 = solution.find_leaves_by_height(root)
    print("Example 1 (height-based):")
    print(result2)  # Expected: [[4,5,3],[2],[1]]
