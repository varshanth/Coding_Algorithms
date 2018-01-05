'''
LeetCode: Length of Longest Substring

Given a string, find the length of the longest substring without repeating
characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
must be a substring, "pwke" is a subsequence and not a substring.


Solution: O(2n)
Algorithm: Sliding Window Based:
    1) Initialize 2 iterators to 0, a tempstore dictionary, a var not_done
    to keep track of if a repetition was encountered or not, and the best length
    2) Iterate until one of the 2 iterators (i,j) becomes equal to length of str
    3) If s[j] is not in temp store, add it to the tempstore, increment j, and
    set not_done to True
    4) If s[j] is in temp store, s[j] is a repetition of a previous character,
    set not_done to False, find length of tempstore, if it is better than the
    best, set best as current length of tempstore. Pop s[i] and increment i
    5) At the end, check if not_done is True, if yes, it means that the current
    substring has not been analyzed. Find length of tempstore, if it is better
    than the best, assign it as the best

e.g)
strinstratt  
i--->j
 i-->j
  i->j
     ij
     i->j
     i--->j
      i-->j
       i->j
         ij
'''
     
  


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp_store = {}
        i = j = 0
        best = 0
        len_s = len(s)
        not_done = False
        while i < len_s and j < len_s:
            if s[j] not in temp_store:
                temp_store[s[j]] = None
                j += 1
                not_done = True
            else:
                cur_len = len(temp_store)
                if cur_len > best:
                    best = cur_len
                temp_store.pop(s[i])
                i += 1
                not_done = False
        if not_done:
            cur_len = len(temp_store)
            if cur_len > best:
                best = cur_len
        return best
