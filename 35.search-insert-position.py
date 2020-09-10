#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (41.36%)
# Likes:    1724
# Dislikes: 212
# Total Accepted:    498.2K
# Total Submissions: 1.2M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            if nums[0] > target:
                return 0
            elif nums[len(nums)-1] < target:
                return len(nums)
            else:
                for i in range(len(nums)-1):
                    if nums[i] < target and  target < nums[i+1]:
                        return i+1

        return nums.index(target)
        
# @lc code=end

