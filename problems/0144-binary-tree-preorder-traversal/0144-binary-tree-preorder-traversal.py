# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.stack = []
        self.result = []
        
    def preorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        
        if root == None:
            return
        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.result
    
    def preorderTraversalIterative(self, root: TreeNode) -> List[int]:       
        if root == None:
            return
        self.stack.append(root)
        while len(self.stack) !=0:
            root = self.stack.pop()
            self.result.append(root.val)
            if root.right != None:
                self.stack.append(root.right)
            if root.left != None:
                self.stack.append(root.left)
        return self.result   
            
    def preorderTraversal(self, root: TreeNode) -> List[int]:       
        if root == None:
            return
        self.stack.append(root)
        while len(self.stack) !=0:
            root = self.stack.pop()
            self.result.append(root.val)
            if root.right != None:
                self.stack.append(root.right)
            if root.left != None:
                self.stack.append(root.left)
        return self.result