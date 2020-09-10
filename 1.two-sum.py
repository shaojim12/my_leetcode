#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for m in range(i+1, len(nums)):
                sum = nums[i] + nums[m]
                if sum == target:
                    break

            if sum == target:
                    break
        return [i, m]            
                

# @lc code=end

