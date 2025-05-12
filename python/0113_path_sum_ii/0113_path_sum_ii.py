from typing import List, Optional

"""
LeetCode Path Sum II

Problem from LeetCode: https://leetcode.com/problems/path-sum-ii/

Description:
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def path_sum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Find all root-to-leaf paths with the given sum.
        
        Args:
            root: Root of the binary tree
            targetSum: Target sum to find
            
        Returns:
            List[List[int]]: All paths with the target sum
        """
        result = []
        self._dfs(root, targetSum, [], result)
        return result
    
    def _dfs(self, node: Optional[TreeNode], target_sum: int, path: List[int], result: List[List[int]]) -> None:
        """
        Helper function for depth-first search.
        
        Args:
            node: Current node
            target_sum: Remaining sum to find
            path: Current path from root to current node
            result: List to collect all valid paths
        """
        if not node:
            return
            
        # Add current node to the path
        path.append(node.val)
        
        # Check if this is a leaf node with the target sum
        if not node.left and not node.right and target_sum == node.val:
            result.append(path[:])  # Add a copy of the path
        
        # Recursively check left and right subtrees
        self._dfs(node.left, target_sum - node.val, path, result)
        self._dfs(node.right, target_sum - node.val, path, result)
        
        # Backtrack by removing the current node from path
        path.pop()
    
    def path_sum_iterative(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Iterative approach using a stack.
        
        Args:
            root: Root of the binary tree
            targetSum: Target sum to find
            
        Returns:
            List[List[int]]: All paths with the target sum
        """
        if not root:
            return []
            
        result = []
        # Stack to store (node, remaining sum, path)
        stack = [(root, targetSum - root.val, [root.val])]
        
        while stack:
            node, remain, path = stack.pop()
            
            # Check if this is a leaf node with the target sum
            if not node.left and not node.right and remain == 0:
                result.append(path)
                
            # Add right child to the stack
            if node.right:
                stack.append((node.right, remain - node.right.val, path + [node.right.val]))
                
            # Add left child to the stack
            if node.left:
                stack.append((node.left, remain - node.left.val, path + [node.left.val]))
                
        return result

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
    #   / \     / \
    #  7   2   5   1
    tree1 = create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    target_sum1 = 22
    result1 = solution.path_sum(tree1, target_sum1)
    print(f"Example 1: targetSum={target_sum1}")
    print(f"Result: {result1}")  # Expected output: [[5,4,11,2],[5,8,4,5]]
    
    # Example 2
    tree2 = create_tree([1, 2, 3])
    target_sum2 = 5
    result2 = solution.path_sum(tree2, target_sum2)
    print(f"\nExample 2: targetSum={target_sum2}")
    print(f"Result: {result2}")  # Expected output: []
    
    # Example 3
    tree3 = create_tree([1, 2])
    target_sum3 = 0
    result3 = solution.path_sum(tree3, target_sum3)
    print(f"\nExample 3: targetSum={target_sum3}")
    print(f"Result: {result3}")  # Expected output: []
    
    # Compare with iterative approach
    print("\nUsing iterative approach:")
    print(f"Example 1: {solution.path_sum_iterative(tree1, target_sum1)}")
    print(f"Example 2: {solution.path_sum_iterative(tree2, target_sum2)}")
    print(f"Example 3: {solution.path_sum_iterative(tree3, target_sum3)}")
