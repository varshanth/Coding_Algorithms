'''
LeetCode: Group Anagrams
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

Solution: O(n), n = no of words
Algorithm:
    1) The common factor of anagrams is that they are all made of the same
    letters. We can capture this by sorting the string.
    2) Create a dictionary per unique sorted sequence of letters (key) with the
    value as the list of strings with that key.
    
    **Implementation tip: Dictionaries accept only immutable datatypes as keys,
    hence we have to convert the list to a tuple**
    
    3) Return the list of dictionary values as the output
'''
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        unique_dict = {}
        for string in strs:
            key = tuple(sorted(string))
            if key in unique_dict:
                unique_dict[key].append(string)
            else:
                unique_dict[key] = [string]
        return_list = list(unique_dict.values())
        return return_list
                
        