from typing import List

"""
LeetCode Word Search

Problem from LeetCode: https://leetcode.com/problems/word-search/

Description:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Check if a word exists in the board using backtracking.
        
        Args:
            board: 2D grid of characters
            word: Target word to search for
            
        Returns:
            bool: True if word exists in the grid, False otherwise
        """
        if not board or not board[0] or not word:
            return False
        
        m, n = len(board), len(board[0])
        
        # Search from each cell as starting point
        for i in range(m):
            for j in range(n):
                if self._dfs(board, i, j, word, 0):
                    return True
        
        return False
    
    def _dfs(self, board: List[List[str]], i: int, j: int, word: str, index: int) -> bool:
        """
        Helper function for DFS backtracking.
        
        Args:
            board: 2D grid
            i, j: Current position
            word: Target word
            index: Current index in the word
            
        Returns:
            bool: True if word can be formed starting from current position
        """
        # If we've matched the entire word
        if index == len(word):
            return True
        
        # Check if out of bounds or character doesn't match
        m, n = len(board), len(board[0])
        if (i < 0 or i >= m or j < 0 or j >= n or
            board[i][j] != word[index]):
            return False
        
        # Mark the cell as visited
        original = board[i][j]
        board[i][j] = '#'  # Use a special character to mark as visited
        
        # Explore in all four directions
        found = (self._dfs(board, i+1, j, word, index+1) or
                 self._dfs(board, i-1, j, word, index+1) or
                 self._dfs(board, i, j+1, word, index+1) or
                 self._dfs(board, i, j-1, word, index+1))
        
        # Restore the cell for other paths
        board[i][j] = original
        
        return found
    
    def exist_optimized(self, board: List[List[str]], word: str) -> bool:
        """
        Optimized version with early pruning and character count check.
        
        Args:
            board: 2D grid of characters
            word: Target word to search for
            
        Returns:
            bool: True if word exists in the grid, False otherwise
        """
        if not board or not board[0] or not word:
            return False
        
        # Check if the board has enough of each required character
        # This can significantly prune futile searches
        char_count = {}
        for row in board:
            for char in row:
                char_count[char] = char_count.get(char, 0) + 1
        
        # Check if word has more of any char than the board
        for char in word:
            if char not in char_count or char_count[char] <= 0:
                return False
            char_count[char] -= 1
        
        # Reset character count
        for char in word:
            char_count[char] += 1
        
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            
            if (i < 0 or i >= m or j < 0 or j >= n or
                board[i][j] != word[index]):
                return False
            
            # Mark as visited
            board[i][j] = '#'
            
            # Try all directions
            for di, dj in directions:
                if dfs(i + di, j + dj, index + 1):
                    return True
            
            # Restore the cell
            board[i][j] = word[index]
            return False
        
        # Try starting from each cell
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word1 = "ABCCED"
    result1 = solution.exist(board1, word1)
    print(f"Example 1: word='{word1}', result={result1}")  # Expected: True
    
    # Example 2
    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word2 = "SEE"
    result2 = solution.exist(board2, word2)
    print(f"Example 2: word='{word2}', result={result2}")  # Expected: True
    
    # Example 3
    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word3 = "ABCB"
    result3 = solution.exist(board3, word3)
    print(f"Example 3: word='{word3}', result={result3}")  # Expected: False
    
    # Compare with optimized approach
    print("\nUsing optimized approach:")
    board4 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]  # Create new copy since board gets modified
    print(f"Example 1: {solution.exist_optimized(board4, word1)}")  # Expected: True
