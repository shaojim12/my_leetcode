#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        
        leftindex = self.findleftindex(left, right, nums, target)
        if leftindex == -1:
            return [-1, -1]
        rightindex = self.findrightindex(leftindex, right, nums, target)
        return [leftindex, rightindex]

    def findleftindex(self, left, right, nums, target):
        while left <= right:
            if nums[left] == target:
                return left
            else:
                left += 1
        return -1            

    def findrightindex(self, left, right, nums, target):
        while left <= right:
            if nums[right] == target:
                return right
            else:
                right -= 1
        return -1    
# @lc code=end

