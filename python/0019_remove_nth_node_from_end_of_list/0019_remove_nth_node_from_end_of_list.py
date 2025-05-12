from typing import List, Optional

"""
LeetCode Remove Nth Node From End of List

Problem from LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Description:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Explanation: After removing the second node from the end, the linked list becomes [1,2,3,5].

Example 2:
Input: head = [1], n = 1
Output: []
Explanation: After removing the first node from the end, the linked list becomes empty.

Example 3:
Input: head = [1,2], n = 1
Output: [1]
Explanation: After removing the first node from the end, the linked list becomes [1].
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the linked list.
        Uses a two-pointer approach to find the node to remove in a single pass.
        
        Args:
            head: Head of the linked list
            n: Position from the end to remove (1-indexed)
            
        Returns:
            ListNode: Head of the modified linked list
        """
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers
        first = dummy
        second = dummy
        
        # Advance first pointer by n+1 steps
        for i in range(n + 1):
            if not first:
                return None  # Invalid n (too large)
            first = first.next
            
        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next
            
        # Remove the nth node from the end
        second.next = second.next.next
        
        return dummy.next
    
    def remove_nth_from_end_two_pass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end using a two-pass approach.
        First pass counts the length, second pass finds the node to remove.
        
        Args:
            head: Head of the linked list
            n: Position from the end to remove (1-indexed)
            
        Returns:
            ListNode: Head of the modified linked list
        """
        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        
        # First pass: count the length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
            
        # Second pass: find the node before the one to remove
        position = length - n
        current = dummy
        for i in range(position):
            current = current.next
            
        # Remove the nth node from the end
        current.next = current.next.next
        
        return dummy.next

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
    head1 = create_linked_list([1, 2, 3, 4, 5])
    n1 = 2
    result1 = solution.remove_nth_from_end(head1, n1)
    print(f"Example 1: n={n1}, Result={linked_list_to_array(result1)}")  # Expected: [1,2,3,5]
    
    # Example 2
    head2 = create_linked_list([1])
    n2 = 1
    result2 = solution.remove_nth_from_end(head2, n2)
    print(f"Example 2: n={n2}, Result={linked_list_to_array(result2)}")  # Expected: []
    
    # Example 3
    head3 = create_linked_list([1, 2])
    n3 = 1
    result3 = solution.remove_nth_from_end(head3, n3)
    print(f"Example 3: n={n3}, Result={linked_list_to_array(result3)}")  # Expected: [1]
    
    # Compare with two-pass approach
    head4 = create_linked_list([1, 2, 3, 4, 5])
    result4 = solution.remove_nth_from_end_two_pass(head4, 2)
    print(f"Two-pass approach: Result={linked_list_to_array(result4)}")  # Expected: [1,2,3,5]
