'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.level_order = []
        self.aux(root, 1)
        return self.level_order

    def aux(self, root, level):
        if root is None:
            return
        
        if len(self.level_order) < level:
            self.level_order.append([root.val])
        else:
            self.level_order[level-1].append(root.val)

        self.aux(root.left, level + 1)
        self.aux(root.right, level + 1)
