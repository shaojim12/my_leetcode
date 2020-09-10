#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x <= 2 ** 31 - 1 and x >= 0:
            tmp = len(str(x))
            output = 0
            for i in range(tmp):
                remainder = x % 10
                x = int(x / 10)
                output = output*10 + remainder

        elif x < 0 and x >= -1 * (2 ** 31):
            x = x * -1
            tmp = len(str(x))
            output = 0 
            for i in range(tmp):
                remainder = x % 10
                x = int(x / 10)
                output = output*10 + remainder
            output = output * -1

        else:
            output = 0

        if output > 2 ** 31 - 1 or output < -1 * (2 ** 31):
            output = 0

        return output
        
# @lc code=end

