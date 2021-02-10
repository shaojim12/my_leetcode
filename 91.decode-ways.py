#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if 0 < int(s[0]) <= 9 else 0

        for i in range(1, len(s)):
            print(i)
            dp[i+1] = dp[i] if 0 < int(s[i]) <= 9 else 0

            dp[i+1] += dp[i-1] if 10 <= (int(s[i]) + int(s[i-1])*10)  <= 26 else 0

        return dp[-1]
  
        
# @lc code=end

