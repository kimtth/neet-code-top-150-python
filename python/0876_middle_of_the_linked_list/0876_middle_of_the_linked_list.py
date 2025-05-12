from typing import Optional


"""
LeetCode Middle of the Linked List

Problem from LeetCode: https://leetcode.com/problems/middle-of-the-linked-list/

Description:
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def middle_node(self, head: Optional[ListNode]) ->Optional[ListNode]:
        """
        Return the middle node of a linked list.
        If there are two middle nodes, return the second middle node.
        
        Args:
            head: Head of the linked list
            
        Returns:
            ListNode: The middle node of the linked list
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def middleNode_array(self, head: Optional[ListNode]) ->Optional[ListNode]:
        """
        Find the middle node using an array.
        
        Args:
            head: Head of the linked list
            
        Returns:
            ListNode: The middle node of the linked list
        """
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        return nodes[len(nodes) // 2]

    def middleNode_count(self, head: Optional[ListNode]) ->Optional[ListNode]:
        """
        Find the middle node by counting nodes.
        
        Args:
            head: Head of the linked list
            
        Returns:
            ListNode: The middle node of the linked list
        """
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        middle = count // 2
        current = head
        for _ in range(middle):
            current = current.next
        return current


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: Create the linked list [1,2,3,4,5]
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)
    
    result1 = solution.middle_node(head1)
    
    # Print the result
    print("Example 1 result:")
    output1 = []
    while result1:
        output1.append(result1.val)
        result1 = result1.next
    print(output1)  # Expected output: [3,4,5]
    
    # Example 2: Create the linked list [1,2,3,4,5,6]
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)
    head2.next.next.next.next.next = ListNode(6)
    
    result2 = solution.middle_node(head2)
    
    # Print the result
    print("Example 2 result:")
    output2 = []
    while result2:
        output2.append(result2.val)
        result2 = result2.next
    print(output2)  # Expected output: [4,5,6]
