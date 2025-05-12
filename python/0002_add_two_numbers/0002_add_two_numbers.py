from typing import List, Optional

"""
LeetCode Add Two Numbers

Problem from LeetCode: https://leetcode.com/problems/add-two-numbers/

Description:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
"""

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def add_two_numbers(self, l1: ListNode, l2: ListNode) ->ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = carry + x + y
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


if __name__ == '__main__':
    # Create example linked lists based on LeetCode sample
    # l1: 2->4->3 (represents 342)
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    # l2: 5->6->4 (represents 465)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    # Solve the problem
    solution = Solution()
    result = solution.add_two_numbers(l1, l2)
    
    # Print the result
    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(output)  # Expected output: [7, 0, 8] (represents 807)
