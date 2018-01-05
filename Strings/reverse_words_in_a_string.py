'''
LeetCode: Reverse Words in a String

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

Algorithm:
    1) Strip the initial sentence from leading and trailing spaces
    2) Use split to seperate the words based on whitespaces
    3) Reverse the array of words
    4) Construct new sentence based on the reversed order
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        if len(s) is 0:
            return ''
        words = s.split()
        reverse_words = words[::-1]
        sentence = reverse_words[0]
        for i in range(1,len(reverse_words)):
            sentence += ' {0}'.format(reverse_words[i])
        return sentence