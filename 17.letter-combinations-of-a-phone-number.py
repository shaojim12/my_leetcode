#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_map = {"0": " ", 
            "1": "",
            "2":"abc", 
            "3":"def", 
            "4":"ghi", 
            "5":"jkl", 
            "6":"mno", 
            "7":"pqrs", 
            "8":"tuv", 
            "9":"wxyz"}

        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return list(key_map[digits[0]])

        prev = self.letterCombinations(digits[:-1])
        additional = key_map[digits[-1]]
        #print(prev)
        #print(additional)

        return [s + c for s in prev for c in additional]
# @lc code=end

