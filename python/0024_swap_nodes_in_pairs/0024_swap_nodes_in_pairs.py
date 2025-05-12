from typing import Optional

"""
LeetCode Swap Nodes in Pairs

Problem from LeetCode: https://leetcode.com/problems/swap-nodes-in-pairs/

Description:
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap every two adjacent nodes in a linked list.
        
        Args:
            head: Head of the linked list
            
        Returns:
            ListNode: Head of the modified linked list with swapped pairs
        """
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Traverse the list and swap adjacent nodes
        while current.next and current.next.next:
            # Nodes to be swapped
            first = current.next
            second = current.next.next
            
            # Perform the swap
            first.next = second.next
            second.next = first
            current.next = second
            
            # Move to the next pair
            current = first
        
        return dummy.next
    
    def swap_pairs_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap every two adjacent nodes using a recursive approach.
        
        Args:
            head: Head of the linked list
            
        Returns:
            ListNode: Head of the modified linked list with swapped pairs
        """
        # Base case: less than two nodes
        if not head or not head.next:
            return head
        
        # Nodes to be swapped
        first = head
        second = head.next
        
        # Swap the nodes
        first.next = self.swap_pairs_recursive(second.next)
        second.next = first
        
        # Return new head (which is the second node)
        return second

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
    result1 = solution.swap_pairs(head1)
    print(f"Example 1: Result={linked_list_to_array(result1)}")  # Expected: [2,1,4,3]
    
    # Example 2
    head2 = create_linked_list([])
    result2 = solution.swap_pairs(head2)
    print(f"Example 2: Result={linked_list_to_array(result2)}")  # Expected: []
    
    # Example 3
    head3 = create_linked_list([1])
    result3 = solution.swap_pairs(head3)
    print(f"Example 3: Result={linked_list_to_array(result3)}")  # Expected: [1]
    
    # Test recursive approach
    head4 = create_linked_list([1, 2, 3, 4, 5])
    result4 = solution.swap_pairs_recursive(head4)
    print(f"Recursive approach: Result={linked_list_to_array(result4)}")  # Expected: [2,1,4,3,5]
