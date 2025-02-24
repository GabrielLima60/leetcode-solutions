'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.aux(root, float('-inf'), float('inf'))

    def aux(self, root, min_val, max_val):
        if root is None:
                return True
        elif root.val <= min_val or root.val >= max_val:
            return False
            
        else:
            return self.aux(root.left, min_val, root.val) and self.aux(root.right, root.val, max_val)
