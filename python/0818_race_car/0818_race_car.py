import sys
from collections import deque


"""
LeetCode Race Car

Problem from LeetCode: https://leetcode.com/problems/race-car/

Description:
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
- position += speed
- speed *= 2

When you get an instruction 'R', your car does the following:
- If your speed is positive then speed = -1
- Otherwise speed = 1
Your position stays the same.

For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.

Example 1:
Input: target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.

Example 2:
Input: target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.

Constraints:
1 <= target <= 10^4
"""

class Solution:

    def racecar(self, target: int) ->int:
        """
        Find the minimum number of instructions needed to reach the target position.
        
        Args:
            target: The target position to reach
            
        Returns:
            int: The minimum number of instructions needed
        """
        dp = [-1] * (target + 1)
        dp[0] = 0
        for t in range(1, target + 1):
            n = t.bit_length()
            if t == (1 << n) - 1:
                dp[t] = n
                continue
            dp[t] = n + 1 + dp[(1 << n) - 1 - t]
            for m in range(n - 1):
                dp[t] = min(dp[t], n - 1 + 1 + m + 1 + dp[t - (1 << n - 1) +
                    (1 << m)])
        return dp[target]

    def racecar_bfs(self, target: int) ->int:
        """
        Find the minimum number of instructions using BFS.
        
        Args:
            target: The target position to reach
            
        Returns:
            int: The minimum number of instructions needed
        """
        queue = deque([(0, 1, 0)])
        visited = set([(0, 1)])
        while queue:
            pos, speed, instructions = queue.popleft()
            if pos == target:
                return instructions
            new_pos = pos + speed
            new_speed = speed * 2
            if (new_pos, new_speed
                ) not in visited and 0 <= new_pos <= 2 * target:
                queue.append((new_pos, new_speed, instructions + 1))
                visited.add((new_pos, new_speed))
            new_pos = pos
            new_speed = -1 if speed > 0 else 1
            if (new_pos, new_speed
                ) not in visited and 0 <= new_pos <= 2 * target:
                queue.append((new_pos, new_speed, instructions + 1))
                visited.add((new_pos, new_speed))
        return -1

    def racecar_recursive(self, target: int) ->int:
        """
        Dynamic programming with recursion and memoization.
        
        Args:
            target: The target position to reach
            
        Returns:
            int: The minimum number of instructions needed
        """
        memo = {}

        def dp(t):
            if t in memo:
                return memo[t]
            n = t.bit_length()
            if t == (1 << n) - 1:
                memo[t] = n
                return n
            memo[t] = n + 1 + dp((1 << n) - 1 - t)
            for m in range(n - 1):
                memo[t] = min(memo[t], n - 1 + 1 + m + 1 + dp(t - (1 << n -
                    1) + (1 << m)))
            return memo[t]
        return dp(target)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    target1 = 3
    result1 = solution.racecar(target1)
    print(f"Example 1: {result1}")  # Expected: 2
    
    # Example 2
    target2 = 6
    result2 = solution.racecar(target2)
    print(f"Example 2: {result2}")  # Expected: 5
