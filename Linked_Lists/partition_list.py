'''
LeetCode: Partition List

Given a linked list and a value x, partition it such that all nodes less than x
 come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two
partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

Solution: O(n)
Algorithm:
    1) Maintain 2 lists namely, LEFT and RIGHT. (Use dummy heads to init both)
    2) Traverse through the list. If the node.val < x, add it to the left list,
    else add it to the right list
    3) At the end, connect the LEFT to the RIGHT as
    left_iterator.next = dummy_head_right.next
    4) Take care of the RIGHT next pointer as right_iterator.next = None
    5) Return dummy_head_left.next as the head
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy_head_left = ListNode(0)
        dummy_head_right = ListNode(0)
        dummy_head_left.next = dummy_head_right.next = None
        left_i = dummy_head_left
        right_i = dummy_head_right
        iterator = head

        while iterator is not None:
            if iterator.val < x:
                left_i.next = iterator
                left_i = left_i.next
            else:
                right_i.next = iterator
                right_i = right_i.next
            iterator = iterator.next
        right_i.next = None
        left_i.next = dummy_head_right.next
        return dummy_head_left.next
