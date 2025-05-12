from typing import List
from collections import Counter
import heapq


"""
LeetCode Hand Of Straights

Problem from LeetCode: https://leetcode.com/problems/hand-of-straights/

Description:
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

Constraints:
1 <= hand.length <= 10^4
0 <= hand[i] <= 10^9
1 <= groupSize <= hand.length
"""

class Solution:

    def is_n_straight_hand(self, hand: List[int], groupSize: int) ->bool:
        """
        Determine if the cards in hand can be rearranged into groupSize consecutive groups.
        
        Args:
            hand: A list of integers representing cards
            groupSize: The required size of each consecutive group
            
        Returns:
            bool: True if the cards can be arranged as required, False otherwise
        """
        if len(hand) % groupSize != 0:
            return False
        card_counts = {}
        for card in hand:
            card_counts[card] = card_counts.get(card, 0) + 1
        sorted_cards = sorted(card_counts.keys())
        while sorted_cards:
            first = sorted_cards[0]
            for i in range(groupSize):
                current_card = first + i
                if current_card not in card_counts:
                    return False
                card_counts[current_card] -= 1
                if card_counts[current_card] == 0:
                    if current_card != sorted_cards[0]:
                        del card_counts[current_card]
                    else:
                        pass
            while sorted_cards and sorted_cards[0] not in card_counts:
                sorted_cards.pop(0)
        return True

    def isNStraightHand_heap(self, hand: List[int], groupSize: int) ->bool:
        """
        Alternative implementation using a min heap.
        
        Args:
            hand: A list of integers representing cards
            groupSize: The required size of each consecutive group
            
        Returns:
            bool: True if the cards can be arranged as required, False otherwise
        """
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]
            for i in range(groupSize):
                current_card = first + i
                if current_card not in count:
                    return False
                count[current_card] -= 1
                if count[current_card] == 0:
                    if current_card != min_heap[0]:
                        del count[current_card]
                    else:
                        heapq.heappop(min_heap)
                        while min_heap and count[min_heap[0]] == 0:
                            heapq.heappop(min_heap)
        return True


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    hand1 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize1 = 3
    result1 = solution.is_n_straight_hand(hand1, groupSize1)
    print(f"Example 1: {result1}")  # Expected: True
    
    # Example 2
    hand2 = [1, 2, 3, 4, 5]
    groupSize2 = 4
    result2 = solution.is_n_straight_hand(hand2, groupSize2)
    print(f"Example 2: {result2}")  # Expected: False
