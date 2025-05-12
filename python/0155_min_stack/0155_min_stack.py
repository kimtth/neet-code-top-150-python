from typing import List, Optional

"""
LeetCode 155. Min Stack

Problem from LeetCode: https://leetcode.com/problems/min-stack/

Description:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""

class MinStack:


    class Node:

        def __init__(self, val, min_val, next_node=None):
            self.val = val
            self.min = min_val
            self.next = next_node

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def push(self, val: int) ->None:
        if not self.head:
            self.head = self.Node(val, val)
        else:
            self.head = self.Node(val, min(val, self.head.min), self.head)

    def pop(self) ->None:
        self.head = self.head.next

    def top(self) ->int:
        return self.head.val

    def get_min(self) ->int:
        return self.head.min


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    print("Example 1:")
    print("Operations: [\"MinStack\",\"push\",\"push\",\"push\",\"getMin\",\"pop\",\"top\",\"getMin\"]")
    print("Values: [[],[-2],[0],[-3],[],[],[],[]]")
    print("Output:")
    
    min_stack = MinStack()  # null
    print("MinStack() -> null")
    
    min_stack.push(-2)      # null
    print("push(-2) -> null")
    
    min_stack.push(0)       # null
    print("push(0) -> null")
    
    min_stack.push(-3)      # null
    print("push(-3) -> null")
    
    print(f"getMin() -> {min_stack.get_min()}")  # return -3
    
    min_stack.pop()         # null
    print("pop() -> null")
    
    print(f"top() -> {min_stack.top()}")         # return 0
    
    print(f"getMin() -> {min_stack.get_min()}")  # return -2
