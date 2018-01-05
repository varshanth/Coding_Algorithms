'''
LeetCode: Palindrome Check without extra space
Solution: O(nlogbase10(n))
Algorithm:
    1) Beware of edge cases i.e -ve nos, nos < 10 and numbers greater than 1
       divisible by 10
    2) Maintain 2 variables, left and right. Left will be the number, right =0
    3) Shift rightmost variable of left to that of the right.
    4) Return true if left is equal to right or if left is equal to right/10
       (in those cases of odd length palindromes e.g 121 left = 1,right=12)
       
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x >= 10 and x%10 == 0):
            return False
        if x < 10:
            return True
        x_left = x
        x_right = 0
        while x_left > x_right:
            x_right = (x_right * 10) + (x_left % 10)
            x_left //=10
        if x_left == x_right or x_left == (x_right//10):
            return True
        return False
        