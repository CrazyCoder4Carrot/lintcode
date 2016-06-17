"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def countval(self, hashTable, res):
        count = 0
        for val in hashTable:
            if val:
                cur = val
                while cur:
                    res.append(cur.val)
                    count += 1
                    cur = cur.next
        return count
    def rehashing(self, hashTable):
        # write your code here
        if not hashTable:
            return []
        res = []
        count = self.countval(hashTable, res)
        if count >= len(hashTable) / 10:
            hashTable = [None for _ in range(2 * len(hashTable))]
            temp = [None for _ in range(2 * len(hashTable))]
        else:
            temp = [None for _ in range(len(hashTable))]
        capacity = len(hashTable)
        for val in res:
            if not hashTable[val % capacity]:
                hashTable[val % capacity] = ListNode(val)
                temp[val % capacity] = hashTable[val % capacity]
            else:
                temp[val % capacity].next = ListNode(val)
                temp[val % capacity] = temp[val % capacity].next
        return hashTable
        