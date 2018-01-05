'''
LeetCode: Split Linked List in Parts

Given a (singly) linked list with head node root, write a function to split the
 linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should
have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts
occurring earlier should always have a size greater than or equal parts
occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input: 
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2,
\root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a
ListNode is [].
Example 2:
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1,
and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].

Solution: Time: O(n) Space: O(1)
Algorithm:
    1) Iterate once through the entire list to determine the size of the list
    2) Keep track of how much excess k is over the size (0 if k <= size)
    3) We have to now split "size" elements into "k" groups. Construct an array
    which keeps track of the size of each group (inited to size // k)
    4) Determine the remainder of the size which has to be distributed amongst
    the k groups
    5) Distribute the remainder amongst the elements of the size array
    e.g) k = 3, size = 11 then size array = [3, 3, 3]
    Distribute remainder = 2 amongst size array elements: [4, 4, 3]
    6) Init a return list to empty and an iterator to the root
    7) Repeat for all the elements in the size array:
        i) Init a dummy list head node and a dummy list iterator
        ii) Repeat for the length specified by the current element in the size
        array:
            a) Link the iterator to the dummy list iterator
            b) update both the dummy list iterator and the main iterator
        iii) Update the dummy list iterator.next to None and append the dummy
        list head node.next to the return list
    8) We have to now take care of the case where k > size (where excess k > 0)
    Append "excess k" number of Nones into the return list
    9) Return the return list
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        size = 0
        iterator = root
        while iterator:
            size += 1
            iterator = iterator.next
        k_excess = max(k - size, 0)
        sizes = [size//k for i in range(k - k_excess)]
        rem_k = size % k
        for i in range(rem_k):
            sizes[i] += 1
        return_list = []
        iterator = root
        for i in range(len(sizes)):
            list_head = ListNode(0)
            list_head.next = None
            list_iter = list_head
            for j in range(sizes[i]):
                list_iter.next = iterator
                iterator = iterator.next
                list_iter = list_iter.next
            list_iter.next = None
            return_list.append(list_head.next)
        for i in range(k_excess):
            return_list.append(None)
        return return_list
                
            
            
        
        