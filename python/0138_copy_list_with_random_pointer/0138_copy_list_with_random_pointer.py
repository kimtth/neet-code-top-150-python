from typing import Optional

"""
LeetCode Copy List with Random Pointer

Problem from LeetCode: https://leetcode.com/problems/copy-list-with-random-pointer/

Description:
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
- val: an integer representing Node.val
- random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Make a deep copy of the linked list with random pointers.
        Uses a hash map to map original nodes to their copies.
        
        Args:
            head: Head of the original linked list
            
        Returns:
            Node: Head of the copied linked list
        """
        if not head:
            return None
            
        # Dictionary to map original nodes to their copies
        old_to_new = {}
        
        # First pass: create new nodes
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
            
        # Second pass: set pointers
        current = head
        while current:
            # Set next pointer
            if current.next:
                old_to_new[current].next = old_to_new[current.next]
                
            # Set random pointer
            if current.random:
                old_to_new[current].random = old_to_new[current.random]
                
            current = current.next
            
        return old_to_new[head]
    
    def copyRandomList_one_pass(self, head: Optional[Node]) -> Optional[Node]:
        """
        Make a deep copy of the linked list with random pointers.
        Uses a slightly different approach that handles both pointers in one pass.
        
        Args:
            head: Head of the original linked list
            
        Returns:
            Node: Head of the copied linked list
        """
        if not head:
            return None
            
        old_to_new = {}
        
        def get_copied_node(node):
            """Get the copied version of a node, creating it if needed."""
            if not node:
                return None
                
            if node not in old_to_new:
                old_to_new[node] = Node(node.val)
                
            return old_to_new[node]
            
        current = head
        while current:
            # Get or create the copy of the current node
            copy = get_copied_node(current)
            
            # Set next pointer
            copy.next = get_copied_node(current.next)
            
            # Set random pointer
            copy.random = get_copied_node(current.random)
            
            current = current.next
            
        return old_to_new[head]
    
    def copyRandomList_no_extra_space(self, head: Optional[Node]) -> Optional[Node]:
        """
        Make a deep copy of the linked list with random pointers.
        Uses O(1) extra space by interweaving original and copied nodes.
        
        Args:
            head: Head of the original linked list
            
        Returns:
            Node: Head of the copied linked list
        """
        if not head:
            return None
            
        # Step 1: Create a copy of each node and insert it after the original node
        current = head
        while current:
            # Create new node
            copy = Node(current.val)
            
            # Insert copy after current
            copy.next = current.next
            current.next = copy
            
            # Move to next original node
            current = copy.next
            
        # Step 2: Set random pointers for the copy nodes
        current = head
        while current:
            # If original has a random pointer, set it for the copy
            if current.random:
                current.next.random = current.random.next
                
            # Move to next original node
            current = current.next.next
            
        # Step 3: Separate the original and copied lists
        original = head
        copy_head = head.next
        copy_current = copy_head
        
        while original:
            # Update original's next pointer
            original.next = original.next.next
            
            # Update copy's next pointer if there's more nodes
            if copy_current.next:
                copy_current.next = copy_current.next.next
                
            # Move to next nodes
            original = original.next
            copy_current = copy_current.next
            
        return copy_head

# Helper function to create a linked list from a list of [val, random_index] pairs
def create_list_from_description(description):
    if not description:
        return None
        
    # Create nodes
    nodes = [Node(val) for val, _ in description]
    
    # Connect next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        
    # Connect random pointers
    for i, (_, random_idx) in enumerate(description):
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]
            
    return nodes[0] if nodes else None

# Helper function to convert a linked list to a list of [val, random_index] pairs
def list_to_description(head):
    if not head:
        return []
        
    # Create a list of all nodes
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
        
    # Create description
    result = []
    current = head
    while current:
        # Find index of the random node
        random_idx = None
        if current.random:
            random_idx = nodes.index(current.random)
            
        result.append([current.val, random_idx])
        current = current.next
        
    return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    desc1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head1 = create_list_from_description(desc1)
    copy1 = solution.copyRandomList(head1)
    result1 = list_to_description(copy1)
    print(f"Example 1: {result1}")  # Expected output matches input
    
    # Example 2
    desc2 = [[1, 1], [2, 1]]
    head2 = create_list_from_description(desc2)
    copy2 = solution.copyRandomList(head2)
    result2 = list_to_description(copy2)
    print(f"Example 2: {result2}")  # Expected output matches input
    
    # Example 3
    desc3 = [[3, None], [3, 0], [3, None]]
    head3 = create_list_from_description(desc3)
    copy3 = solution.copyRandomList(head3)
    result3 = list_to_description(copy3)
    print(f"Example 3: {result3}")  # Expected output matches input
    
    # Compare different implementations
    print("\nUsing no extra space approach:")
    copy4 = solution.copyRandomList_no_extra_space(create_list_from_description(desc1))
    result4 = list_to_description(copy4)
    print(f"Example 1: {result4}")
