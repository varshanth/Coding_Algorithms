'''
LeetCode: Add Two Numbers II

You are given two non-empty linked lists representing two non-negative
integers. The most significant digit comes first and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists
is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

Solution: Time: O(n) Space: O(n), where n = length of the bigger number
Algorithm:
    1) Find the size of the both the lists
    2) Pad the smaller list with zeros so that both the list lengths are equal
    3) Call a recursive function which takes in 2 list heads and does the
    following:
        a) Calculate absolute sum of the passed nodes
        b) Determine the result node and the carry from the further nodes by
        calling this function again with l1.next and l2.next if l1.next is not
        None. (If l1.next is None, then this is the last node and hence result
        node of the further node is None and carry is 0)
        c) Add the carry to the absolute sum and determine the current carry
        d) Create a new ListNode (current result node) with value absolute
        sum % 10 and assign its next value to be equal to the result node
        obtained from the previous step
        e) Return carry and the new result node
    4) If a carry is returned, create a ListNode with value 1 and assign its
    next node to be the returned result node. Assign the result node as the
    "one" node
    5) Return the result node

e.g)
l1: 7  ->  2  ->  4  ->  3  ->  1
l2: 5  ->  6  ->  4

Step 2:

l1: 7  ->  2  ->  4  ->  3  ->  1
l2: 0  ->  0  ->  5  ->  6  ->  4

Step 3:

Result:  7  ->  2  ->  9  ->  9  ->  5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        l1_size = l2_size = 0
        l1_iter = l1
        l2_iter = l2
        while l1_iter:
            l1_size += 1
            l1_iter = l1_iter.next
        while l2_iter:
            l2_size += 1
            l2_iter = l2_iter.next
        bigger, smaller = [l1, l2] if l1_size > l2_size else [l2,l1]
        bigger_size, smaller_size = ([l1_size, l2_size]
                                     if l1_size > l2_size
                                     else [l2_size, l1_size])
        diff = bigger_size - smaller_size
        for i in range(diff):
            zero = ListNode(0)
            zero.next = smaller
            smaller = zero
        carry, result_head = self.addTwoSimilarLengthNumbers(smaller, bigger)
        if carry:
            one = ListNode(1)
            one.next = result_head
            result_head = one
        return result_head
    
    def addTwoSimilarLengthNumbers(self, l1, l2):
        abs_sum = l1.val + l2.val
        carry, prev_res = (self.addTwoSimilarLengthNumbers(l1.next, l2.next)
                           if l1.next is not None else [0, None])
        abs_sum += carry
        result_node = ListNode(abs_sum%10)
        carry = 1 if abs_sum >=10 else 0
        result_node.next = prev_res
        return [carry, result_node]