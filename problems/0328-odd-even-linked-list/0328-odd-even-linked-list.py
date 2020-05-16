# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        oh = ListNode()
        eh = ListNode()
        
        fo = oh
        fe = eh
        
        odd = True
        
        while head:
            if odd:
                fo.next = head
                fo = fo.next
            else:
                fe.next = head
                fe = fe.next
            
            odd = not odd
            head = head.next
        fe.next = None
        fo.next = eh.next
        return oh.next