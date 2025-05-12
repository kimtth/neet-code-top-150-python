from typing import List, Optional

"""
LeetCode Merge Two Sorted Lists

Problem from LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/

Description:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into a single sorted linked list.
        
        Args:
            list1: Head of first sorted linked list
            list2: Head of second sorted linked list
            
        Returns:
            ListNode: Head of merged sorted linked list
        """
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Compare nodes from both lists and merge them in order
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach the remaining nodes from either list
        current.next = list1 if list1 else list2
        
        return dummy.next
    
    def merge_two_lists_recursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists using a recursive approach.
        
        Args:
            list1: Head of first sorted linked list
            list2: Head of second sorted linked list
            
        Returns:
            ListNode: Head of merged sorted linked list
        """
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Compare values and recursively merge
        if list1.val <= list2.val:
            list1.next = self.merge_two_lists_recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_two_lists_recursive(list1, list2.next)
            return list2

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
    list1_1 = create_linked_list([1, 2, 4])
    list2_1 = create_linked_list([1, 3, 4])
    result1 = solution.merge_two_lists(list1_1, list2_1)
    print(f"Example 1: Result={linked_list_to_array(result1)}")  # Expected: [1,1,2,3,4,4]
    
    # Example 2
    list1_2 = create_linked_list([])
    list2_2 = create_linked_list([])
    result2 = solution.merge_two_lists(list1_2, list2_2)
    print(f"Example 2: Result={linked_list_to_array(result2)}")  # Expected: []
    
    # Example 3
    list1_3 = create_linked_list([])
    list2_3 = create_linked_list([0])
    result3 = solution.merge_two_lists(list1_3, list2_3)
    print(f"Example 3: Result={linked_list_to_array(result3)}")  # Expected: [0]
    
    # Test recursive approach
    list1_4 = create_linked_list([1, 2, 4])
    list2_4 = create_linked_list([1, 3, 4])
    result4 = solution.merge_two_lists_recursive(list1_4, list2_4)
    print(f"Recursive approach: Result={linked_list_to_array(result4)}")  # Expected: [1,1,2,3,4,4]
