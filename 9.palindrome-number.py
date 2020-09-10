#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (46.08%)
# Likes:    1807
# Dislikes: 1449
# Total Accepted:    761.2K
# Total Submissions: 1.7M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        count = 0
        tmp_x = x
        while tmp_x >= 1:
            tmp_x /= 10
            count += 1

        tmp_z = 0

        if (count % 2) == 0:
            for i in range(int(count/2)): 
                pop = x % 10
                x = int(x / 10)
                tmp_z = tmp_z*10 + pop

        elif (count % 2) == 1:
            for i in range(int((count-1)/2)):
                pop = x % 10
                x = int(x / 10)
                tmp_z = tmp_z*10 + pop
            x = int(x / 10) 


        return (tmp_z == x) and count > 0 or x == 0
        
# @lc code=end

