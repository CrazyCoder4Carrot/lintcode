"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
"""
Naive version failed. 
O(N*N) complexity
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        i = 0
        while i in range(len(lists)):
            if lists[i] == None:
                lists.remove(None)
            i += 1
        head = ListNode(-1)
        cur = head
        while lists:
            index = 0
            minval = sys.maxint
            i = 0
            while i in range(len(lists)):
                if lists[i].val < minval:
                    minval = lists[i].val
                    index = i
                i += 1
            cur.next = ListNode(minval)
            cur = cur.next
            lists[index] = lists[index].next
            if lists[index] == None:
                lists.remove(None)
        return head.next
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here

        lists = filter(lambda x: x != None, lists)
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        end = len(lists) - 1
        while end > 0 :
            start = 0
            while start < end:
                lists[start] = self.merge(lists[start], lists[end])
                start += 1
                end -= 1
        return lists[0]
    def merge(self, a, b):
        head = ListNode(0)
        cur = head
        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
            cur.next = None
        if not a:
            cur.next = b
        if not b:
            cur.next = a
        return head.next
                