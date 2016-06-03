"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        slow = head
        fast = slow.next
        while n and fast:
            fast = fast.next
            n-= 1
        while slow and fast:
            slow = slow.next
            fast = fast.next
        if slow == head:
            head = head.next
            return head
        slow.next = slow.next.next
        return head