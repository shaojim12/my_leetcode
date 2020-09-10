#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = []
        tmp = 1
        for m in range(n):
            tmp_list = []
            for i in range(n):
                tmp_list.append(tmp)
                tmp += 1
            res.append(tmp_list)

        return res


# @lc code=end

