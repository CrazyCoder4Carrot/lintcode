# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # Write your code here
        if not headA or not headB:
            return None
        cur = headA
        while cur:
            temp = cur.next
            cur.next = None
            cur = temp
        cur = headB
        while cur.next:
            cur = cur.next
        return cur