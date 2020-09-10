#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dict = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n not in self.dict:
            self.dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.dict[n]

# @lc code=end

