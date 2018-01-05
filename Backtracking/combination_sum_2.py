'''
LeetCode: Combination Sum 2
Given a collection of candidate numbers (C) and a target number (T), find all
unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Solution: O(2^n)
Algorithm: Backtracking:
    1) Maintain a dictionary of the accepted combinations
    2) Call a DFS recursive function which takes as arguments:
    a) The current combination b) the remaining sum to be calculated
    c) the sorted list of choices d) accepted combinations
        i) For each of the choices, calculate the new remaining sum as the
        difference between the old remaining sum and the current choice.
        ii) If the new remaining sum is less than 0, since the choices are
        sorted, there is no point in proceeding with the next choice, so break.
        iii) If the remaining sum is greater than or equal to 0, then add the
        current choice to the current combination.
        iv) If the remaining sum is equal to 0, check if the current
        combination is in the accepted combinations, if not, add it
        v) If the remaining sum is greater than 0, then call the recursive
        function by passing the list of choices as the list of all future
        choices, the new remaining sum, the current combination and the
        accepted combinations
        vi) Pop the current choice from the current combination and evaluate
        the next choice
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        accepted_combin = {}
        self.explore_comb_sum_dfs([], target, sorted(candidates),
                                  accepted_combin)
        return list(accepted_combin.keys())
    
    def explore_comb_sum_dfs(self, cur_combin, rem_sum, choices,
                             accepted_combin):
        for i in range(len(choices)):
            new_rem_sum = rem_sum - choices[i]
            if new_rem_sum >= 0:
                cur_combin.append(choices[i])
                if new_rem_sum is 0:
                    key = tuple(cur_combin)
                    if key not in accepted_combin:
                        accepted_combin[key] = None
                else:
                    self.explore_comb_sum_dfs(cur_combin, new_rem_sum,
                                          choices[i:], accepted_combin)
                cur_combin.pop()
            else:
                break