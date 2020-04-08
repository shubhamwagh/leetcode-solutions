# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        result = head
        count = 0
        while head.next is not None:
            head = head.next
            count+=1
        
        if count % 2 ==0:
            middle = count // 2
        else:
            middle = count // 2 + 1
        print(middle)
        for i in range(0, middle):
            result = result.next
            
        return result   
        
#         fast = slow = head
        
#         while fast and fast.next:
#             fast, slow = fast.next.next, slow.next
            
#         return slow     
        
        
        