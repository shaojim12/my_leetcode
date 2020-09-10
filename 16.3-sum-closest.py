#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res_abs = 99999
        res = 0
        for i in range(len(nums)-2):

            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                total_abs = abs(nums[i]+nums[left]+nums[right]-target)
                if total == target:
                    return target

                elif total_abs < res_abs:
                    res_abs = total_abs
                    res = total

                elif total < target:
                    left += 1

                elif total > target:
                    right -= 1
        return res
                    

# @lc code=end

