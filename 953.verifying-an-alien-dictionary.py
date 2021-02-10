#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        aldict = {}
        for i, element in enumerate(order):
            aldict[element] = i

        for i in range(1, len(words)):
            pre, cur = words[i-1], words[i]

            for m in range(min(len(pre), len(cur))):
                if aldict[pre[m]] < aldict[cur[m]] and m < min(len(pre), len(cur)) - 1:
                    break
                elif aldict[pre[m]] == aldict[cur[m]] and m == min(len(pre), len(cur)) - 1:
                    if len(pre) > len(cur):
                        return False
                elif aldict[pre[m]] > aldict[cur[m]]:
                    return False
            
        return True

# @lc code=end

