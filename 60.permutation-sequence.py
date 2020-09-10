#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        all_nums = []
        for m in range(1, n+1):
            all_nums.append(m)
        result = ['']
        self.dfs(all_nums, k, result)
        return result[0]

    def dfs(self, all_nums, k, result):
        if not all_nums:
            return

        total_num = 1
        for i in range(len(all_nums)-1):
            total_num = total_num * (i+1)

        if (k % total_num) > 0:
            res_num = int(k / total_num)
        elif (k % total_num) == 0:
            res_num = int(k / total_num) - 1
            
        result[0] = result[0] + str(all_nums[res_num])
        del all_nums[res_num]

        self.dfs(all_nums, k-(res_num*total_num), result)

# @lc code=end

