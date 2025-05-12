from typing import List

"""
LeetCode Text Justification

Problem from LeetCode: https://leetcode.com/problems/text-justification/

Description:
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
- The input array words contains at least one word.

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output: [
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output: [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output: [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""

class Solution:

    def full_justify(self, words: List[str], maxWidth: int) ->List[str]:
        """
        Format text such that each line has exactly maxWidth characters
        and is fully justified.
        
        Args:
            words: Array of words
            maxWidth: Width of each line
            
        Returns:
            List[str]: The fully justified text
        """
        result = []
        n = len(words)
        index = 0
        while index < n:
            total_chars = len(words[index])
            last = index + 1
            while last < n:
                if total_chars + 1 + len(words[last]) > maxWidth:
                    break
                total_chars += 1 + len(words[last])
                last += 1
            line = ''
            diff = last - index - 1
            if last == n or diff == 0:
                for i in range(index, last):
                    line += words[i]
                    if i < last - 1:
                        line += ' '
                line += ' ' * (maxWidth - len(line))
            else:
                spaces = (maxWidth - (total_chars - diff)) // diff
                extra_spaces = (maxWidth - (total_chars - diff)) % diff
                for i in range(index, last):
                    line += words[i]
                    if i < last - 1:
                        space_count = spaces + (1 if i - index <
                            extra_spaces else 0)
                        line += ' ' * space_count
            result.append(line)
            index = last
        return result

    def _format_line(self, words: List[str], start: int, end: int,
        max_width: int, is_last_line: bool) ->str:
        """
        Format a single line with justification.
        
        Args:
            words: List of all words
            start: Starting index of words for this line
            end: Ending index of words for this line (exclusive)
            max_width: Maximum line width
            is_last_line: Whether this is the last line
            
        Returns:
            str: The formatted line
        """
        total_chars = sum(len(words[i]) for i in range(start, end))
        word_count = end - start
        spaces_needed = max_width - total_chars
        if word_count == 1 or is_last_line:
            line = ' '.join(words[start:end])
            return line + ' ' * (max_width - len(line))
        gaps = word_count - 1
        spaces_per_gap = spaces_needed // gaps
        extra_spaces = spaces_needed % gaps
        line = ''
        for i in range(start, end - 1):
            line += words[i]
            if i - start < extra_spaces:
                line += ' ' * (spaces_per_gap + 1)
            else:
                line += ' ' * spaces_per_gap
        line += words[end - 1]
        return line


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    max_width1 = 16
    result1 = solution.full_justify(words1, max_width1)
    print("Example 1:")
    for line in result1:
        print(f'"{line}"')
    
    # Example 2
    words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
    max_width2 = 16
    result2 = solution.full_justify(words2, max_width2)
    print("\nExample 2:")
    for line in result2:
        print(f'"{line}"')
    
    # Example 3
    words3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    max_width3 = 20
    result3 = solution.full_justify(words3, max_width3)
    print("\nExample 3:")
    for line in result3:
        print(f'"{line}"')
