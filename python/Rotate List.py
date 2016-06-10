# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        if not head or not head.next:
            return head
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        k = k % count
        if not k:
            return head
        cur = head
        while k and cur.next:
            cur = cur.next
            k-=1
        if k:
            return head
        pre = head
        while pre and cur.next:
            pre = pre.next
            cur = cur.next
        temp = head
        head = pre.next
        pre.next = None
        cur.next = temp
        return head
        