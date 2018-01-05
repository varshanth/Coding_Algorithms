'''
LeetCode: Palindrome Linked List


Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

Solution: Time: O(n) Space: O(1)
Algorithm:
    1) Check boundary conditions and do necessary returns
    2) Iterate through the entire list to determine the size
    3) Traverse to the middle node (in case of odd number, (n/2)+1, in case
    of even number n/2)
    4) Keep track of the middle node
    5) Reverse the second half of the linked list
    6) Use 2 pointers, one pointing to head and one pointing to the 
    middle_node.next, and iterate (n/2) nodes while comparing its values.
    Return false if the values aren't equal
    7) Return true if the previous iteration didn't return false already
    
e.g)
Start             1  ->  2  ->  3  ->  3  ->  2  ->  1
                                m

Step 3 to 5       1  ->  2  ->  3  ->  1  ->  2  ->  3

Step 6            1  ->  2  ->  3  ->  1  ->  2  ->  3
                  s                    m
                  
                  1  ->  2  ->  3  ->  1  ->  2  ->  3
                         s                    m
                         
                  1  ->  2  ->  3  ->  1  ->  2  ->  3
                                s                    m
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        # Get size of list
        size = 0
        iterator = head
        while iterator is not None:
            size += 1
            iterator = iterator.next
        skip_middle = (size % 2 != 0)
        from_middle = head
        # Go to the middle node
        for i in range(size // 2 -1):
            from_middle = from_middle.next
        if skip_middle:
            from_middle = from_middle.next
        # Reverse the list from the middle
        prev_node = None
        curr_node = from_middle.next
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        from_middle.next.next = None
        from_middle.next = prev_node
        from_start = head
        from_middle = from_middle.next
        for i in range(size // 2):
            if from_start.val != from_middle.val:
                return False
            from_start = from_start.next
            from_midd