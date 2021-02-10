#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        templist = []
        ans = 1
        temp_len = 0
        templist.append(s[0])
        for i in range(1, len(s)):
            templist.append(s[i])
            for m in range(len(templist)-1):
                if templist[-1] == templist[m]:
                    for n in range(m+1):
                        del templist[0]

                    break

            temp_len = len(templist)
            ans = max(ans, temp_len)

        return ans

            

        
# @lc code=end

