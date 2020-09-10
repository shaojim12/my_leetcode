#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans, total, tmp_list = [], 0, []
        self.dfs(candidates, target, ans, total, tmp_list, 0)
        return ans

    def dfs(self, num_list, target, ans, total, ans_list, index):
        if int(total) == target:
            ans.append(ans_list)
            return
        if int(total) > target:
            return
        
        if total < target:
           for i in range(index, len(num_list)):
               self.dfs(num_list, target, ans, total+num_list[i], ans_list+[num_list[i]], i)

# @lc code=end

