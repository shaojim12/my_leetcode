#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx-1] + n

        result = len(nums) + 1
        left = 0
        for right, n in enumerate(nums):
            if n >= s:
                left = self.findleft(left, right, nums, s, n)
                result = min(result, right-left+1)

        return result if result <= len(nums) else 0

    def findleft(self, left, right, nums, s, n):
        while left < right:
            mid = left + (right-left)//2
            if (n - nums[mid]) >= s:
                left = mid + 1
            else:
                right = mid
        return left

# @lc code=end

