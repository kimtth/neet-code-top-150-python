from collections import defaultdict, deque
from typing import List


"""
LeetCode Word Ladder

Problem from LeetCode: https://leetcode.com/problems/word-ladder/

Description:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, so there is no valid transformation sequence.
"""

class Solution:

    def ladder_length(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Find the length of shortest transformation sequence from beginWord to endWord.
        
        Args:
            beginWord: Starting word
            endWord: Target word
            wordList: Dictionary of valid words
            
        Returns:
            int: Number of words in the shortest transformation sequence, or 0 if none exists
        """
        if endWord not in wordList:
            return 0
            
        word_len = len(beginWord)
        all_combo_dict = defaultdict(list)
        
        # Preprocess words to create generic word to actual word mapping
        for word in wordList:
            for i in range(word_len):
                # Create generic word with a wildcard character
                generic_word = word[:i] + '*' + word[i + 1:]
                all_combo_dict[generic_word].append(word)
                
        # BFS
        queue = deque([(beginWord, 1)])  # (word, level)
        visited = {beginWord: True}
        
        while queue:
            current_word, level = queue.popleft()
            
            # Try all possible transformations
            for i in range(word_len):
                # Create generic word with a wildcard
                intermediate_word = current_word[:i] + '*' + current_word[i + 1:]
                
                # Get all real words that match this generic word
                for word in all_combo_dict[intermediate_word]:
                    # If we found the end word, return the level
                    if word == endWord:
                        return level + 1
                        
                    # If we haven't visited this word yet
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                        
                # Clear the list to avoid revisiting
                all_combo_dict[intermediate_word] = []
                
        return 0
    
    def ladder_length_bidirectional(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Find the length of shortest transformation sequence using bidirectional BFS.
        
        Args:
            beginWord: Starting word
            endWord: Target word
            wordList: Dictionary of valid words
            
        Returns:
            int: Number of words in the shortest transformation sequence, or 0 if none exists
        """
        if endWord not in wordList:
            return 0
            
        # Convert wordList to a set for O(1) lookups
        word_set = set(wordList)
        
        # Queues for bidirectional BFS
        begin_queue = deque([beginWord])
        end_queue = deque([endWord])
        
        # Visited sets
        begin_visited = {beginWord: 1}  # Word -> level
        end_visited = {endWord: 1}
        
        while begin_queue and end_queue:
            # Process one level of the begin queue
            if len(begin_queue) <= len(end_queue):
                level = self._process_queue(begin_queue, begin_visited, end_visited, word_set)
                if level:
                    return level
            # Process one level of the end queue
            else:
                level = self._process_queue(end_queue, end_visited, begin_visited, word_set)
                if level:
                    return level
                    
        return 0
        
    def _process_queue(self, queue, visited, other_visited, word_set):
        """Helper function for bidirectional BFS."""
        size = len(queue)
        for _ in range(size):
            current_word = queue.popleft()
            current_level = visited[current_word]
            
            # Try changing each position
            for i in range(len(current_word)):
                # Try all 26 lowercase letters
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = current_word[:i] + c + current_word[i+1:]
                    
                    # If the word is in the other visited set, we found a path
                    if new_word in other_visited:
                        return current_level + other_visited[new_word] - 1
                        
                    if new_word in word_set and new_word not in visited:
                        visited[new_word] = current_level + 1
                        queue.append(new_word)
                        
        return None


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result1 = solution.ladder_length(beginWord1, endWord1, wordList1)
    print(f"Example 1: Length of shortest transformation sequence = {result1}")  # Expected output: 5
    
    # Example 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    result2 = solution.ladder_length(beginWord2, endWord2, wordList2)
    print(f"Example 2: Length of shortest transformation sequence = {result2}")  # Expected output: 0
    
    # Compare with bidirectional approach
    print("\nUsing bidirectional BFS:")
    result3 = solution.ladder_length_bidirectional(beginWord1, endWord1, wordList1)
    print(f"Example 1: Length of shortest transformation sequence = {result3}")  # Expected output: 5
