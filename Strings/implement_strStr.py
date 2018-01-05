'''
LeetCode: Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Solution: O(mn)
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_n = len(needle)
        len_h = len(haystack)
        if len_n > len_h:
            return -1
        if len_n is 0:
            return 0
        for slow in range(len_h - len_n + 1):
            if haystack[slow:slow+len_n] == needle:
                return slow
        return -1