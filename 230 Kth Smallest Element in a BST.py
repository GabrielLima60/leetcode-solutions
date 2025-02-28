'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 
        self.k = k
        self.answer = None
        self.aux(root)

        return self.answer

    def aux(self, node):
        if node is None:
            return 

        self.aux(node.left)

        self.k -= 1

        if self.k == 0:
            self.answer = node.val
            return 
        
        self.aux(node.right)
