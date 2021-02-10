#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1]
        right = [1]
        ans = []

        for i in range(1, len(nums)):
            left += [nums[i-1] * left[i-1]]
            right += [nums[-i] * right[i-1]]

        for m in range(len(nums)):
            ans += [left[m] * right[-m-1]]

        return ans

# @lc code=end

