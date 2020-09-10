#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        a = list(a)
        b = list(b)

        while a != [] or b != [] or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            carry, tmp = divmod(carry, 2)
            result += str(tmp)

            if not (a or b):
                if carry == 0:
                    break
                else:
                    result += str(carry)
                    break

        return result[::-1]


# @lc code=end
