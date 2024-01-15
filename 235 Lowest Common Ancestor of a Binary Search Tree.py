#Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return False
        
        else: 
            if  self.isBellowOrEqual(root.left, p) and self.isBellowOrEqual(root.left, q):
                return self.lowestCommonAncestor(root.left, p, q)
            elif  self.isBellowOrEqual(root.right, p) and self.isBellowOrEqual(root.right, q):
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root 

    def isBellowOrEqual(self, root, target) -> bool:
        if root == None:
            return False
        elif root == target:
            return True
        else:
            return self.isBellowOrEqual(root.left, target) or self.isBellowOrEqual(root.right, target)
