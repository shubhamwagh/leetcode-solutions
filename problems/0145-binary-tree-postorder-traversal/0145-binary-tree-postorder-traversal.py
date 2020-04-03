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
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.result.append(root.val)
        return self.result