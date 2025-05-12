from typing import List


"""
LeetCode 212. Word Search II

Problem from LeetCode: https://leetcode.com/problems/word-search-ii/

Description:
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All the strings of words are unique.
"""

class TrieNode:
    """Trie node for efficient word lookup."""

    def __init__(self):
        """Initialize a node with empty children and no word."""
        self.children = {}
        self.word = None


class Solution:

    def find_words(self, board: List[List[str]], words: List[str]) ->List[str]:
        """
        Find all words from the dictionary that can be formed in the board.
        Words can be constructed from adjacent cells (horizontally or vertically).
        
        Args:
            board: 2D board of characters
            words: Dictionary of words to search for
            
        Returns:
            List[str]: All words found in the board
        """
        # Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for letter in word:
                if letter not in node.children:
                    node.children[letter] = TrieNode()
                node = node.children[letter]
            node.word = word
            
        results = []
        self.board = board
        
        # Search words starting from each cell
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in root.children:
                    self.backtracking(row, col, root, results)
                    
        return results

    def backtracking(self, row: int, col: int, parent: TrieNode, results: List[str]) ->None:
        """
        Backtracking algorithm to find all words starting from a specific cell.
        
        Args:
            row, col: Current cell coordinates
            parent: Parent node in the Trie
            results: List to store the found words
        """
        letter = self.board[row][col]
        curr_node = parent.children[letter]
        
        # Found a word
        if curr_node.word:
            results.append(curr_node.word)
            curr_node.word = None  # Avoid duplicates
            
        # Mark the cell as visited
        self.board[row][col] = '#'
        
        # Explore neighbors
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < len(self.board) and 
                0 <= new_col < len(self.board[0]) and 
                self.board[new_row][new_col] in curr_node.children):
                self.backtracking(new_row, new_col, curr_node, results)
                
        # Restore the cell
        self.board[row][col] = letter
        
        # Optimization: Remove exhausted branches
        if not curr_node.children:
            parent.children.pop(letter)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    board1 = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words1 = ["oath","pea","eat","rain"]
    result1 = solution.find_words(board1, words1)
    
    print("Example 1:")
    print(f"Board: {board1}")
    print(f"Words: {words1}")
    print(f"Output: {result1}")  # Expected output: ["eat","oath"]
    
    # Example 2
    board2 = [
        ["a","b"],
        ["c","d"]
    ]
    words2 = ["abcb"]
    result2 = solution.find_words(board2, words2)
    
    print("\nExample 2:")
    print(f"Board: {board2}")
    print(f"Words: {words2}")
    print(f"Output: {result2}")  # Expected output: []
    
    # Additional test case with overlapping words
    board3 = [
        ["a","b","c"],
        ["a","e","d"],
        ["a","f","g"]
    ]
    words3 = ["abcdefg", "gfedcba", "abc", "aaa", "aea", "afa"]
    result3 = solution.find_words(board3, words3)
    
    print("\nAdditional example:")
    print(f"Board: {board3}")
    print(f"Words: {words3}")
    print(f"Output: {result3}")
