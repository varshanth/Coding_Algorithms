'''
Leetcode: Rotate a singly linked list by k elements
Solution: O(n)
Algorithm: Lots of test cases to consider!!:
    1) If head is none return
    2) Get effective k, because it can be greater than the size of the list.
    Get size of list and effective k = k % size
    3) If k is 0, no effective rotation required so return
    4) From head (1st position) go to the (size - k)th position i.e size -k -1
    (From a dummy head, it is just size - k) using iterator
    5) Reassign pointers:
       last.next = head, head = iterator.next, iterator.next = None

e.g) 
   head
     A->B->C->D->E, k=2

             head
     A->B->C->D->E
     ^           |
     |------------
             
             head     
     A->B->C  D->E
     ^           |
     |------------
     
Tricks & Lessons Learnt:
************************
    1) Never assume ideal scenario for the input UNLESS mentioned
    2) When iterating through a list, first determine if you will need the ptr
    to the last element or not.
    a) If you need, then when iterating through to determine the size,
        i) Check if head is None, if assign size = 0
        ii) Else, assign size = 1, and START ptr from head, increment size count
            and END when ptr.next is None i.e stop when you are at the last node
       **In this, we do not process the last node
    b) Else, determine the size the correct way:
        i) Assign size=0
        ii) START ptr from head, increment size count and END when ptr is None
       **In this, we process the last node
'''                 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        get_size_iter = iter = head
        size = 1
        while get_size_iter.next is not None:
            get_size_iter = get_size_iter.next
            size += 1
        if k >= size:
            k = k % size
        if k is 0:
            return head
        for i in range(size-k-1):
            iter = iter.next
        get_size_iter.next = head
        head = iter.next
        iter.next = None
        return head