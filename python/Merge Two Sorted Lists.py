"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if not l1:
            return l2
        if not l2:
            return l1
        cur = l1
        temp = []
        while cur:
            temp.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            temp.append(cur.val)
            cur = cur.next
        temp.sort()
        head = ListNode(temp[0])
        cur = head
        for val in temp[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return head