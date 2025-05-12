from typing import List
from collections import defaultdict, deque


"""
LeetCode Reconstruct Itinerary

Problem from LeetCode: https://leetcode.com/problems/reconstruct-itinerary/

Description:
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:
1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
"""

class Solution:

    def find_itinerary(self, tickets: List[List[str]]) ->List[str]:
        """
        Find the itinerary that uses all tickets starting from JFK.
        
        Args:
            tickets: List of airline tickets where each ticket is [from, to]
            
        Returns:
            List[str]: The reconstructed itinerary
        """
        graph = defaultdict(list)
        for from_airport, to_airport in tickets:
            graph[from_airport].append(to_airport)
        for destinations in graph.values():
            destinations.sort()
        itinerary = deque()

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop(0)
                dfs(next_airport)
            itinerary.appendleft(airport)
        dfs('JFK')
        return list(itinerary)

    def find_itinerary_efficient(self, tickets: List[List[str]]) ->List[str]:
        """
        Find the itinerary using a more efficient approach for removing destinations.
        
        Args:
            tickets: List of airline tickets where each ticket is [from, to]
            
        Returns:
            List[str]: The reconstructed itinerary
        """
        from heapq import heappush, heappop
        graph = defaultdict(list)
        for from_airport, to_airport in tickets:
            heappush(graph[from_airport], to_airport)
        itinerary = []

        def dfs(airport):
            while graph[airport]:
                dfs(heappop(graph[airport]))
            itinerary.append(airport)
        dfs('JFK')
        return itinerary[::-1]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    result1 = solution.find_itinerary(tickets1)
    print(f"Example 1: {result1}")  # Expected: ["JFK","MUC","LHR","SFO","SJC"]
    
    # Example 2
    tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    result2 = solution.find_itinerary(tickets2)
    print(f"Example 2: {result2}")  # Expected: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    
    # Using efficient implementation
    print("\nUsing efficient implementation:")
    result3 = solution.find_itinerary_efficient(tickets1)
    print(f"Example 1: {result3}")  # Expected: ["JFK","MUC","LHR","SFO","SJC"]
    
    result4 = solution.find_itinerary_efficient(tickets2)
    print(f"Example 2: {result4}")  # Expected: ["JFK","ATL","JFK","SFO","ATL","SFO"]
