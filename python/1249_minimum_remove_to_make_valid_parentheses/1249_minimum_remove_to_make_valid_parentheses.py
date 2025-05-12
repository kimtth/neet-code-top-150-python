from typing import List, Optional

"""
LeetCode Minimum Remove To Make Valid Parentheses

Problem from LeetCode: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

Example 1:
    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
    Input: s = "a)b(c)d"
    Output: "ab(c)d"

Example 3:
    Input: s = "))(("
    Output: ""
    Explanation: An empty string is also valid.

Constraints:
    1 <= s.length <= 10^5
    s[i] is either'(' , ')', or lowercase English letter.
"""

class Solution:

    def min_remove_to_make_valid(self, s):
        remove_indices = set()
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    remove_indices.add(i)
                else:
                    stack.pop()
        while stack:
            remove_indices.add(stack.pop())
        result = []
        for i in range(len(s)):
            if i not in remove_indices:
                result.append(s[i])
        return ''.join(result)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "lee(t(c)o)de)"
    result1 = solution.min_remove_to_make_valid(s1)
    print(f"Example 1: '{result1}'")  # Output: "lee(t(c)o)de"
    
    # Example 2
    s2 = "a)b(c)d"
    result2 = solution.min_remove_to_make_valid(s2)
    print(f"Example 2: '{result2}'")  # Output: "ab(c)d"
    
    # Example 3
    s3 = "))(("
    result3 = solution.min_remove_to_make_valid(s3)
    print(f"Example 3: '{result3}'")  # Output: ""
