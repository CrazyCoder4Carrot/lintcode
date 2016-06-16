"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    
    def reverseBetween(self, head, m, n):
        # write your code here
        if not head or m >= n:
            return head
        dummyhead = ListNode(0, head)
        start = head
        pre = dummyhead
        m -= 1
        while m and start:
            m -= 1
            pre = start
            start = start.next
        end = dummyhead
        while n and end:
            n -= 1 
            end = end.next
        next = end.next
        end.next = None
        newhead = self.reverse(start)
        pre.next = newhead
        start.next = next
        return dummyhead.next
    def reverse(self, head):
        if not head or not head.next:
            return head
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
        
        