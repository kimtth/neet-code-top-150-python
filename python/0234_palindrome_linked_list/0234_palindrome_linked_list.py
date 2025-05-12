from typing import Optional


"""
LeetCode 234. Palindrome Linked List

Problem from LeetCode: https://leetcode.com/problems/palindrome-linked-list/

Description:
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true
Explanation: The list 1->2->2->1 is a palindrome.

Example 2:
Input: head = [1,2]
Output: false
Explanation: The list 1->2 is not a palindrome.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def is_palindrome(self, head: Optional[ListNode]) ->bool:
        """
        Check if a linked list is a palindrome.
        
        Args:
            head: Head of the linked list
            
        Returns:
            bool: True if the linked list is a palindrome, False otherwise
        """
        if not head or not head.next:
            return True
            
        # Find the middle of the linked list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse the second half
        second_half_head = self._reverse(slow.next)
        
        # Compare the first and second half
        p1 = head
        p2 = second_half_head
        is_palindrome = True
        while p2:
            if p1.val != p2.val:
                is_palindrome = False
                break
            p1 = p1.next
            p2 = p2.next
            
        # Restore the linked list (reverse the second half back)
        slow.next = self._reverse(second_half_head)
        
        return is_palindrome

    def _reverse(self, head: Optional[ListNode]) ->Optional[ListNode]:
        """
        Reverse a linked list.
        
        Args:
            head: Head of the linked list to reverse
            
        Returns:
            ListNode: Head of the reversed linked list
        """
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev

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

# Helper function to convert a linked list to an array (for display)
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
    arr1 = [1, 2, 2, 1]
    head1 = create_linked_list(arr1)
    result1 = solution.is_palindrome(head1)
    print(f"Example 1: head = {arr1}")
    print(f"Output: {result1}")  # Expected output: True
    
    # Example 2
    arr2 = [1, 2]
    head2 = create_linked_list(arr2)
    result2 = solution.is_palindrome(head2)
    print(f"\nExample 2: head = {arr2}")
    print(f"Output: {result2}")  # Expected output: False
    
    # Additional examples
    
    # Single element (should be True)
    arr3 = [5]
    head3 = create_linked_list(arr3)
    result3 = solution.is_palindrome(head3)
    print(f"\nSingle element: head = {arr3}")
    print(f"Output: {result3}")  # Expected output: True
    
    # Empty list (should be True)
    arr4 = []
    head4 = create_linked_list(arr4)
    result4 = solution.is_palindrome(head4)
    print(f"\nEmpty list: head = {arr4}")
    print(f"Output: {result4}")  # Expected output: True
    
    # Odd length palindrome
    arr5 = [1, 2, 3, 2, 1]
    head5 = create_linked_list(arr5)
    result5 = solution.is_palindrome(head5)
    print(f"\nOdd length palindrome: head = {arr5}")
    print(f"Output: {result5}")  # Expected output: True
