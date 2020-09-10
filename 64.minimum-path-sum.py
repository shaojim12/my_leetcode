#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid)-1, len(grid[0])-1

        for i in range(rows-1, -1, -1):
            grid[i][columns] = grid[i+1][columns] + grid[i][columns]

        for j in range(columns-1, -1, -1):
            grid[rows][j] = grid[rows][j+1] + grid[rows][j]

        for m in range(rows-1, -1, -1):
            for n in range(columns-1, -1, -1):
                grid[m][n] = grid[m][n] + min(grid[m+1][n], grid[m][n+1])

        return grid[0][0]

        
# @lc code=end

