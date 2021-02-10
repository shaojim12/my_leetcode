#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        status_dict = {}
        stack = []

        # only add the mark to dictionary, if the parenthesis is valid
        for index, ch in enumerate(s):
            if ch == "(":
                stack.append(index)
            elif ch == ")" and stack:
                status_dict[index] = True
                status_dict[stack[-1]] = True
                stack.pop()

        answer = ""
        for ind, c in enumerate(s):
            if (c == "(" or c == ")") and (ind not in status_dict):
                continue
            else:
                answer += c

        return answer


# @lc code=end

