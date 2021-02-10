#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left_index, right_index = 0, len(height)-1
        left_max, right_max = height[left_index], height[right_index]
        rain_water = 0
        while left_index < right_index:
            if left_max <= right_max:
                rain_water = rain_water + left_max - height[left_index]
                left_index += 1
                left_max = max(left_max, height[left_index])

            else:
                rain_water = rain_water + right_max - height[right_index]
                right_index -= 1
                right_max = max(right_max, height[right_index])

        return rain_water

        
# @lc code=end

