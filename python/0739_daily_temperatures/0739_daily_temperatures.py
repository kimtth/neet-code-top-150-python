from typing import List


"""
LeetCode Daily Temperatures

Problem from LeetCode: https://leetcode.com/problems/daily-temperatures/

Description:
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
"""

class Solution:

    def daily_temperatures(self, temperatures: List[int]) ->List[int]:
        """
        Given an array of daily temperatures, return an array where each element is the number
        of days you would have to wait until a warmer temperature.
        If there is no future day for which this is possible, put 0 instead.
        
        Args:
            temperatures: List of daily temperatures
            
        Returns:
            List[int]: List where each element is the number of days to wait for a warmer temperature
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
        return answer

    def dailyTemperatures_monotonic(self, temperatures: List[int]) ->List[int]:
        """
        Alternative implementation explicitly explaining monotonic stack technique.
        
        Args:
            temperatures: List of daily temperatures
            
        Returns:
            List[int]: List where each element is the number of days to wait for a warmer temperature
        """
        n = len(temperatures)
        result = [0] * n
        stack = []
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                result[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        return result

    def dailyTemperatures_efficient(self, temperatures: List[int]) ->List[int]:
        """
        More efficient implementation with optimized space.
        
        Args:
            temperatures: List of daily temperatures
            
        Returns:
            List[int]: List where each element is the number of days to wait for a warmer temperature
        """
        n = len(temperatures)
        answer = [0] * n
        for i in range(n - 1, -1, -1):
            next_day = i + 1
            while next_day < n and temperatures[next_day] <= temperatures[i]:
                if answer[next_day] == 0:
                    next_day = n
                else:
                    next_day += answer[next_day]
            if next_day < n:
                answer[i] = next_day - i
        return answer


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
    result1 = solution.daily_temperatures(temperatures1)
    print(f"Example 1: {result1}")  # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    
    # Example 2
    temperatures2 = [30, 40, 50, 60]
    result2 = solution.daily_temperatures(temperatures2)
    print(f"Example 2: {result2}")  # Expected: [1, 1, 1, 0]
    
    # Example 3
    temperatures3 = [30, 60, 90]
    result3 = solution.daily_temperatures(temperatures3)
    print(f"Example 3: {result3}")  # Expected: [1, 1, 0]
