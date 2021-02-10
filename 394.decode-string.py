#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:

        stack = []; curNum = 0; curString = ""

        for c in s:
            if c == "[":
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0

            elif c == "]":

                num = stack.pop()
                PrevString = stack.pop()
                curString = PrevString + num*curString

            elif c.isdigit():
                curNum = curNum*10 + int(c)

            else:
                curString += c

        return curString


        
# @lc code=end

