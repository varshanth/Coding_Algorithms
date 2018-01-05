'''
LeetCode: Sort a Linked List

Sort a linked list in O(nlog(n)) with constant space complexity

Solution: Time: O(nlog(n)) Space: O(1)
Algorithm:
    Typical Mergesort algorithm with some slight variations:
        a) We pass linked lists to the merge and mergesort functions
        b) While splitting the linked lists, we split the original linked list
        in place by making the split linked lists as separate and disconnected
        c) Merge function takes care of connecting back the linked list after
        merging the sorted linked lists

e.g) 5  ->  4  ->  3  ->  2  ->  1
           /              \
    5  ->  4               3  ->  2  ->  1
                           /              \
    4  ->  5               3               2  ->  1
           \               3               1  ->  2
            \               \             /
             \              1  ->  2  ->  3
              \            /
     1  ->  2  ->  3  ->  4  ->  5
     
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        def merge(head1, head2):
            if head1 is None:
                return head2
            if head2 is None:
                return head1
            dummy_head = ListNode(0)
            dummy_head.next = None
            head1_iter = head1
            head2_iter = head2
            dummy_iter = dummy_head
            while head1_iter and head2_iter:
                if head1_iter.val < head2_iter.val:
                    dummy_iter.next = head1_iter
                    head1_iter = head1_iter.next
                else:
                    dummy_iter.next = head2_iter
                    head2_iter = head2_iter.next
                dummy_iter = dummy_iter.next
            while head1_iter:
                dummy_iter.next = head1_iter
                dummy_iter = dummy_iter.next
                head1_iter = head1_iter.next
            while head2_iter:
                dummy_iter.next = head2_iter
                dummy_iter = dummy_iter.next
                head2_iter = head2_iter.next
            dummy_iter.next = None
            return dummy_head.next
            
        def mergesort(head, size):
            if size is 0 or size is 1:
                return head
            half = size // 2
            other_half = size - half
            head1 = head
            head2 = head
            # Traverse till the last node in the 1st half
            for i in range(half-1):
                head2 = head2.next
            # Save the next connection and terminate the first list
            head2_start = head2.next
            head2.next = None
            # Start the second half using the saved pointer
            head2 = head2_start
            # Split and sort the left half
            left_sorted = mergesort(head, half)
            # Split and sort the right half
            right_sorted = mergesort(head2, other_half)
            # Merge the sorted halves
            merged = merge(left_sorted, right_sorted)
            return merged
        
        size = 0
        iterator = head
        while iterator:
            size += 1
            iterator = iterator.next
        return mergesort(head, size)
        