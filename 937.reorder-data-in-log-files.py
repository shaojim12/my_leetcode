#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_list = []
        alpha_list = []

        for log in logs:
            if log.split()[1].isdigit():
                digit_list.append(log)
            else:
                alpha_list.append(log)

        alpha_list.sort() 
        alpha_list.sort(key = lambda x: x.split()[1:])  
        #alpha_list.sort(key= lambda x: x.split(" ", 1))

        return alpha_list + digit_list



        


# @lc code=end

