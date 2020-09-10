#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.leftans = [1]
        self.rightans = [1]
        
    def leftdepth(self, x, depth):
        if x.left == None:
            self.leftans.append(depth)
        else:
            self.leftdepth(x.left, depth+1)
        
        if x.right == None:
            self.leftans.append(depth)
        else:
            self.leftdepth(x.right, depth+1)

    def rightdepth(self, x, depth):
        if x.left == None:
            self.rightans.append(depth)
        else:
            self.rightdepth(x.left, depth+1)
        
        if x.right == None:
            self.rightans.append(depth)
        else:
            self.rightdepth(x.right, depth+1)
        '''  
        if x.left:
            self.depth(x.left, depth+1)
        if x.right:
            self.depth(x.right, depth+1)
        '''

    def isBalanced(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        print(root)
        if not root.left:
            pass
        else:
            self.leftdepth(root.left, 2)
            

        if not root.right:
            pass
        else:
            self.rightdepth(root.right, 2)
        if abs(max(self.leftans) - max(self.rightans)) > 1:
            return False
        else:
            return True


# @lc code=end

