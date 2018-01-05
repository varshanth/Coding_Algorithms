'''
LeetCode: Longest Common Prefix

Longest common prefix for a pair of strings S1 and S2 is the longest string S
which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is the prefix
of ALL the strings in the array.

Solution: O(n * min(length of all strings)) where n = no of strings
Algorithm:
    1) The max length of prefix is at worst the length of smallest string in
    the list of strings. Find length of smallest string
    2) Obviously if min length of any string is 0, there is no common prefix
    3) Iterate through min_length characters one by one of all strings and if
    there is a mismatch, break and return any_string[:iterator_val]

'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        len_strs = len(strs)
        if len_strs is 0:
            return ''
        # Find string of min length
        len_array = [len(string) for string in strs]
        min_len = min(len_array)
        if min_len is 0:
            return ''
        i = 0
        break_outer = False
        while i < min_len:
            ith_letter = strs[0][i]
            for string in strs[1:]:
                if string[i] != ith_letter:
                    break_outer = True
                    break
            if break_outer:
                break
            i+=1
        # Use any string since prefix will be common
        first = strs[0]
        return first[:i]
                
        