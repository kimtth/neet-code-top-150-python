from typing import List, Optional

"""
LeetCode Max Stack

Problem from LeetCode: https://leetcode.com/problems/max-stack/

Description:
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:
- MaxStack() Initializes the stack object.
- void push(int x) Pushes element x onto the stack.
- int pop() Removes the element on top of the stack and returns it.
- int top() Gets the element on the top of the stack without removing it.
- int peekMax() Retrieves the maximum element in the stack without removing it.
- int popMax() Retrieves the maximum element in the stack and removes it. If there are multiple instances of the maximum, only remove the top-most one.

Example 1:
Input:
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output:
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation:
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack decreased, and the top is now the element 1.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack is now 5.
stk.top();     // return 5, [5] the stack did not change.
"""

class MaxStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []

    def push(self, x: int) ->None:
        """
        Push element x onto stack.
        
        Args:
            x: The element to push
        """
        max_val = x if not self.max_stack else max(self.max_stack[-1], x)
        self.stack.append(x)
        self.max_stack.append(max_val)

    def pop(self) ->int:
        """
        Remove the top element of the stack and return it.
        
        Returns:
            int: The top element of the stack
        """
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) ->int:
        """
        Get the top element of the stack.
        
        Returns:
            int: The top element of the stack
        """
        return self.stack[-1]

    def peek_max(self) ->int:
        """
        Retrieve the maximum element in the stack.
        
        Returns:
            int: The maximum element in the stack
        """
        return self.max_stack[-1]

    def pop_max(self) ->int:
        """
        Remove the maximum element in the stack and return it.
        
        Returns:
            int: The maximum element in the stack
        """
        max_val = self.peek_max()
        buffer = []
        while self.top() != max_val:
            buffer.append(self.pop())
        self.pop()
        while buffer:
            self.push(buffer.pop())
        return max_val


class MaxStackEfficient:


    class Node:

        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        """
        Initialize your data structure here.
        This implementation uses a doubly linked list and a dictionary for O(1) operations.
        """
        self.head = self.Node(0)
        self.tail = self.Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.val_to_nodes = {}

    def _add_node(self, node):
        """Add a node right before the tail."""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def _remove_node(self, node):
        """Remove a node from the doubly linked list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def push(self, x: int) ->None:
        """Push element x onto stack."""
        node = self.Node(x)
        self._add_node(node)
        if x not in self.val_to_nodes:
            self.val_to_nodes[x] = []
        self.val_to_nodes[x].append(node)

    def pop(self) ->int:
        """Remove the top element of the stack and return it."""
        if self.head.next == self.tail:
            return -1
        node = self.tail.prev
        self._remove_node(node)
        self.val_to_nodes[node.val].remove(node)
        if not self.val_to_nodes[node.val]:
            del self.val_to_nodes[node.val]
        return node.val

    def top(self) ->int:
        """Get the top element of the stack."""
        if self.head.next == self.tail:
            return -1
        return self.tail.prev.val

    def peek_max(self) ->int:
        """Retrieve the maximum element in the stack."""
        if not self.val_to_nodes:
            return -1
        return max(self.val_to_nodes.keys())

    def pop_max(self) ->int:
        """Remove the maximum element in the stack and return it."""
        if not self.val_to_nodes:
            return -1
        max_val = max(self.val_to_nodes.keys())
        node = self.val_to_nodes[max_val][-1]
        self._remove_node(node)
        self.val_to_nodes[max_val].remove(node)
        if not self.val_to_nodes[max_val]:
            del self.val_to_nodes[max_val]
        return max_val


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    max_stack = MaxStack()
    
    # Push elements
    max_stack.push(5)
    max_stack.push(1)
    max_stack.push(5)
    
    # Test operations
    print("Top element:", max_stack.top())  # Expected: 5
    print("Pop max element:", max_stack.pop_max())  # Expected: 5
    print("Top element after popMax:", max_stack.top())  # Expected: 1
    print("Peek max element:", max_stack.peek_max())  # Expected: 5
    print("Pop element:", max_stack.pop())  # Expected: 1
    print("Top element after pop:", max_stack.top())  # Expected: 5
    
    # Test the efficient implementation
    print("\nTesting efficient implementation:")
    max_stack_efficient = MaxStackEfficient()
    
    # Push elements
    max_stack_efficient.push(5)
    max_stack_efficient.push(1)
    max_stack_efficient.push(5)
    
    # Test operations
    print("Top element:", max_stack_efficient.top())  # Expected: 5
    print("Pop max element:", max_stack_efficient.pop_max())  # Expected: 5
    print("Top element after popMax:", max_stack_efficient.top())  # Expected: 1
    print("Peek max element:", max_stack_efficient.peek_max())  # Expected: 5
    print("Pop element:", max_stack_efficient.pop())  # Expected: 1
    print("Top element after pop:", max_stack_efficient.top())  # Expected: 5
