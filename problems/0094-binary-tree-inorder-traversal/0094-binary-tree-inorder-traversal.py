# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = []
        self.stack = []
        
    def inorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        
        if root == None:
            return
        
        self.inorderTraversal(root.left)
        self.result.append(root.val)
        self.inorderTraversal(root.right)
        return self.result
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root == None:
            return        
        while True:
            if root != None:
                self.stack.append(root)
                root = root.left
            else:
                if len(self.stack)!=0:
                    root = self.stack.pop()
                    self.result.append(root.val)
                    root = root.right
                else:
                    break
        return self.result