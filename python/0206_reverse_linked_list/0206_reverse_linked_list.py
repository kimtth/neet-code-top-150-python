from typing import List, Optional

"""
LeetCode 206. Reverse Linked List

Problem from LeetCode: https://leetcode.com/problems/reverse-linked-list/

Description:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse_list(self, head: ListNode) ->ListNode:
        """
        Reverse a singly linked list.
        
        Args:
            head: Head of the linked list
            
        Returns:
            ListNode: Head of the reversed linked list
        """
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverse_list_recursive(self, head: ListNode) ->ListNode:
        """
        Reverse a singly linked list using recursion.
        
        Args:
            head: Head of the linked list
            
        Returns:
            ListNode: Head of the reversed linked list
        """
        if head is None or head.next is None:
            return head
        new_head = self.reverse_list_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

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
    arr1 = [1, 2, 3, 4, 5]
    head1 = create_linked_list(arr1)
    print(f"Input: head = {arr1}")
    reversed_head1 = solution.reverse_list(head1)
    result1 = linked_list_to_array(reversed_head1)
    print(f"Output (iterative): {result1}")  # Expected output: [5,4,3,2,1]
    
    # Example 2
    arr2 = [1, 2]
    head2 = create_linked_list(arr2)
    print(f"\nInput: head = {arr2}")
    reversed_head2 = solution.reverse_list(head2)
    result2 = linked_list_to_array(reversed_head2)
    print(f"Output (iterative): {result2}")  # Expected output: [2,1]
    
    # Example 3
    arr3 = []
    head3 = create_linked_list(arr3)
    print(f"\nInput: head = {arr3}")
    reversed_head3 = solution.reverse_list(head3)
    result3 = linked_list_to_array(reversed_head3)
    print(f"Output (iterative): {result3}")  # Expected output: []
    
    # Test recursive solution with Example 1
    head1_rec = create_linked_list(arr1)
    reversed_head1_rec = solution.reverse_list_recursive(head1_rec)
    result1_rec = linked_list_to_array(reversed_head1_rec)
    print(f"\nOutput (recursive): {result1_rec}")  # Expected output: [5,4,3,2,1]
