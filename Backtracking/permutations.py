'''
LeetCode: Permutaions

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Solution: O(2^n)
Algorithm: Backtracking:
    1) Maintain a dictionary of the accepted permutations
    2) Call a DFS recursive function which takes as arguments:
    a) The current permutation b) the choices c) accepted permutations
    This function will check if there are any remaining choices. If there
    aren't, then it will check if the current permutation is in the accepted
    permutations dictionary. If it is not, then it will add it.
    If there are remaining choices, for each remaining choice, it will add
    the choice to the current permutation (push), call itself recursively by
    passing to the function call the new current permutation, the choices list
    excluding the current choice and the accepted permutations dictionary.
    After the recursive call is complete, it will pop the current choice from
    the current permutation and move on to the next choice.
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perm_set = {}
        self.explore_perm_dfs([], nums, perm_set)
        return list(perm_set.keys())
    
    def explore_perm_dfs(self, cur_perm, choices, perm_set):
        if len(choices) is 0:
            if tuple(cur_perm) not in perm_set:
                perm_set[tuple(cur_perm)] = None
                return
        for i in range(len(choices)):
            cur_elem = choices[i]
            cur_perm.append(cur_elem)
            self.explore_perm_dfs(cur_perm, choices[:i]+choices[i+1:], perm_set)
            cur_perm.pop()