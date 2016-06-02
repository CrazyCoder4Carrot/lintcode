"""
932ms version
insert node in the same list
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        # write your code here
        cur = head
        index = head
        tempmax = head.val
        while index.next:
            if tempmax < index.next.val:
                index = index.next
                tempmax = index.val
                continue
            cur = head
            if cur.val > index.next.val:
                temp = index.next
                index.next = index.next.next
                head = temp
                temp.next = cur
                continue
            while cur.next and cur != index and cur.next.val < index.next.val:
                cur = cur.next
            if cur:
                if cur == index:
                    index = index.next
                    continue
                else:
                    temp = index.next
                    index.next = index.next.next
                    temp.next = cur.next
                    cur.next = temp
        return head
"""
645 ms
convert list to array, sort the array then convert it to the list
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        # write your code here
        cur = head
        temp = []
        while cur:
            temp.append(cur.val)
            cur = cur.next
        cur = head
        temp.sort()
        i = 0
        while cur:
            cur.val = temp[i]
            i += 1
            cur = cur.next
        return head
"""
"""