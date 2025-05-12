from typing import List
import heapq
from collections import defaultdict


"""
LeetCode Cheapest Flights Within K Stops

Problem from LeetCode: https://leetcode.com/problems/cheapest-flights-within-k-stops/

Description:
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

Constraints:
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
"""

class Solution:

    def find_cheapest_price(self, n: int, flights: List[List[int]], src:
        int, dst: int, k: int) ->int:
        """
        Find the cheapest price from src to dst with at most k stops.
        
        Args:
            n: Number of cities (labeled from 0 to n-1)
            flights: Array of flights where flights[i] = [from_i, to_i, price_i]
            src: Source city
            dst: Destination city
            k: Maximum number of stops
            
        Returns:
            int: The cheapest price from src to dst with at most k stops, or -1 if no such route exists
        """
        costs = [float('inf')] * n
        costs[src] = 0
        for i in range(k + 1):
            temp = costs.copy()
            for u, v, cost in flights:
                if costs[u] == float('inf'):
                    continue
                if temp[v] > costs[u] + cost:
                    temp[v] = costs[u] + cost
            costs = temp
        return costs[dst] if costs[dst] != float('inf') else -1

    def findCheapestPrice_dijkstra(self, n: int, flights: List[List[int]],
        src: int, dst: int, k: int) ->int:
        """
        Alternative implementation using Dijkstra's algorithm with a priority queue.
        
        Args:
            n: Number of cities (labeled from 0 to n-1)
            flights: Array of flights where flights[i] = [from_i, to_i, price_i]
            src: Source city
            dst: Destination city
            k: Maximum number of stops
            
        Returns:
            int: The cheapest price from src to dst with at most k stops, or -1 if no such route exists
        """
        graph = defaultdict(list)
        for from_city, to_city, price in flights:
            graph[from_city].append((to_city, price))
        heap = [(0, src, 0)]
        visited = {}
        while heap:
            price, city, stops = heapq.heappop(heap)
            if city == dst:
                return price
            if stops > k or (city, stops) in visited and visited[city, stops
                ] < price:
                continue
            visited[city, stops] = price
            for neighbor, next_price in graph[city]:
                heapq.heappush(heap, (price + next_price, neighbor, stops + 1))
        return -1

    def findCheapestPrice_bfs(self, n: int, flights: List[List[int]], src:
        int, dst: int, k: int) ->int:
        """
        Implementation using BFS to explore all paths with at most k stops.
        
        Args:
            n: Number of cities (labeled from 0 to n-1)
            flights: Array of flights where flights[i] = [from_i, to_i, price_i]
            src: Source city
            dst: Destination city
            k: Maximum number of stops
            
        Returns:
            int: The cheapest price from src to dst with at most k stops, or -1 if no such route exists
        """
        graph = defaultdict(list)
        for from_city, to_city, price in flights:
            graph[from_city].append((to_city, price))
        queue = [(src, 0, 0)]
        min_cost = float('inf')
        while queue:
            city, cost, stops = queue.pop(0)
            if city == dst:
                min_cost = min(min_cost, cost)
                continue
            if stops > k or cost >= min_cost:
                continue
            for neighbor, price in graph[city]:
                queue.append((neighbor, cost + price, stops + 1))
        return min_cost if min_cost != float('inf') else -1


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    n1 = 4
    flights1 = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src1 = 0
    dst1 = 3
    k1 = 1
    result1 = solution.find_cheapest_price(n1, flights1, src1, dst1, k1)
    print(f"Example 1: {result1}")  # Expected: 700
    
    # Example 2
    n2 = 3
    flights2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src2 = 0
    dst2 = 2
    k2 = 1
    result2 = solution.find_cheapest_price(n2, flights2, src2, dst2, k2)
    print(f"Example 2: {result2}")  # Expected: 200
    
    # Example 3
    n3 = 3
    flights3 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src3 = 0
    dst3 = 2
    k3 = 0
    result3 = solution.find_cheapest_price(n3, flights3, src3, dst3, k3)
    print(f"Example 3: {result3}")  # Expected: 500
