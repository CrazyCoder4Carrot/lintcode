"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if not head:
            return head
        cur = head
        slow = head
        fast = head.next
        if not slow or not fast:
            return head
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
        l2 = slow.next
        slow.next = None
        l2 = self.reverse(l2)
        while cur and l2:
            temp1 = cur.next
            temp2 = l2.next
            cur.next = l2
            l2.next = temp1
            cur = temp1
            l2 = temp2
            
        return head
    def reverse(self, head):
        pre = None
        cur = head
        if not head or not head.next:
            return head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre