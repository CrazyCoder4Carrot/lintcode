# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        dummyhead = RandomListNode(1)
        curnew = dummyhead
        cur = head
        while cur:
            curnew.next = RandomListNode(cur.label)
            curnew = curnew.next
            curnew.random = cur.random
            cur = cur.next
        return dummyhead.next