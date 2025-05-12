from collections import defaultdict
import bisect
from typing import Dict, List, Tuple


"""
LeetCode Time Based Key Value Store

Problem from LeetCode: https://leetcode.com/problems/time-based-key-value-store/

Design a time-based key-value data structure that can store multiple values for the same 
key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key with the value value
  at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was called previously,
  with timestamp_prev <= timestamp. If there are multiple such values, it returns the value 
  associated with the largest timestamp_prev. If there are no values, it returns "".

Example 1:
    Input:
    ["TimeMap", "set", "get", "get", "set", "get", "get"]
    [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    Output:
    [null, null, "bar", "bar", null, "bar2", "bar2"]
    
    Explanation:
    TimeMap timeMap = new TimeMap();
    timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
    timeMap.get("foo", 1);         // return "bar"
    timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
    timeMap.get("foo", 4);         // return "bar2"
    timeMap.get("foo", 5);         // return "bar2"

Constraints:
    1 <= key.length, value.length <= 100
    key and value consist of lowercase English letters and digits.
    1 <= timestamp <= 10^7
    All the timestamps timestamp of set are strictly increasing.
    At most 2 * 10^5 calls will be made to set and get.
"""

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) ->None:
        """
        Store the key-value pair in the data structure.
        
        Args:
            key: The key to store
            value: The value to store
            timestamp: The timestamp for this key-value pair
        """
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) ->str:
        """
        Return the value associated with the key at the timestamp.
        
        Args:
            key: The key to retrieve
            timestamp: The timestamp to search for
            
        Returns:
            str: The value at the timestamp, or "" if not found
        """
        if key not in self.store:
            return ''
        values = self.store[key]
        idx = bisect.bisect_right(values, (timestamp, chr(127)))
        if idx == 0:
            return ''
        return values[idx - 1][1]


class TimeMap_manual_binary_search:

    def __init__(self):
        """
        Initialize the TimeMap.
        """
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) ->None:
        """
        Store the key-value pair.
        """
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) ->str:
        """
        Get the value at or before the given timestamp.
        """
        if key not in self.store:
            return ''
        values = self.store[key]
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0:
            return values[right][1]
        else:
            return ''


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    print(timeMap.get("foo", 1))   # Output: "bar"
    print(timeMap.get("foo", 3))   # Output: "bar"
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))   # Output: "bar2"
    print(timeMap.get("foo", 5))   # Output: "bar2"
    
    # Testing alternative implementation
    print("\nTesting manual binary search implementation:")
    timeMap2 = TimeMap_manual_binary_search()
    timeMap2.set("foo", "bar", 1)
    print(timeMap2.get("foo", 1))  # Output: "bar"
    print(timeMap2.get("foo", 3))  # Output: "bar"
    timeMap2.set("foo", "bar2", 4)
    print(timeMap2.get("foo", 4))  # Output: "bar2"
    print(timeMap2.get("foo", 5))  # Output: "bar2"
