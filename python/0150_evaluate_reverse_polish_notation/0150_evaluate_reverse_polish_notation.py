from typing import List, Optional

"""
LeetCode Evaluate Reverse Polish Notation

Problem from LeetCode: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Description:
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

class Solution:
    def eval_r_p_n(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.
        
        Args:
            tokens: List of tokens in Reverse Polish Notation
            
        Returns:
            int: Result of the evaluated expression
        """
        stack = []
        for token in tokens:
            if self.is_operator(token):
                b = stack.pop()
                a = stack.pop()
                result = self.apply_operator(token, a, b)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]

    def is_operator(self, token: str) -> bool:
        """
        Check if a token is an operator.
        
        Args:
            token: Token to check
            
        Returns:
            bool: True if token is an operator, False otherwise
        """
        return token in ['+', '-', '*', '/']

    def apply_operator(self, operator: str, a: int, b: int) -> int:
        """
        Apply an arithmetic operator to two operands.
        
        Args:
            operator: Arithmetic operator (+, -, *, /)
            a: First operand
            b: Second operand
            
        Returns:
            int: Result of the operation a operator b
        """
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return int(a / b)
        else:
            raise ValueError('Invalid operator')


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    tokens1 = ["2", "1", "+", "3", "*"]
    result1 = solution.eval_r_p_n(tokens1)
    print(f"Example 1: {tokens1} -> {result1}")  # Expected output: 9
    
    # Example 2
    tokens2 = ["4", "13", "5", "/", "+"]
    result2 = solution.eval_r_p_n(tokens2)
    print(f"Example 2: {tokens2} -> {result2}")  # Expected output: 6
    
    # Example 3
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    result3 = solution.eval_r_p_n(tokens3)
    print(f"Example 3: Result = {result3}")  # Expected output: 22
    
    # Additional example with negative numbers
    tokens4 = ["4", "3", "-"]
    result4 = solution.eval_r_p_n(tokens4)
    print(f"Example 4: {tokens4} -> {result4}")  # Expected output: 1
