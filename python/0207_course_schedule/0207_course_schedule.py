from typing import List
from collections import defaultdict, deque


"""
LeetCode Course Schedule

Problem from LeetCode: https://leetcode.com/problems/course-schedule/

Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

class Solution:

    def can_finish(self, numCourses: int, prerequisites: List[List[int]]
        ) ->bool:
        """
        Determine if it's possible to finish all courses given the prerequisites.
        
        Args:
            numCourses: Number of courses (labeled from 0 to numCourses-1)
            prerequisites: List of prerequisite pairs where [a, b] means course a depends on course b
            
        Returns:
            bool: True if all courses can be finished, False otherwise
        """
        course_graph = defaultdict(list)
        for course, prereq in prerequisites:
            course_graph[prereq].append(course)
        visited = set()

        def dfs(course):
            """
            Depth-first search to detect cycles in the course dependency graph.
            
            Args:
                course: The current course to check
                
            Returns:
                bool: True if no cycle is detected, False otherwise
            """
            if course in visited:
                return False
            if not course_graph[course]:
                return True
            visited.add(course)
            for next_course in course_graph[course]:
                if not dfs(next_course):
                    return False
            visited.remove(course)
            course_graph[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

    def can_finish_topological(self, numCourses: int, prerequisites: List[
        List[int]]) ->bool:
        """
        Alternative approach using topological sort to detect if a valid ordering exists.
        
        Args:
            numCourses: Number of courses
            prerequisites: List of prerequisite pairs
            
        Returns:
            bool: True if all courses can be finished, False otherwise
        """
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        queue = deque([c for c in range(numCourses) if in_degree[c] == 0])
        count = 0
        while queue:
            current = queue.popleft()
            count += 1
            for next_course in graph[current]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return count == numCourses

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    result1 = solution.can_finish(numCourses1, prerequisites1)
    print(f"Example 1: {result1}")  # Expected output: True
    
    # Example 2
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    result2 = solution.can_finish(numCourses2, prerequisites2)
    print(f"Example 2: {result2}")  # Expected output: False
