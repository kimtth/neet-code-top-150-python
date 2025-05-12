from typing import Optional

"""
LeetCode Reverse Nodes in k-Group

Problem from LeetCode: https://leetcode.com/problems/reverse-nodes-in-k-group/

Description:
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:
Input: head = [1], k = 1
Output: [1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse nodes in k-group in a linked list.
        
        Args:
            head: Head of the linked list
            k: Number of nodes to reverse at a time
            
        Returns:
            ListNode: Head of the modified linked list with k-groups reversed
        """
        # Check if we need to reverse (base case for recursion)
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
            
        # If we don't have k nodes, return the head without reversing
        if count < k:
            return head
            
        # Reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        # Connect the reversed group with the rest of the list
        # head is now the last node of the reversed group
        head.next = self.reverse_k_group(curr, k)
        
        # prev is now the first node of the reversed group (new head)
        return prev
    
    def reverse_k_group_iterative(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Iterative approach to reverse nodes in k-group.
        
        Args:
            head: Head of the linked list
            k: Number of nodes to reverse at a time
            
        Returns:
            ListNode: Head of the modified linked list with k-groups reversed
        """
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # Check if we have k nodes left
            kth = self._get_kth(group_prev, k)
            if not kth:
                break
                
            group_next = kth.next
            
            # Reverse the group
            prev, curr = group_next, group_prev.next
            for _ in range(k):
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
                
            # Connect with the rest of the list
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
            
        return dummy.next
        
    def _get_kth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        """Helper function to get the kth node from current."""
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

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
    k1 = 2
    result1 = solution.reverse_k_group(head1, k1)
    print(f"Example 1: k={k1}, Result={linked_list_to_array(result1)}")  # Expected: [2,1,4,3,5]
    
    # Example 2
    head2 = create_linked_list([1, 2, 3, 4, 5])
    k2 = 3
    result2 = solution.reverse_k_group(head2, k2)
    print(f"Example 2: k={k2}, Result={linked_list_to_array(result2)}")  # Expected: [3,2,1,4,5]
    
    # Example 3
    head3 = create_linked_list([1, 2, 3, 4, 5])
    k3 = 1
    result3 = solution.reverse_k_group(head3, k3)
    print(f"Example 3: k={k3}, Result={linked_list_to_array(result3)}")  # Expected: [1,2,3,4,5]
    
    # Example 4
    head4 = create_linked_list([1])
    k4 = 1
    result4 = solution.reverse_k_group(head4, k4)
    print(f"Example 4: k={k4}, Result={linked_list_to_array(result4)}")  # Expected: [1]
    
    # Test iterative approach
    head5 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    k5 = 3
    result5 = solution.reverse_k_group_iterative(head5, k5)
    print(f"Iterative approach: k={k5}, Result={linked_list_to_array(result5)}")  # Expected: [3,2,1,6,5,4,7,8]
