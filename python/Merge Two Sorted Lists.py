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


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
Running time:  2616ms
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
        cur1 = l1
        cur2 = l2
        if cur1.val < cur2.val:
            head = ListNode(cur1.val)
            cur1 = cur1.next
        else:
            head = ListNode(cur2.val)
            cur2 = cur2.next
        cur = head
        while cur and (cur1 or cur2):
            temp = 0
            if not cur1:
                cur.next = cur2
                break
            if not cur2:
                cur.next = cur1
                break
            if cur1.val < cur2.val:
                temp = cur1.val
                cur1 = cur1.next
            else:
                temp = cur2.val
                cur2 = cur2.next
            cur.next = ListNode(temp)
            cur = cur.next
        return head