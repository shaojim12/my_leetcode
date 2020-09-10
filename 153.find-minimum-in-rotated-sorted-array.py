#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l)//2

            while l < mid and nums[l] > nums[mid]:
                l += 1
                if nums[l] < nums[mid]:
                    return nums[l]

            if nums[l] <= nums[mid] and nums[l] <= nums[r]:
                return nums[l]
            else:
                l = mid + 1

# @lc code=end

