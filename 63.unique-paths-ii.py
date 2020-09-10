#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows, columns = len(obstacleGrid), len(obstacleGrid[0])


        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]


        for i in range(1, columns):
            obstacleGrid[0][i] = obstacleGrid[0][i - 1] * (1 - obstacleGrid[0][i])
        
        for j in range(1, rows):
            obstacleGrid[j][0] = obstacleGrid[j-1][0] * (1 - obstacleGrid[j][0])

        for m in range(1, rows):
            for n in range(1, columns):
                obstacleGrid[m][n] = (obstacleGrid[m-1][n] + obstacleGrid[m][n-1]) * (1 - obstacleGrid[m][n])

        return obstacleGrid[-1][-1] 
# @lc code=end

