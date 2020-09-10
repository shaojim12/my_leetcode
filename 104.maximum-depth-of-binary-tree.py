#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth_num = 0
        if root == None:
            return depth_num
        else:
            depth_num += 1
            return max(self.caldepth(root.left, depth_num), self.caldepth(root.right, depth_num))

    def caldepth(self, root, depth_num):
        if root == None:
            return depth_num
        else:
            depth_num += 1
            return max(self.caldepth(root.left, depth_num), self.caldepth(root.right, depth_num))

# @lc code=end

