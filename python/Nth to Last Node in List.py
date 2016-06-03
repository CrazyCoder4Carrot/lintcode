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
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        # write your code here
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        while fast and slow:
            fast = fast.next
            slow = slow.next
        return slow
        Nth to Last Node in List