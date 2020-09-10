#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.82%)
# Likes:    1147
# Dislikes: 1938
# Total Accepted:    491.1K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
#
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
#

# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.append(0)
        print(digits)
        if digits[-2] == 9:
            for i in range(len(digits)-1):
                if digits[-i-2] == 9:
                    digits[-i-2] = 1
                    digits[-i-1] = 0
                else:
                    digits[-i-2] += 1
                    digits[-i-1] = 0
                    return digits[:-1]
            return digits
        else:
            digits[-2] += 1
            return digits[:-1]


# @lc code=end
