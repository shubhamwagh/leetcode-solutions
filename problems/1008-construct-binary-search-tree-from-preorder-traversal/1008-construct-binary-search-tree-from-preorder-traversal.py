# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#     def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
#         inorder = sorted(preorder)
#         return self.construct_binary_search_tree(preorder, inorder)
    
#     def construct_binary_search_tree(self, preorder, inorder):
        
#         lengthpre = len(preorder)
#         lengthin = len(inorder)
        
#         if lengthpre!=lengthin or lengthpre ==0 or preorder==None or inorder==None:
#             return None
        
#         root = TreeNode(preorder[0])
#         root_index = inorder.index(root.val)
        
#         root.left = self.construct_binary_search_tree(preorder[1:root_index+1], inorder[:root_index])
#         root.right = self.construct_binary_search_tree(preorder[root_index+1:], inorder[root_index+1:])
#         return root
    def insert(self, node, i):
        # print(node, i)
        if node is None:
            node = TreeNode(i)
        elif node.val > i:
            node.left = self.insert(node.left, i)
        elif node.val < i:
            node.right = self.insert(node.right, i)
        return node
    
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        node = root
        for i in preorder[1:]:
            self.insert(root, i)
        return root