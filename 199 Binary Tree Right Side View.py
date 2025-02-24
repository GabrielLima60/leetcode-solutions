'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        node_right_side = {} 
        self.aux(root, 0, node_right_side)

        return list(node_right_side.values())

    def aux(self, root, level, node_right_side):
        if root is None:
            return

        node_right_side[level] = root.val
        self.aux(root.left, level + 1, node_right_side)
        self.aux(root.right, level + 1, node_right_side)
