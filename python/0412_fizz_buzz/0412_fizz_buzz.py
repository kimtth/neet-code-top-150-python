from typing import List


"""
LeetCode Fizz Buzz

Problem from LeetCode: https://leetcode.com/problems/fizz-buzz/

Given an integer n, return a string array answer (1-indexed) where:

- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
    Input: n = 3
    Output: ["1","2","Fizz"]

Example 2:
    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]

Example 3:
    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
    1 <= n <= 10^4
"""

class Solution:

    def fizz_buzz(self, n: int) ->List[str]:
        """
        Return the string representation of numbers from 1 to n.
        
        For multiples of 3, return "Fizz" instead of the number.
        For multiples of 5, return "Buzz" instead of the number.
        For multiples of both 3 and 5, return "FizzBuzz".
        
        Args:
            n: Upper limit
            
        Returns:
            List[str]: String representations from 1 to n following the FizzBuzz rules
        """
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result

    def fizz_buzz_concatenation(self, n: int) ->List[str]:
        """
        Alternative implementation using string concatenation.
        This is more extensible if more divisors need to be added.
        
        Args:
            n: Upper limit
            
        Returns:
            List[str]: String representations from 1 to n following the FizzBuzz rules
        """
        result = []
        for i in range(1, n + 1):
            answer = ''
            if i % 3 == 0:
                answer += 'Fizz'
            if i % 5 == 0:
                answer += 'Buzz'
            if not answer:
                answer = str(i)
            result.append(answer)
        return result

    def fizz_buzz_comprehension(self, n: int) ->List[str]:
        """
        Pythonic implementation using list comprehension.
        
        Args:
            n: Upper limit
            
        Returns:
            List[str]: String representations from 1 to n following the FizzBuzz rules
        """
        return [('FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 
            'Buzz' if i % 5 == 0 else str(i)) for i in range(1, n + 1)]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: n = 3
    print("Example 1:")
    result = solution.fizz_buzz(3)
    print(f"Output: {result}")  # Expected: ["1","2","Fizz"]
    
    # Example 2: n = 5
    print("\nExample 2:")
    result = solution.fizz_buzz(5)
    print(f"Output: {result}")  # Expected: ["1","2","Fizz","4","Buzz"]
    
    # Example 3: n = 15
    print("\nExample 3:")
    result = solution.fizz_buzz(15)
    print(f"Output: {result}")  # Expected: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    
    # Test with alternative implementations
    print("\nAlternative implementations:")
    print("Concatenation approach:", solution.fizz_buzz_concatenation(15))
    print("List comprehension approach:", solution.fizz_buzz_comprehension(15))
