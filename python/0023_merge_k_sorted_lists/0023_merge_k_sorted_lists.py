from typing import List, Optional
import heapq


"""
LeetCode Merge k Sorted Lists

Problem from LeetCode: https://leetcode.com/problems/merge-k-sorted-lists/

Description:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted linked list.
        Uses a min-heap approach for optimal performance.
        
        Args:
            lists: Array of k sorted linked lists
            
        Returns:
            ListNode: Head of the merged sorted linked list
        """
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Priority queue to keep track of the smallest elements
        min_heap = []
        
        # Add the head of each list to the min heap
        for i, head in enumerate(lists):
            if head:
                # Use list index as a tie-breaker to avoid comparing ListNode objects
                heapq.heappush(min_heap, (head.val, i, head))
        
        # Process the heap until it's empty
        while min_heap:
            # Get the node with the smallest value
            val, i, node = heapq.heappop(min_heap)
            
            # Add the node to the merged list
            current.next = node
            current = current.next
            
            # If there are more nodes in this list, add the next one to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next
    
    def merge_k_lists_divide_conquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists using divide and conquer approach.
        
        Args:
            lists: Array of k sorted linked lists
            
        Returns:
            ListNode: Head of the merged sorted linked list
        """
        if not lists:
            return None
        
        # Helper function to merge two sorted lists
        def merge_two_lists(l1, l2):
            dummy = ListNode(0)
            current = dummy
            
            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            
            current.next = l1 if l1 else l2
            return dummy.next
        
        # Divide and conquer
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.merge_k_lists_divide_conquer(lists[:mid])
        right = self.merge_k_lists_divide_conquer(lists[mid:])
        
        return merge_two_lists(left, right)

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
    lists1 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    result1 = solution.merge_k_lists(lists1)
    print(f"Example 1: Result={linked_list_to_array(result1)}")
    # Expected output: [1, 1, 2, 3, 4, 4, 5, 6]
    
    # Example 2
    lists2 = []
    result2 = solution.merge_k_lists(lists2)
    print(f"Example 2: Result={linked_list_to_array(result2)}")
    # Expected output: []
    
    # Example 3
    lists3 = [create_linked_list([])]
    result3 = solution.merge_k_lists(lists3)
    print(f"Example 3: Result={linked_list_to_array(result3)}")
    # Expected output: []
    
    # Compare with divide and conquer approach
    lists4 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    result4 = solution.merge_k_lists_divide_conquer(lists4)
    print(f"Divide & Conquer approach: Result={linked_list_to_array(result4)}")
    # Expected output: [1, 1, 2, 3, 4, 4, 5, 6]
