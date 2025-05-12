from typing import List, Optional

"""
LeetCode 277. Find the Celebrity

Problem from LeetCode: https://leetcode.com/problems/find-the-celebrity/

Description:
Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. 
The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions 
like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) 
by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). 
There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. 
If there is no celebrity, return -1.

Example 1:
Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:
Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.

Constraints:
- n == graph.length
- n == graph[i].length
- 2 <= n <= 100
- graph[i][j] is 0 or 1.
- graph[i][i] == 1
"""

# Mock implementation of the knows API
def knows(a, b):
    """
    Mock implementation of the knows API for testing.
    In a real environment, this would be provided by the system.
    
    For example 1, we're using:
    graph = [
        [1,1,0],  # Person 0 knows 0 (themself) and 1, but not 2
        [0,1,0],  # Person 1 knows only themself
        [1,1,1]   # Person 2 knows 0, 1, and themself
    ]
    
    Args:
        a: Person asking (knows a?)
        b: Person being asked about (does a know b?)
        
    Returns:
        bool: Whether person a knows person b
    """
    # In a real scenario, this function would be provided
    # This is a mock implementation for testing purposes
    graph = [
        [1, 1, 0],  # Person 0 knows 0 (themself) and 1, but not 2
        [0, 1, 0],  # Person 1 knows only themself
        [1, 1, 1]   # Person 2 knows 0, 1, and themself
    ]
    return graph[a][b] == 1

class Solution:

    def find_celebrity(self, n: int) ->int:
        """
        Find the celebrity in a group of n people.
        
        A celebrity is defined as:
        1. Doesn't know anyone
        2. Everyone knows them
        
        Args:
            n: Number of people
            
        Returns:
            int: The celebrity's ID or -1 if no celebrity exists
        """
        self.num_of_people = n
        celeb_candidate = 0
        for i in range(n):
            if knows(celeb_candidate, i):
                celeb_candidate = i
        if self.is_celebrity(celeb_candidate):
            return celeb_candidate
        return -1

    def is_celebrity(self, i: int) ->bool:
        """
        Verify if person i is a celebrity.
        
        Args:
            i: Person ID to check
            
        Returns:
            bool: True if i is a celebrity, False otherwise
        """
        for j in range(self.num_of_people):
            if i == j:
                continue
            if knows(i, j) or not knows(j, i):
                return False
        return True

    def find_celebrity_optimized(self, n: int) ->int:
        """
        Find the celebrity using fewer API calls.
        
        Args:
            n: Number of people
            
        Returns:
            int: The celebrity's ID or -1 if no celebrity exists
        """
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return -1
        return candidate


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    n1 = 3  # 3 people in the graph
    result1 = solution.find_celebrity(n1)
    print(f"Example 1: n = {n1}, celebrity = {result1}")  # Expected output: 1
    
    # Example with optimized approach
    result2 = solution.find_celebrity_optimized(n1)
    print(f"Example 1 (optimized): n = {n1}, celebrity = {result2}")  # Expected output: 1
