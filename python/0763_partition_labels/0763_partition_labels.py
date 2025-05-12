from typing import List


"""
LeetCode Partition Labels

Problem from LeetCode: https://leetcode.com/problems/partition-labels/

Description:
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""

class Solution:

    def partition_labels(self, s: str) ->List[int]:
        """
        Partition a string into as many parts as possible so that each letter appears in at most one part.
        
        Args:
            s: A string of lowercase English letters
            
        Returns:
            List[int]: A list of integers representing the size of each part
        """
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i
        result = []
        partition_start = 0
        partition_end = 0
        for i, char in enumerate(s):
            partition_end = max(partition_end, last_occurrence[char])
            if i == partition_end:
                result.append(partition_end - partition_start + 1)
                partition_start = i + 1
        return result

    def partitionLabels_pythonic(self, s: str) ->List[int]:
        """
        More Pythonic implementation of the solution.
        
        Args:
            s: A string of lowercase English letters
            
        Returns:
            List[int]: A list of integers representing the size of each part
        """
        last_index = {char: i for i, char in enumerate(s)}
        result = []
        start = end = 0
        for i, char in enumerate(s):
            end = max(end, last_index[char])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result

    def partitionLabels_using_sets(self, s: str) ->List[int]:
        """
        Implementation using sets to track characters in each partition.
        
        Args:
            s: A string of lowercase English letters
            
        Returns:
            List[int]: A list of integers representing the size of each part
        """
        last_pos = {char: i for i, char in enumerate(s)}
        result = []
        current_chars = set()
        start = 0
        for i, char in enumerate(s):
            current_chars.add(char)
            can_end = True
            for c in current_chars:
                if last_pos[c] > i:
                    can_end = False
                    break
            if can_end:
                result.append(i - start + 1)
                start = i + 1
                current_chars = set()
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "ababcbacadefegdehijhklij"
    result1 = solution.partition_labels(s1)
    print(f"Example 1: {result1}")  # Expected: [9, 7, 8]
    
    # Example 2
    s2 = "eccbbbbdec"
    result2 = solution.partition_labels(s2)
    print(f"Example 2: {result2}")  # Expected: [10]
