'''
LeetCode: Add_2_Numbers_1
Solution: O(m+n)
Algorithm:
    1) Create dummy node for result and init carry to 0
    2) Iterate until one of the list iterators become None: (O(m) or O(n))
        a) Add the 2 iterator values and carry
        b) Update carry
        c) Create node for result and append to result list
    3) Perform 2 just for list 1 and carry (O(m))
    4) Perform 2 just for list 2 and carry (O(n))
    5) If there is carry at the end, perform 2c just for the carry
    6) Return result head
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = int(0)
        l1_iter = l1
        l2_iter = l2
        result_head = ListNode(0)
        result_iter = result_head
        while l1_iter is not None and l2_iter is not None:
            arithm_result = l1_iter.val + l2_iter.val + carry
            carry = arithm_result // 10
            if carry is not 0:
                arithm_result -= int(10)
            result_iter.next = ListNode(arithm_result)
            result_iter = result_iter.next
            l1_iter = l1_iter.next
            l2_iter = l2_iter.next
        while l1_iter is not None:
            arithm_result = l1_iter.val + carry
            carry = arithm_result // 10
            if carry is not 0:
                arithm_result -= int(10)
            result_iter.next = ListNode(arithm_result)
            result_iter = result_iter.next
            l1_iter = l1_iter.next
        while l2_iter is not None:
            arithm_result = l2_iter.val + carry
            carry = arithm_result // 10
            if carry is not 0:
                arithm_result -= int(10)
            result_iter.next = ListNode(arithm_result)
            result_iter = result_iter.next
            l2_iter = l2_iter.next
        if carry is not 0:
            result_iter.next = ListNode(1)
            result_iter = result_iter.next      
        result_head = result_head.next
        return result_head