#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1 : i+1] and (len(w)-i == 1 or d[i-len(w)]):
                    d[i] = True
        return d[-1]
# @lc code=end

