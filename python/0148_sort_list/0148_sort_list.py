from typing import List, Optional

"""
LeetCode Sort List

Problem from LeetCode: https://leetcode.com/problems/sort-list/

Description:
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
"""

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sort a linked list in ascending order using merge sort.
        Time Complexity: O(n log n)
        Space Complexity: O(log n) for recursion stack
        
        Args:
            head: Head of the linked list
            
        Returns:
            ListNode: Head of the sorted linked list
        """
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        left = self.sort_list(head)
        right = self.sort_list(mid)
        return self.merge(left, right)

    def get_mid(self, head: ListNode) -> ListNode:
        """
        Find the middle node of the linked list by using slow and fast pointers.
        
        Args:
            head: Head of the linked list
            
        Returns:
            ListNode: Middle node of the linked list
        """
        prev = None
        while head and head.next:
            prev = head if prev is None else prev.next
            head = head.next.next
        mid = prev.next
        prev.next = None
        return mid

    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merge two sorted linked lists into one sorted linked list.
        
        Args:
            list1: Head of the first sorted linked list
            list2: Head of the second sorted linked list
            
        Returns:
            ListNode: Head of the merged sorted linked list
        """
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next

    def sort_list_bottom_up(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sort a linked list using bottom-up merge sort (non-recursive).
        This approach has O(1) space complexity.
        
        Args:
            head: Head of the linked list
            
        Returns:
            ListNode: Head of the sorted linked list
        """
        if not head or not head.next:
            return head
            
        # Count the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
            
        # Create a dummy node to simplify merging
        dummy = ListNode(0)
        dummy.next = head
        
        # Iterate with different step sizes (1, 2, 4, 8, ...)
        step = 1
        while step < length:
            prev = dummy
            current = dummy.next
            
            while current:
                # Split the list and get the head of the first part
                left = current
                right = self._split(left, step)
                current = self._split(right, step)
                
                # Merge the two parts and connect to the previous part
                prev = self._merge_lists(left, right, prev)
                
            step *= 2
            
        return dummy.next
    
    def _split(self, head: ListNode, step: int) -> Optional[ListNode]:
        """Helper method to split the list at a given position."""
        if not head:
            return None
            
        for i in range(1, step):
            if not head.next:
                break
            head = head.next
            
        next_head = head.next
        head.next = None
        return next_head
    
    def _merge_lists(self, left: Optional[ListNode], right: Optional[ListNode], prev: ListNode) -> ListNode:
        """Helper method to merge two lists and attach to prev."""
        current = prev
        
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
            
        current.next = left if left else right
        
        # Move to the end of the merged list
        while current.next:
            current = current.next
            
        return current


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
    head1 = create_linked_list([4, 2, 1, 3])
    result1 = solution.sort_list(head1)
    print(f"Example 1: {linked_list_to_array(result1)}")  # Expected output: [1, 2, 3, 4]
    
    # Example 2
    head2 = create_linked_list([-1, 5, 3, 4, 0])
    result2 = solution.sort_list(head2)
    print(f"Example 2: {linked_list_to_array(result2)}")  # Expected output: [-1, 0, 3, 4, 5]
    
    # Example 3
    head3 = create_linked_list([])
    result3 = solution.sort_list(head3)
    print(f"Example 3: {linked_list_to_array(result3)}")  # Expected output: []
    
    # Test with bottom-up approach
    head4 = create_linked_list([4, 2, 1, 3])
    result4 = solution.sort_list_bottom_up(head4)
    print(f"\nBottom-up approach: {linked_list_to_array(result4)}")  # Expected output: [1, 2, 3, 4]
