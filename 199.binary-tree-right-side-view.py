#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        answers = []
        layers = 0
        self.collect(root, layers, answers)

        return answers

    def collect(self, node, layers, answers):
        if node:
            if layers == len(answers):
                answers.append(node.val)

            self.collect(node.right, layers+1, answers)
            self.collect(node.left, layers+1, answers)

            

# @lc code=end

