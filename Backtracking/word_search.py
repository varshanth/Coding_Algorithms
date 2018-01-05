'''
LeetCode: Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

Solution: O((mn)^2)
Algorithm: Backtracking and DFS:
    a) We start with a starting position and if the node's value is equal to
    the target word's first character, then we visit the neighboring nodes in a
    depth first manner.

    b) We keep track of the visited node in a single path. At each visit, if
    the current node has not been visited already and if the current node's
    value is equal to the required char in the word passed, then we mark the
    node as visited (push into a stack) and search in the 4 directions
    (top, down, left, or right) by calling DFS with the rest of the characters
    of the word EXCEPT the one visited by the current node. e.g) if the word is
    'THIS', if we are at 'H', then we would pass IS i.e word[1:] (the previous
    DFS call (at T) would have passed word[1:], effectively making this call as
    word[2:])
    
    c) In the DFS call, if the length of the word passed is 0, then we have
    traversed all the letters of the word and hence we return True.
    
    d) We then pop out the current node from the visited stack and return
    (DFS(up) or DFS(down) or DFS(left) or DFS(right)). If any of the explored
    directions would have yielded the successful word traversal, the
    corresponding call would yield True and the by the property of the OR,
    the further DFS calls needn't take place
'''

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m is 0:
            return False
        n = len(board[0])
        if n is 0:
            return False
        
        visited = {}
        def DFS(board, i, j, word):
            if len(word) is 0:
                # Nothing to seek, word traversal complete: word is found
                return True
            if ((i < 0) or (i == m) or (j < 0) or (j == n) or
                ((i,j) in visited) or (board[i][j] != word[0])):
                return False
            # Push node onto visited stack
            visited[(i,j)] = True
            pattern_present = (
                    DFS(board, i+1, j, word[1:]) or
                    DFS(board, i-1, j, word[1:]) or
                    DFS(board,i, j-1, word[1:]) or
                    DFS(board, i, j+1, word[1:])
                    )
            # Pop node out of stack
            visited.pop((i,j))
            return pattern_present
        
        for i in range(m):
            for j in range(n):
                if DFS(board, i, j, word):
                    return True
        return False