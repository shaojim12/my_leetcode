#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (33.48%)
# Likes:    1199
# Dislikes: 1613
# Total Accepted:    548.8K
# Total Submissions: 1.6M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        if needle == "":
            return 0
        
        for i in range(len(haystack)-len(needle)+1):
            for m in range(len(needle)):
                if haystack[i+m] != needle[m]:
                    break
                elif m == len(needle)-1:
                    return i
        return -1
        '''
        if needle not in haystack:
            return -1

        return haystack.index(needle)
# @lc code=end

