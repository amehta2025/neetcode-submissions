# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next  #second half of list starts at slow.next
        slow.next = None
        prev = None
        while second:  #reversing the second portion of the list
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        

        #now we merge the two halves
        second = prev #because second is gonna be null, but prev is gonna house n-1
        first = head
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        



            


#slow pointer and fast pointer; with odd nodes, second half of the list is smaller half of odd list
#so pointers should be at beginning and end of linkedlist