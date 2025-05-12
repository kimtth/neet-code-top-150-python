from typing import List
from collections import defaultdict, deque


"""
LeetCode 210: Course Schedule II

Problem from LeetCode: https://leetcode.com/problems/course-schedule-ii/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid 
answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished 
course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished 
both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses * (numCourses - 1)
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- All the pairs [ai, bi] are distinct.
"""

class Solution:
    def find_order(self, numCourses: int, prerequisites: List[List[int]]
        ) ->List[int]:
        """
        Return the ordering of courses you should take to finish all courses.
        
        Args:
            numCourses: Number of courses (labeled from 0 to numCourses-1)
            prerequisites: List of prerequisite pairs where [a, b] means course 'a' depends on course 'b'
            
        Returns:
            List[int]: The course order to take to finish all courses, or empty list if impossible
        """
        WHITE = 1
        GRAY = 2
        BLACK = 3
        is_possible = True
        color = {}
        adj_list = defaultdict(list)
        topological_order = []
        for i in range(numCourses):
            color[i] = WHITE
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return
            color[node] = GRAY
            for neighbor in adj_list[node]:
                if color[neighbor] == WHITE:
                    dfs(neighbor)
                elif color[neighbor] == GRAY:
                    is_possible = False
                    return
            color[node] = BLACK
            topological_order.append(node)
        for i in range(numCourses):
            if color[i] == WHITE:
                dfs(i)
        if not is_possible:
            return []
        return topological_order[::-1]

    def find_order_b_f_s(self, numCourses: int, prerequisites: List[List[int]]
        ) ->List[int]:
        """
        Alternative approach using BFS (Kahn's algorithm) for topological sorting.
        
        Args:
            numCourses: Number of courses
            prerequisites: List of prerequisite pairs
            
        Returns:
            List[int]: The course order or empty list if impossible
        """
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []
        while queue:
            course = queue.popleft()
            result.append(course)
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return result if len(result) == numCourses else []


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    numCourses = 2
    prerequisites = [[1, 0]]
    result = solution.find_order(numCourses, prerequisites)
    print(result)  # Output: [0, 1]
    
    # Example 2
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result = solution.find_order(numCourses, prerequisites)
    print(result)  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]
    
    # Example 3
    numCourses = 1
    prerequisites = []
    result = solution.find_order(numCourses, prerequisites)
    print(result)  # Output: [0]
