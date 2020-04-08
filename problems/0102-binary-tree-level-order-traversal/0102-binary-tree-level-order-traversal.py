# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        
        
        result = []
        if root==None:
            return result
        
        queue = collections.deque([root])
        while len(queue) !=0:
            level_list = []
            queue_size = len(queue)
            for i in range(0, queue_size):
                val = queue.popleft()
                level_list.append(val.val)
                
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
            result.append(level_list)        
                    
        return result