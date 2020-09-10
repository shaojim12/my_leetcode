#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums)-1

        while l < r:
            while l < r and nums[l] == nums[r]:
                l += 1

            mid = l + (r-l)//2
            
            if nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid

        return nums[l]
# @lc code=end

