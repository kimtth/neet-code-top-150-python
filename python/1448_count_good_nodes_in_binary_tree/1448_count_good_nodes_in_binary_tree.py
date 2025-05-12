from typing import Optional

"""
LeetCode Count Good Nodes In Binary Tree

Problem from LeetCode: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree root, a node X in the tree is named good if in the path from root 
to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
                3
               / \
              1   4
             /   / \
            3   1   5
    Input: root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Nodes in blue are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path
    Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
                3
               / 
              3   
             / \  
            4   2 
    Input: root = [3,3,null,4,2]
    Output: 3
    Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
    Input: root = [1]
    Output: 1
    Explanation: Root is considered as good.

Constraints:
    The number of nodes in the binary tree is in the range [1, 10^5].
    Each node's value is between [-10^4, 10^4].
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def good_nodes(self, root: TreeNode) -> int:
        return self.count_good_nodes(root, float('-inf'))

    def count_good_nodes(self, node: TreeNode, max_so_far: int) -> int:
        if not node:
            return 0
        count = 0
        if node.val >= max_so_far:
            count = 1
            max_so_far = node.val
        count += self.count_good_nodes(node.left, max_so_far)
        count += self.count_good_nodes(node.right, max_so_far)
        return count


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    # Example 1: [3,1,4,3,null,1,5]
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)
    root1.right.left = TreeNode(1)
    root1.right.right = TreeNode(5)
    
    solution = Solution()
    result1 = solution.good_nodes(root1)
    print(f"Example 1: {result1}")  # Output: 4
    
    # Example 2: [3,3,null,4,2]
    root2 = TreeNode(3)
    root2.left = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(2)
    
    result2 = solution.good_nodes(root2)
    print(f"Example 2: {result2}")  # Output: 3
    
    # Example 3: [1]
    root3 = TreeNode(1)
    
    result3 = solution.good_nodes(root3)
    print(f"Example 3: {result3}")  # Output: 1
