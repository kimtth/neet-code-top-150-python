from typing import List, Optional

"""
LeetCode Linked List Cycle

Problem from LeetCode: https://leetcode.com/problems/linked-list-cycle/

Description:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Determine if a linked list has a cycle using Floyd's Tortoise and Hare algorithm.
        
        Args:
            head: Head of the linked list
            
        Returns:
            bool: True if the linked list has a cycle, False otherwise
        """
        if not head:
            return False
        slow = head
        fast = head.next
        while slow and fast:
            if not fast or not fast.next:
                return False
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
    
    def has_cycle_hashset(self, head: Optional[ListNode]) -> bool:
        """
        Determine if a linked list has a cycle using a hash set to track visited nodes.
        O(n) time and space complexity.
        
        Args:
            head: Head of the linked list
            
        Returns:
            bool: True if the linked list has a cycle, False otherwise
        """
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
            
        return False


# Helper function to create a linked list with a cycle
def create_cyclic_linked_list(arr, pos):
    if not arr:
        return None
        
    head = ListNode(arr[0])
    current = head
    nodes = [head]
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
        
    # Create cycle if pos is valid
    if pos >= 0 and pos < len(nodes):
        current.next = nodes[pos]
        
    return head

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    head1 = create_cyclic_linked_list([3, 2, 0, -4], 1)
    result1 = solution.has_cycle(head1)
    print(f"Example 1: {result1}")  # Expected output: True
    
    # Example 2
    head2 = create_cyclic_linked_list([1, 2], 0)
    result2 = solution.has_cycle(head2)
    print(f"Example 2: {result2}")  # Expected output: True
    
    # Example 3
    head3 = create_cyclic_linked_list([1], -1)
    result3 = solution.has_cycle(head3)
    print(f"Example 3: {result3}")  # Expected output: False
    
    # Compare with hash set approach
    print("\nUsing hash set approach:")
    head4 = create_cyclic_linked_list([3, 2, 0, -4], 1)
    result4 = solution.has_cycle_hashset(head4)
    print(f"Example 1: {result4}")  # Expected output: True
