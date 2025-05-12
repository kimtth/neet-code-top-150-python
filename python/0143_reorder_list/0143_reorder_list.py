from typing import List, Optional

"""
LeetCode Reorder List

Problem from LeetCode: https://leetcode.com/problems/reorder-list/

Description:
You are given the head of a singly linked list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorder_list(self, head: Optional[ListNode]) -> None:
        """
        Reorder the linked list by interweaving the first half with the reversed second half.
        This is done in-place with O(1) extra space.
        
        Args:
            head: Head of the linked list
        """
        if not head:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        first, second = head, prev
        while second.next:
            temp = first.next
            first.next = second
            first = temp
            temp = second.next
            second.next = first
            second = temp
    
    def reorder_list_using_stack(self, head: Optional[ListNode]) -> None:
        """
        Alternative implementation using a stack to store all nodes.
        O(n) time and O(n) space complexity.
        
        Args:
            head: Head of the linked list
        """
        if not head or not head.next:
            return
            
        # Create a stack of all nodes
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next
            
        # Reorder the list
        length = len(stack)
        current = head
        
        for i in range(length // 2):
            # Get the next node from the end
            next_end = stack.pop()
            
            # Save the next node in the original list
            next_orig = current.next
            
            # Insert the end node after the current node
            current.next = next_end
            next_end.next = next_orig
            
            # Move to the next position in the original list
            current = next_orig
            
        # Ensure the list is properly terminated
        if length % 2 == 0:
            # Even length: the last node is from the original second half
            current.next = None
        else:
            # Odd length: the last node is the middle node
            stack.pop().next = None


# Helper function to create a linked list from an array
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to an array
def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    head1 = create_linked_list([1, 2, 3, 4])
    solution.reorder_list(head1)
    print(f"Example 1: {linked_list_to_array(head1)}")  # Expected output: [1, 4, 2, 3]
    
    # Example 2
    head2 = create_linked_list([1, 2, 3, 4, 5])
    solution.reorder_list(head2)
    print(f"Example 2: {linked_list_to_array(head2)}")  # Expected output: [1, 5, 2, 4, 3]
    
    # Test using stack approach
    head3 = create_linked_list([1, 2, 3, 4])
    solution.reorder_list_using_stack(head3)
    print(f"\nUsing stack approach:")
    print(f"Example 1: {linked_list_to_array(head3)}")  # Expected output: [1, 4, 2, 3]
