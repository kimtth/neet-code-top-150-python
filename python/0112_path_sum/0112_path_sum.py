from typing import Optional

"""
LeetCode Path Sum

Problem from LeetCode: https://leetcode.com/problems/path-sum/

Description:
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is 5 -> 4 -> 11 -> 2.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 -> 2): The sum is 3.
(1 -> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def has_path_sum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Check if there is a root-to-leaf path with the given sum.
        
        Args:
            root: Root of the binary tree
            targetSum: Target sum to find
            
        Returns:
            bool: True if a path with the target sum exists, False otherwise
        """
        # Base case: empty tree
        if not root:
            return False
            
        # Subtract the current node's value from the target
        targetSum -= root.val
        
        # If this is a leaf node, check if the target sum is reached
        if not root.left and not root.right:
            return targetSum == 0
            
        # Recursively check left and right subtrees
        return (self.has_path_sum(root.left, targetSum) or 
                self.has_path_sum(root.right, targetSum))
    
    def has_path_sum_iterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Iterative approach using a stack.
        
        Args:
            root: Root of the binary tree
            targetSum: Target sum to find
            
        Returns:
            bool: True if a path with the target sum exists, False otherwise
        """
        if not root:
            return False
            
        # Stack to store nodes and their accumulated sum
        stack = [(root, root.val)]
        
        while stack:
            node, current_sum = stack.pop()
            
            # Check if this is a leaf node with the target sum
            if not node.left and not node.right and current_sum == targetSum:
                return True
                
            # Add right child to the stack
            if node.right:
                stack.append((node.right, current_sum + node.right.val))
                
            # Add left child to the stack
            if node.left:
                stack.append((node.left, current_sum + node.left.val))
                
        return False

# Helper function to create a binary tree from a list
def create_tree(values, index=0):
    if not values or index >= len(values) or values[index] is None:
        return None
    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)
    root.right = create_tree(values, 2 * index + 2)
    return root

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    #        5
    #       / \
    #      4   8
    #     /   / \
    #    11  13  4
    #   / \      \
    #  7   2      1
    tree1 = create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    target_sum1 = 22
    result1 = solution.has_path_sum(tree1, target_sum1)
    print(f"Example 1: targetSum={target_sum1}, result={result1}")  # Expected output: True
    
    # Example 2
    #    1
    #   / \
    #  2   3
    tree2 = create_tree([1, 2, 3])
    target_sum2 = 5
    result2 = solution.has_path_sum(tree2, target_sum2)
    print(f"Example 2: targetSum={target_sum2}, result={result2}")  # Expected output: False
    
    # Example 3
    tree3 = None
    target_sum3 = 0
    result3 = solution.has_path_sum(tree3, target_sum3)
    print(f"Example 3: targetSum={target_sum3}, result={result3}")  # Expected output: False
    
    # Compare with iterative approach
    print("\nUsing iterative approach:")
    print(f"Example 1: {solution.has_path_sum_iterative(tree1, target_sum1)}")
    print(f"Example 2: {solution.has_path_sum_iterative(tree2, target_sum2)}")
    print(f"Example 3: {solution.has_path_sum_iterative(tree3, target_sum3)}")
