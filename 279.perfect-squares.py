#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:        
        square_nums = []
        i = 1
        while i * i <= n:
            square_nums.append(i * i)
            i += 1

        count = 0
        tocheck = {n}

        while tocheck:
            count += 1
            temp = set()
            for x in tocheck:
                for y in square_nums:
                    if x == y:
                        return count
                    if x < y:
                        break
                    temp.add(x - y)

            tocheck = temp

# @lc code=end

