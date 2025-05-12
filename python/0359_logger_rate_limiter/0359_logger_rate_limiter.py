from typing import List, Optional

"""
LeetCode Logger Rate Limiter

Problem from LeetCode: https://leetcode.com/problems/logger-rate-limiter/

Description:
Design a logger system that receives a stream of messages along with their timestamps. 
Each unique message should only be printed at most every 10 seconds 
(i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:
- Logger() Initializes the logger object.
- bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.

Example:
Input
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output
[null, true, true, false, false, false, true]

Explanation
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");  // return false, message "foo" was printed at timestamp 1, the next allowed timestamp is 11
logger.shouldPrintMessage(8, "bar");  // return false, message "bar" was printed at timestamp 2, the next allowed timestamp is 12
logger.shouldPrintMessage(10, "foo"); // return false, message "foo" was printed at timestamp 1, the next allowed timestamp is 11
logger.shouldPrintMessage(11, "foo"); // return true, message "foo" was not printed in the last 10 seconds, timestamp 11 is allowed

Constraints:
0 <= timestamp <= 10^9
Every timestamp will be passed in non-decreasing order (chronological order).
1 <= message.length <= 30
At most 10^4 calls will be made to shouldPrintMessage.
"""

class Logger:
    """
    Design a logger system that receives a stream of messages along with timestamps.
    Each unique message should only be printed at most every 10 seconds.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg_dict = {}

    def should_print_message(self, timestamp: int, message: str) ->bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        
        Args:
            timestamp: The current timestamp (in seconds)
            message: The message to be printed
            
        Returns:
            bool: True if the message should be printed, False otherwise
        """
        if message not in self.msg_dict:
            self.msg_dict[message] = timestamp
            return True
        old_timestamp = self.msg_dict[message]
        if timestamp - old_timestamp >= 10:
            self.msg_dict[message] = timestamp
            return True
        else:
            return False


    class LoggerWithQueue:

        def __init__(self):
            self.msg_dict = {}
            self.msg_queue = []

        def should_print_message(self, timestamp: int, message: str) ->bool:
            while self.msg_queue and self.msg_queue[0][0] <= timestamp - 10:
                old_time, old_msg = self.msg_queue.pop(0)
                if self.msg_dict.get(old_msg) == old_time:
                    self.msg_dict.pop(old_msg)
            if message not in self.msg_dict:
                self.msg_dict[message] = timestamp
                self.msg_queue.append((timestamp, message))
                return True
            return False


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    logger = Logger()
    
    # Test the main Logger implementation
    print("Testing Logger implementation:")
    print(logger.should_print_message(1, "foo"))   # true
    print(logger.should_print_message(2, "bar"))   # true
    print(logger.should_print_message(3, "foo"))   # false
    print(logger.should_print_message(8, "bar"))   # false
    print(logger.should_print_message(10, "foo"))  # false
    print(logger.should_print_message(11, "foo"))  # true
    
    # Test the Logger with Queue implementation
    print("\nTesting LoggerWithQueue implementation:")
    logger_with_queue = Logger.LoggerWithQueue()
    print(logger_with_queue.should_print_message(1, "foo"))   # true
    print(logger_with_queue.should_print_message(2, "bar"))   # true
    print(logger_with_queue.should_print_message(3, "foo"))   # false
    print(logger_with_queue.should_print_message(8, "bar"))   # false
    print(logger_with_queue.should_print_message(10, "foo"))  # false
    print(logger_with_queue.should_print_message(11, "foo"))  # true
