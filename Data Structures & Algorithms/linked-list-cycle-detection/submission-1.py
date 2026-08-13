# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = []
        s1 = set(s)
        while head:
            if head in s1: 
                return True
            else: 
                s1.add(head)
                head = head.next
        return False

#make a set, store all the nodes in there


