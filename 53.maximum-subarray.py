#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (45.31%)
# Likes:    5918
# Dislikes: 248
# Total Accepted:    730.9K
# Total Submissions: 1.6M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)

        tmp_list = []
        for i in range(len(nums)):
            if nums[i] > 0:
                tmp = nums[i]
                tmp_list.append(tmp)
                for m in range(1, len(nums)-i):

                    tmp += nums[i+m]
                    tmp_list.append(tmp)
                    if tmp > nums[i+m]:
                        continue
                    else:
                        break

        return max(tmp_list)
            
        
# @lc code=end

