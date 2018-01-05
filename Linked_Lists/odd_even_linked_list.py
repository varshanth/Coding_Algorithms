'''
LeetCode: Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even
nodes. Please note here we are talking about the node number and not the value
in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was
in the input. 
The first node is considered odd, the second node even and so on ...

Solution: Time: O(n) Space: O(n)
Algorithm:
    1) Create 2 dummy heads as odd head and even head and init their nexts to
    None. Init 2 iterators, odd iterator and even iterator to the respective
    dummy heads
    2) Use an iterator and init and iterator index to 1 (indicating that we are
    starting from the 1st node) and keep track of the iterator index
    3) If the iterator index is odd, update the odd_iterator.next to this
    iterator and update the odd_iterator to odd_iterator.next. If the iterator
    index is even, update the even_iterator.next to this iterator and update
    the even_iterator to even_iterator.next 
    4) Update the iterator to iterator.next and repeat until iterator is None
    5) At the end, update the even iterator.next to None, odd iterator.next
    to the even head.next and return the odd head.next
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Size is 0, 1, or 2
        if head is None or head.next is None or head.next.next is None:
            return head
        head_odd = ListNode(0)
        head_odd.next = None
        head_even = ListNode(0)
        head_even.next = None
        odd_iter = head_odd
        even_iter = head_even
        i = 1
        iterator = head
        while iterator:
            if i % 2 != 0:
                odd_iter.next = iterator
                odd_iter = odd_iter.next
            else:
                even_iter.next = iterator
                even_iter = even_iter.next
            iterator = iterator.next
            i += 1
        even_iter.next = None
        odd_iter.next = head_even.next
        return head_odd.next