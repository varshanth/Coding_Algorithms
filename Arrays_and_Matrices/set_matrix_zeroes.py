'''
LeetCode: Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Solution: O(m+n) space
    
Algorithm:
    a) Maintain 2 arrays m_zeroes and n_zeroes which keeps track of the rows
    and columns where zeroes are present in the matrix
    b) Go through the entire matrix and update m_zeroes and n_zeroes
    c) Now go through the entire matrix again and set the element in the matrix
    to zero if m_zeroes[i] is 0 or n_zeroes[j] is 0
    
'''

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m is 0:
            return
        n = len(matrix[0])
        if n is 0:
            return
        m_zero = [1 for i in range(m)]
        n_zero = [1 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] is 0:
                    m_zero[i] = 0
                    n_zero[j] = 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] *= (m_zero[i]*n_zero[j])
        return

        