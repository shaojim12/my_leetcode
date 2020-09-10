#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        if x == 1:
            return 1
        while 1 :
            mid = (l + r)//2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid*mid:
                r = mid
            else:
                l = mid


# @lc code=end

