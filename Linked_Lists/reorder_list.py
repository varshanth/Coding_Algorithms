'''
LeetCode: Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

Solution: O(n) Space: O(n)
Algorithm:
    1) Iterate through the list and determine size of the list. While iterating
    push the nodes into a stack
    2) Iterate from the head, save the node.next, pop a node from the stack and
    update the connections as node.next = popped node, and popped
    node.next = saved node.next and the iterator to the saved node.next
    3) Perform step 2) size/2 number of times to yield alternating nodes in 
    forward and reverse order
    4) At the end, assign the iterator.next to None since it has become the new
    tail

e.g)    1  ->  2  ->  3  ->  4  ->  5

Stack:   5 4 3 2 1

Iteration 1:   1  -    2  ->  3  ->  4  ->  5
               i   \   ^
                    \  |
Popped:              ->5
Stack:   4 3 2 1

Iteration 2:   1  ->  5  ->  2  -    3  ->  5
                             i   \   ^
                                  \  |
Popped:                            ->4
Stack:   3 2 1

Stop:          1  ->  5  ->  2  ->  4  ->  3
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return
        size = 0
        iterator = head
        stack = []
        while iterator is not None:
            size += 1
            stack.append(iterator)
            iterator = iterator.next
        iterator = head
        for i in range(size//2):
            iter_next = iterator.next
            iterator.next = stack.pop()
            iterator.next.next = iter_next
            iterator = iter_next
        iterator.next = None