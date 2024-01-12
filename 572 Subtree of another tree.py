#Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        if root == None or subRoot == None:
            return root == subRoot

        else:
            root_is_subTree = (self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right,  subRoot.right) and root.val == subRoot.val)
            root_has_subTree_bellow = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,  subRoot)
            return root_is_subTree or root_has_subTree_bellow


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q != None and p != None:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right and p.val == q.val
        
        else: 
            return q == p
