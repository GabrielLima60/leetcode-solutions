'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_found = [root.val]
        self.aux(root, max_found)

        return max_found[0]

    def aux(self, root, max_found):
        if root is None:
            return 0


        left_side = max(self.aux(root.left, max_found), 0)
        right_side = max(self.aux(root.right, max_found), 0)
        final = root.val + left_side + right_side

        max_found[0] = max(max_found[0], final)
        return root.val + max(left_side, right_side)
