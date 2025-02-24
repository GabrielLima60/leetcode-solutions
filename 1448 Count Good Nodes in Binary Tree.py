'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = []
        self.aux(root, root.val, good_nodes)

        return len(good_nodes)

    def aux(self, root, min_val, good_nodes):
        if root is None:
            return 

        elif root.val >= min_val:
            good_nodes.append(['a'])
            self.aux(root.left, root.val, good_nodes)
            self.aux(root.right, root.val, good_nodes)
        else:
            self.aux(root.left, min_val, good_nodes)
            self.aux(root.right, min_val, good_nodes)     
