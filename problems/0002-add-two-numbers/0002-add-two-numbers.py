# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = result = ListNode(0)
        print(result)
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                
                carry += l1.val
                l1 = l1.next
            
            if l2:
                
                carry += l2.val
                l2 = l2.next
            
            result.val = carry % 10
            carry = carry // 10
            
            if l1 or l2 or carry:
                result.next = ListNode(0)
                result = result.next
        return head