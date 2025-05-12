from typing import List, Optional
from collections import deque

"""
LeetCode Convert Sorted Array to Binary Search Tree

Problem from LeetCode: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Description:
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted.

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sorted_array_to_bst(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Convert a sorted array to a height-balanced binary search tree.
        Uses a recursive approach by choosing the middle element as the root.
        
        Args:
            nums: Sorted array of integers
            
        Returns:
            TreeNode: Root of the height-balanced BST
        """
        if not nums:
            return None
            
        # Find the middle element to use as the root
        mid = len(nums) // 2
        
        # Create the root node with the middle element
        root = TreeNode(nums[mid])
        
        # Recursively build the left and right subtrees
        root.left = self.sorted_array_to_bst(nums[:mid])
        root.right = self.sorted_array_to_bst(nums[mid+1:])
        
        return root
    
    def sorted_array_to_bst_optimized(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Optimized implementation that avoids creating new subarrays.
        
        Args:
            nums: Sorted array of integers
            
        Returns:
            TreeNode: Root of the height-balanced BST
        """
        def build_bst(left, right):
            if left > right:
                return None
                
            # Find the middle element
            mid = (left + right) // 2
            
            # Create the root node with the middle element
            root = TreeNode(nums[mid])
            
            # Recursively build the left and right subtrees
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            
            return root
            
        return build_bst(0, len(nums) - 1)
    
    def sorted_array_to_bst_iterative(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Iterative implementation using a queue.
        
        Args:
            nums: Sorted array of integers
            
        Returns:
            TreeNode: Root of the height-balanced BST
        """
        if not nums:
            return None
            
        # Initialize the root node
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        # Queue of (node, left bound, right bound)
        queue = deque([(root, 0, mid - 1), (root, mid + 1, len(nums) - 1)])
        
        while queue:
            parent, left, right = queue.popleft()
            
            if left <= right:
                mid = (left + right) // 2
                child = TreeNode(nums[mid])
                
                # Determine if this is a left or right child
                if nums[mid] < parent.val:
                    parent.left = child
                else:
                    parent.right = child
                    
                # Add child nodes to the queue
                queue.append((child, left, mid - 1))
                queue.append((child, mid + 1, right))
                
        return root

# Helper function to print tree in level order
def level_order_traversal(root):
    if not root:
        return []
        
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
    nums1 = [-10, -3, 0, 5, 9]
    root1 = solution.sorted_array_to_bst(nums1)
    result1 = level_order_traversal(root1)
    print(f"Example 1: {result1}")  # One of the valid outputs
    
    # Example 2
    nums2 = [1, 3]
    root2 = solution.sorted_array_to_bst(nums2)
    result2 = level_order_traversal(root2)
    print(f"Example 2: {result2}")  # One of the valid outputs
    
    # Compare with optimized implementation
    print("\nUsing optimized implementation:")
    root1_opt = solution.sorted_array_to_bst_optimized(nums1)
    result1_opt = level_order_traversal(root1_opt)
    print(f"Example 1: {result1_opt}")  # Should match the recursive approach
    
    # Compare with iterative implementation
    print("\nUsing iterative implementation:")
    root1_iter = solution.sorted_array_to_bst_iterative(nums1)
    result1_iter = level_order_traversal(root1_iter)
    print(f"Example 1: {result1_iter}")  # May have different layout but still valid
