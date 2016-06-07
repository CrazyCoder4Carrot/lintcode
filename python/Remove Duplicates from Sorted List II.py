"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head:
            return None
        if not head.next:
            return None
        res = ListNode(0)
        cur = res
        pos = head.next
        while pos:
            if head.val != pos.val:
                cur.next = head
                head = head.next
                pos = pos.next
                cur = cur.next
            else:
                while pos and head.val == pos.val:
                    pos = pos.next
                if not pos:
                    break
                else:
                    head = pos
                    pos = pos.next
        if head.next == pos:
            cur.next = head
        else:
            cur.next = None
        return res.next
            