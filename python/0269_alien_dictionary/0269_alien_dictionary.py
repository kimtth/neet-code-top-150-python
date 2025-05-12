from typing import List, Dict
from collections import defaultdict


"""
LeetCode 269. Alien Dictionary

Problem from LeetCode: https://leetcode.com/problems/alien-dictionary/

Description:
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
"""

class Solution:

    def alien_order(self, words: List[str]) ->str:
        """
        Determine the order of characters in an alien alphabet given a list of sorted words.
        
        Args:
            words: List of strings sorted by the rules of the alien language
            
        Returns:
            str: The order of characters in the alien language, or "" if no valid order exists
        """
        reversed_list = defaultdict(list)
        seen = {}
        result = []
        
        # Initialize the adjacency list with all characters
        for word in words:
            for c in word:
                if c not in reversed_list:
                    reversed_list[c] = []
                    
        # Build the graph
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # Check for invalid order: if word1 is a prefix of word2, it should come before
            if len(word1) > len(word2) and word1.startswith(word2):
                return ''
                
            # Find the first differing character
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    reversed_list[word2[j]].append(word1[j])
                    break

        # DFS to check for cycles and build the result
        def dfs(c):
            if c in seen:
                return seen[c]
                
            seen[c] = False  # Mark as visiting (potential cycle)
            
            for next_char in reversed_list[c]:
                if not dfs(next_char):
                    return False
                    
            seen[c] = True   # Mark as visited
            result.append(c)
            return True
            
        # Process all characters
        for c in reversed_list:
            if c not in seen:
                if not dfs(c):
                    return ''
                    
        # Check if all characters were included
        if len(result) < len(reversed_list):
            return ''
            
        return ''.join(result)

    def alien_order_b_f_s(self, words: List[str]) ->str:
        """
        Implement the alien dictionary problem using BFS topological sort.
        
        Args:
            words: List of strings sorted by the rules of the alien language
            
        Returns:
            str: The order of characters in the alien language, or "" if no valid order exists
        """
        from collections import deque
        
        # Initialize the graph and in-degree counts
        graph = defaultdict(set)
        in_degree = {}
        
        # Add all characters to the in_degree dictionary
        for word in words:
            for c in word:
                in_degree[c] = 0
                
        # Build the graph
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # Check for invalid order
            if len(word1) > len(word2) and word1.startswith(word2):
                return ''
                
            # Find the first differing character
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    # Add directed edge: word1[j] -> word2[j]
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
                    
        # Start with characters that have no prerequisites
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        result = []
        
        # Process the queue
        while queue:
            curr = queue.popleft()
            result.append(curr)
            
            for next_char in graph[curr]:
                in_degree[next_char] -= 1
                if in_degree[next_char] == 0:
                    queue.append(next_char)
                    
        # Check if all characters were included
        if len(result) != len(in_degree):
            return ''
            
        return ''.join(result)

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    result1 = solution.alien_order(words1)
    print(f"Example 1: {result1}")  # Expected output: "wertf"
    
    # Example 2
    words2 = ["z", "x"]
    result2 = solution.alien_order(words2)
    print(f"Example 2: {result2}")  # Expected output: "zx"
    
    # Example 3
    words3 = ["z", "x", "z"]
    result3 = solution.alien_order(words3)
    print(f"Example 3: {result3}")  # Expected output: ""
    
    # Try BFS approach
    print("\nUsing BFS approach:")
    result1_bfs = solution.alien_order_b_f_s(words1)
    print(f"Example 1: {result1_bfs}")
    
    result2_bfs = solution.alien_order_b_f_s(words2)
    print(f"Example 2: {result2_bfs}")
    
    result3_bfs = solution.alien_order_b_f_s(words3)
    print(f"Example 3: {result3_bfs}")
