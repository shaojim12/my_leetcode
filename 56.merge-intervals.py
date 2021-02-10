#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return

        intervals.sort(key = lambda x:x[0])
        # sort the list by the first element
        ans_list = []
        i = 1

        while (i <= len(intervals)):
                if i == len(intervals):
                    ans_list.append(intervals[i-1])
                    return ans_list
                    # if i is on the end of the list
                    # append current interval
                    # then return the answer

                elif intervals[i-1][1] >= intervals[i][0]:
                    intervals[i] = [min(intervals[i-1][0], intervals[i][0]), max(intervals[i][1], intervals[i-1][1])]
                    i += 1
                    # if two intervals are overlapping
                    # let current intervel be the overlapping value, in this way we can ignore the previous interval

                else:
                    ans_list.append(intervals[i-1])
                    i += 1
                    # if two intervals are non-overlapping
                    # append previous interval

# @lc code=end

