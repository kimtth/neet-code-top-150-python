from typing import List
import random


"""
LeetCode Insert Delete GetRandom O(1)

Problem from LeetCode: https://leetcode.com/problems/insert-delete-getrandom-o1/

Description:
Implement the RandomizedSet class:
- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Constraints:
-2^31 <= val <= 2^31 - 1
At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""

class RandomizedSet:
    """
    A data structure that supports insert, remove, and getRandom operations in O(1) time.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Dictionary to store val -> index mapping for O(1) lookup
        self.val_to_idx = {}
        # List to store values for O(1) random access
        self.values = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        
        Args:
            val: Value to insert
            
        Returns:
            bool: True if the value was not present, False otherwise
        """
        if val in self.val_to_idx:
            return False
        
        # Add value to the end of the list
        self.values.append(val)
        # Store the index in the dictionary
        self.val_to_idx[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        
        Args:
            val: Value to remove
            
        Returns:
            bool: True if the value was present, False otherwise
        """
        if val not in self.val_to_idx:
            return False
        
        # Get the index of the value to remove
        idx = self.val_to_idx[val]
        last_val = self.values[-1]
        
        # Move the last element to the position of the element to remove
        self.values[idx] = last_val
        self.val_to_idx[last_val] = idx
        
        # Remove the last element and the value from the dictionary
        self.values.pop()
        del self.val_to_idx[val]
        
        return True

    def get_random(self) -> int:
        """
        Get a random element from the set.
        
        Returns:
            int: A random element from the set
        """
        return random.choice(self.values)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    randomizedSet = RandomizedSet()
    
    # Test the operations
    print(randomizedSet.insert(1))   # Returns true as 1 was inserted successfully
    print(randomizedSet.remove(2))   # Returns false as 2 does not exist in the set
    print(randomizedSet.insert(2))   # Inserts 2 to the set, returns true
    
    # getRandom should return either 1 or 2 randomly
    random_val = randomizedSet.get_random()
    print(f"Random value: {random_val}")  # Will be either 1 or 2
    
    print(randomizedSet.remove(1))   # Removes 1 from the set, returns true
    print(randomizedSet.insert(2))   # 2 was already in the set, so return false
    
    # Since 2 is the only number in the set, getRandom will always return 2
    print(f"Random value: {randomizedSet.get_random()}")  # Will always be 2
    
    # Additional tests
    print("\nAdditional tests:")
    randomizedSet.insert(3)
    randomizedSet.insert(4)
    randomizedSet.insert(5)
    
    print("Current set:", randomizedSet.values)
    print("Random value:", randomizedSet.get_random())  # Will be one of 2, 3, 4, or 5
    
    print("Remove 3:", randomizedSet.remove(3))
    print("Current set after removing 3:", randomizedSet.values)
