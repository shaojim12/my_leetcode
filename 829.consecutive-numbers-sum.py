#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#

# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        answer = 0
        num_sqrt = (2 * N) ** 0.5
        for i in range(int(num_sqrt)):
            number = (N - (i * (i + 1) / 2)) / (i + 1)
            if (number % 1) == 0:
                answer += 1

        return answer


        
# @lc code=end

