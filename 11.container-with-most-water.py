#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        i = 0
        j = len(height)-1

        while i < j:
            area = min(height[i], height[j]) * (j-i)

            if area > maxarea:
                maxarea = area

            elif height[i] > height[j]:
                j -= 1
            
            else:
                i += 1

        return maxarea
# @lc code=end

