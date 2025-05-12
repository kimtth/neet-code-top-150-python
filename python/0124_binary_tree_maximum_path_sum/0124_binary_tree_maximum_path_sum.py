from typing import List, Optional

"""
LeetCode Binary Tree Maximum Path Sum

Problem from LeetCode: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Description:
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum path sum in a binary tree.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            int: Maximum path sum
        """
        # Initialize global max path sum
        self.max_sum = float('-inf')
        
        # Helper function to compute max path sum with the given node as highest point
        def max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
                
            # Compute maximum path sum for left and right subtrees
            # We take max(0, path_sum) because if path_sum < 0, we can just exclude that path
            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))
            
            # Compute the current path sum with current node as the highest point
            # This path can't be extended further up
            current_path_sum = node.val + left_gain + right_gain
            
            # Update global maximum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum sum of a path that can be extended further
            # We can only choose one path (left or right) when extending upwards
            return node.val + max(left_gain, right_gain)
            
        # Start the recursion
        max_gain(root)
        return self.max_sum
    
    def max_path_sum_iterative(self, root: Optional[TreeNode]) -> int:
        """
        Iterative approach (post-order traversal with stack).
        
        Args:
            root: Root of the binary tree
            
        Returns:
            int: Maximum path sum
        """
        # This is a more complex problem to solve iteratively
        # because we need to track both the max path sum and the max gain from each node
        # This implementation is left as a challenge for advanced users
        pass  # Implementation would go here

# Function to create a binary tree from a list (level-order traversal)
def create_tree_from_list(values):
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
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
    root1 = create_tree_from_list([1, 2, 3])
    result1 = solution.max_path_sum(root1)
    print(f"Example 1: {result1}")  # Expected output: 6
    
    # Example 2
    root2 = create_tree_from_list([-10, 9, 20, None, None, 15, 7])
    result2 = solution.max_path_sum(root2)
    print(f"Example 2: {result2}")  # Expected output: 42
    
    # Additional test case
    root3 = create_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    result3 = solution.max_path_sum(root3)
    print(f"Additional example: {result3}")  # Expected output: 48 (11->4->5->8->13)
