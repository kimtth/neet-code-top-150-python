from typing import List


"""
LeetCode Generate Parentheses

Problem from LeetCode: https://leetcode.com/problems/generate-parentheses/

Description:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""

class Solution:

    def generate_parenthesis(self, n: int) ->List[str]:
        """
        Generate all combinations of well-formed parentheses.
        
        Args:
            n: Number of pairs of parentheses
            
        Returns:
            List[str]: All combinations of well-formed parentheses
        """
        results = []
        self._backtrack(results, '', 0, 0, n)
        return results

    def _backtrack(self, results: List[str], current: str, open_count: int,
        close_count: int, max_pairs: int) ->None:
        """
        Backtracking helper function to generate valid parentheses combinations.
        
        Args:
            results: List to collect all valid combinations
            current: Current string being built
            open_count: Number of opening parentheses used so far
            close_count: Number of closing parentheses used so far
            max_pairs: Maximum number of parentheses pairs
        """
        if len(current) == max_pairs * 2:
            results.append(current)
            return
        if open_count < max_pairs:
            self._backtrack(results, current + '(', open_count + 1,
                close_count, max_pairs)
        if close_count < open_count:
            self._backtrack(results, current + ')', open_count, close_count +
                1, max_pairs)

    def generate_parenthesis_iterative(self, n: int) -> List[str]:
        """
        Generate all combinations of well-formed parentheses using an iterative approach.
        
        Args:
            n: Number of pairs of parentheses
            
        Returns:
            List[str]: All combinations of well-formed parentheses
        """
        if n == 0:
            return []
            
        result = []
        queue = [('', 0, 0)]  # (current string, open count, close count)
        
        while queue:
            curr, open_count, close_count = queue.pop(0)
            
            if len(curr) == 2 * n:
                result.append(curr)
                continue
                
            if open_count < n:
                queue.append((curr + '(', open_count + 1, close_count))
                
            if close_count < open_count:
                queue.append((curr + ')', open_count, close_count + 1))
                
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    n1 = 3
    result1 = solution.generate_parenthesis(n1)
    print(f"Example 1 (n={n1}): {result1}")
    # Expected output: ["((()))","(()())","(())()","()(())","()()()"]
    
    # Example 2
    n2 = 1
    result2 = solution.generate_parenthesis(n2)
    print(f"Example 2 (n={n2}): {result2}")
    # Expected output: ["()"]
    
    # Additional example
    n3 = 2
    result3 = solution.generate_parenthesis(n3)
    print(f"Example 3 (n={n3}): {result3}")
    # Expected output: ["(())","()()"]
    
    # Compare with iterative implementation
    print("\nUsing iterative approach:")
    result_iter = solution.generate_parenthesis_iterative(n1)
    print(f"n={n1}: {result_iter}")
    # Should match the output of the recursive approach
