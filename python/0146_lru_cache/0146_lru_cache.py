from typing import List, Optional

"""
LeetCode LRU Cache

Problem from LeetCode: https://leetcode.com/problems/lru-cache/

Description:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example:
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""

class Node:
    """
    Doubly linked list node to store key-value pairs and maintain order.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache implementation using a hash map and a doubly linked list.
    The hash map provides O(1) access to cache items, while the doubly linked list
    maintains the order of items for efficient LRU eviction.
    """
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with the given capacity.
        
        Args:
            capacity: Maximum number of key-value pairs the cache can hold
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Retrieve the value of the key if it exists in the cache.
        This operation also makes the key the most recently used.
        
        Args:
            key: Key to look up in the cache
            
        Returns:
            int: Value associated with the key, or -1 if the key doesn't exist
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_at_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the value of a key in the cache.
        If the key already exists, update its value and make it the most recently used.
        If the key doesn't exist, add it to the cache. If this causes the cache to
        exceed its capacity, remove the least recently used item.
        
        Args:
            key: Key to insert or update
            value: Value to associate with the key
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._insert_at_head(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._insert_at_head(new_node)

    def _remove(self, node: Node) -> None:
        """
        Remove a node from the doubly linked list.
        
        Args:
            node: Node to remove
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_head(self, node: Node) -> None:
        """
        Insert a node at the head of the doubly linked list (most recently used).
        
        Args:
            node: Node to insert
        """
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    lru_cache = LRUCache(2)
    
    operations = [
        "put", "put", "get", "put", "get", "put", "get", "get", "get"
    ]
    params = [
        [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]
    ]
    
    results = []
    for i, op in enumerate(operations):
        if op == "put":
            lru_cache.put(params[i][0], params[i][1])
            results.append(None)
        elif op == "get":
            result = lru_cache.get(params[i][0])
            results.append(result)
    
    print("Operations:", operations)
    print("Parameters:", params)
    print("Results:", results)
    # Expected output: [None, None, 1, None, -1, None, -1, 3, 4]
