    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head, a ListNode
    # @oaram {int} v1 an integer
    # @param {int} v2 an integer
    # @return {ListNode} a new head of singly-linked list
    def swapNodes(self, head, v1, v2):
        # Write your code here
        if not head:
            return head
        dummyhead = ListNode("#")
        dummyhead.next = head
        ptr1 = dummyhead
        while ptr1.next and ptr1.next.val != v1:
            ptr1 = ptr1.next
        ptr2 = dummyhead
        while ptr2.next and ptr2.next.val != v2:
            ptr2 = ptr2.next
        if not ptr1.next or not ptr2.next:
            return head
        temp1 = ptr1.next
        temp2 = ptr2.next
        if temp2 == ptr1:
            ptr2.next = temp1
            temp = temp1.next
            temp1.next = temp2
            temp2.next = temp
        elif temp1 == ptr2:
            ptr1.next = temp2
            temp = temp2.next
            temp2.next = temp1
            temp1.next = temp
        else:
            ptr1.next = temp2
            ptr2.next = temp1
            temp = temp1.next
            temp1.next = temp2.next
            temp2.next = temp
        return dummyhead.next