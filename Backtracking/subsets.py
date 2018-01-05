'''
LeetCode: Subsets

Given a set of distinct integers, nums, return all possible subsets (the power
set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Solution: O(2^n)
Algorithm: Backtracking:
    1) Initialize the subset dictionary to contain empty set
    2) Call a DFS function by passing the nums array, the subset dictionary and
    the current subset so far:
        a) If the nums array is empty, return
        b) Repeat for all elements in the nums array:
        i) Add the current element in the nums array to the current subset
        ii) Check if the current subset in the subset dictionary. If not, then
        add it to the dictionary and call the DFS function by passing the
        current subset, the nums array from the i+1th element and the subset
        dictionary
        iii) Pop the current element from the current subset
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets_dict = {():None}
        self.explore_subsets_dfs([], nums, subsets_dict)
        return list(subsets_dict.keys())
        
    def explore_subsets_dfs(self, cur_subset, nums, subsets_dict):
        if len(nums) is 0:
            return
        for i in range(len(nums)):
            cur_subset.append(nums[i])
            if tuple(cur_subset) not in subsets_dict:
                subsets_dict[tuple(cur_subset)] = None
                self.explore_subsets_dfs(cur_subset, nums[i+1:], subsets_dict)
            cur_subset.pop()