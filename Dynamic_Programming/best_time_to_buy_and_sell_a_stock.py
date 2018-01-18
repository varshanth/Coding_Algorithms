'''
LeetCode: Best time to buy and sell a stock

Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (ie, buy one and
sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger
than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

Solution: O(n)
Algorithm:
    The solution to this problem is to identify the highest difference between
    the lowest terms and its future terms in the array
    
    1) Initialize 2 variables, one which keeps track of the smallest term, to
    the first element in the array, and the other as the max profit to 0
    2) Go through the array from the 2nd element and assign the smallest term
    as the minimum of the current smallest term and the current term
    3) Assign the max profit as the max of the current max profit and diff b/w
    the current term and the smallest term
'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_prices = len(prices)
        if len_prices < 2:
            return 0
        max_profit, min_price = 0, prices[0]
        
        for i in range(1,len_prices):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i]-min_price)
        return max_profit