# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        temp = []
        cur = head
        while cur:
            temp.append(cur.val)
            cur = cur.next
        return temp == temp[::-1]