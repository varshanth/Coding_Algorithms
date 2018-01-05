'''
LeetCode: Copy List with Random Pointer
You are given a Double Link List with one pointer of each node pointing to the
next node just like in a single link list. The second pointer however CAN point
to any node in the list and not just the previous node. Now write a program in
O(n) time to duplicate this list. That is, write a program which will create a
copy of this list.

Solution: Time: O(n) Space: O(1)
Algorithm:
    The complication here as to why we can't simply copy the list is that the
    random pointer might be pointing to a future node and even if it points to 
    a past node, we would have to traverse from starting to find the past node
    which is not guaranteed to have a unique label.
    
    1) Pass 1: Create copies of the original nodes and link the copy nodes next to
    their original nodes
    
                v-------------.
    e.g) 1  ->  2  ->  3  ->  4
         |-------------^
         
Copy:                  v---------------------------.
         1  ->  1  ->  2  ->  2  ->  3  ->  3  ->  4  ->  4
         |---------------------------^  
         
    2) Pass 2: Traverse the joint list and assign the random pointer of the
    copied nodes to the original nodes random pointer's next value, which is
    essentially a copy of the node pointed by the random pointer
    
Random:                       |---------------------------- 
                       v------v--------------------.      | 
         1  ->  1  ->  2  ->  2  ->  3  ->  3  ->  4  ->  4
         |------|--------------------^      ^
                |---------------------------|
    
    3) Pass 3: Seperate the original list from that of the copied list
    
                        v-------------.
Original         1  ->  2  ->  3  ->  4
                 |-------------^
         
                    v-------------.
Copy        1  ->  2  ->  3  ->  4
            |-------------^
'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        iterator = head
        # Make copies of nodes of list and attach it to its original nodes
        while iterator:
            copy_iterator = RandomListNode(iterator.label)
            copy_iterator.next = iterator.next
            iterator.next = copy_iterator
            iterator = iterator.next.next
        iterator = head
        while iterator:
            # Link the random pointer to its own copy
            iterator.next.random = iterator.random.next if iterator.random else None
            iterator = iterator.next.next
        iterator = head
        copy_head = ListNode(0)
        copy_head.next = None
        copy_iterator = copy_head
        # Seperate the copy list from original list
        while iterator is not None:
            copy_iterator.next = iterator.next
            copy_iterator = copy_iterator.next
            iterator.next = iterator.next.next
            iterator = iterator.next
        return copy_head.next