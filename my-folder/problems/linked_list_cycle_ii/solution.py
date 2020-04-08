# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        fast = slow = head
        
        while fast and fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
            if slow == fast:
                while slow !=head:
                    slow = slow.next
                    head = head.next
                return slow    


        return None    
        
        
        

            
        
        
        
        
        