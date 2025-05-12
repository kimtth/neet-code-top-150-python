from typing import List


"""
LeetCode 271. Encode and Decode Strings

Problem from LeetCode: https://leetcode.com/problems/encode-and-decode-strings/

Description:
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}

Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}

So Machine 1 does:
string encoded_string = encode(strs);

and Machine 2 does:
vector<string> strs2 = decode(encoded_string);

strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

Example 1:
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

Example 2:
Input: dummy_input = [""]
Output: [""]
"""

class Codec:
    """
    Design an algorithm to encode a list of strings to a string.
    The encoded string is then sent over the network and is decoded back to the original list of strings.
    """

    def encode(self, strs: List[str]) ->str:
        """
        Encodes a list of strings to a single string.
        
        Args:
            strs: List of strings to encode
            
        Returns:
            str: Encoded string
        """
        if len(strs) == 0:
            return chr(258)
        separator = chr(257)
        return separator.join(strs)

    def decode(self, s: str) ->List[str]:
        """
        Decodes a single string to a list of strings.
        
        Args:
            s: Encoded string
            
        Returns:
            List[str]: Decoded list of strings
        """
        if s == chr(258):
            return []
        separator = chr(257)
        return s.split(separator)

    def encode_length_prefixed(self, strs: List[str]) ->str:
        """
        Encodes a list of strings to a single string using length prefixing.
        Format: [length]#[string][length]#[string]...
        
        Args:
            strs: List of strings to encode
            
        Returns:
            str: Encoded string
        """
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode_length_prefixed(self, s: str) ->List[str]:
        """
        Decodes a single string to a list of strings using length prefixing.
        
        Args:
            s: Encoded string
            
        Returns:
            List[str]: Decoded list of strings
        """
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            result.append(s[i:i + length])
            i += length
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    codec = Codec()
    
    # Example 1
    strs1 = ["Hello", "World"]
    print(f"Example 1 Input: {strs1}")
    
    # Using character separator approach
    encoded1 = codec.encode(strs1)
    print(f"Encoded: {encoded1!r}")
    decoded1 = codec.decode(encoded1)
    print(f"Decoded: {decoded1}")
    print(f"Matching original: {strs1 == decoded1}")
    
    # Using length-prefixed approach
    encoded1_lp = codec.encode_length_prefixed(strs1)
    print(f"\nLength-prefixed encoded: {encoded1_lp!r}")
    decoded1_lp = codec.decode_length_prefixed(encoded1_lp)
    print(f"Length-prefixed decoded: {decoded1_lp}")
    print(f"Matching original: {strs1 == decoded1_lp}")
    
    # Example 2
    strs2 = [""]
    print(f"\nExample 2 Input: {strs2}")
    
    # Using character separator approach
    encoded2 = codec.encode(strs2)
    print(f"Encoded: {encoded2!r}")
    decoded2 = codec.decode(encoded2)
    print(f"Decoded: {decoded2}")
    print(f"Matching original: {strs2 == decoded2}")
    
    # Using length-prefixed approach
    encoded2_lp = codec.encode_length_prefixed(strs2)
    print(f"\nLength-prefixed encoded: {encoded2_lp!r}")
    decoded2_lp = codec.decode_length_prefixed(encoded2_lp)
    print(f"Length-prefixed decoded: {decoded2_lp}")
    print(f"Matching original: {strs2 == decoded2_lp}")
    
    # Example with special characters
    strs3 = ["#", "a#b", "c##d", "", "###"]
    print(f"\nSpecial characters Input: {strs3}")
    
    # Using length-prefixed approach (more robust with special characters)
    encoded3_lp = codec.encode_length_prefixed(strs3)
    print(f"Length-prefixed encoded: {encoded3_lp!r}")
    decoded3_lp = codec.decode_length_prefixed(encoded3_lp)
    print(f"Length-prefixed decoded: {decoded3_lp}")
    print(f"Matching original: {strs3 == decoded3_lp}")
