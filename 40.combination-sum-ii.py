#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.dfs(candidates, 0, [], result, target)
        return result


    def dfs(self, nums, index, path, result, target):
        if target == 0:
            result.append(path)
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            if nums[i] > target:
                return

            self.dfs(nums, i+1, path + [nums[i]], result, target - nums[i])

# @lc code=end

