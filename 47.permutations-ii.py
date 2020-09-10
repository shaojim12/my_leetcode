#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.dfs(nums, [], result)
        return result
    
    def dfs(self, nums, path, result):
        if not nums:
            result.append(path)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], result)
# @lc code=end

