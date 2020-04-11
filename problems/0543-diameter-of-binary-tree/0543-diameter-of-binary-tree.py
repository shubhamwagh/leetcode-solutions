# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def height(root):
            if root==None:
                return 0
            l_tree = root.left
            r_tree = root.right
            l_height = r_height = 0
            if l_tree != None:
                l_height = height(l_tree)
            if r_tree!=None:
                r_height = height(r_tree)
        
            return 1 + max(l_height, r_height)
            
        
        if root == None:
            return 0
        
        l_tree_height = height(root.left)
        r_tree_height = height(root.right)
        
        l_diameter_tree = self.diameterOfBinaryTree(root.left)
        r_diameter_tree = self.diameterOfBinaryTree(root.right)
        return max(l_tree_height + r_tree_height, max(l_diameter_tree, r_diameter_tree))