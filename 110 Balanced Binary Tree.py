# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)

        return abs(leftDepth - rightDepth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getDepth(self, root) -> int:
        if root == None:
            return 1
        else:
            return 1 + max(self.getDepth(root.right), self.getDepth(root.left))
