#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_stack = []
        l2_stack = []

        while l1:
            l1_stack.append(l1.val)
            l1 = l1.next

        while l2:
            l2_stack.append(l2.val)
            l2 = l2.next

        digit = 0
        carry = 0
        head = None
        while (l1_stack or l2_stack or carry == 1):
            if not (l1_stack or l2_stack):
                digit = 0
            elif not l1_stack:
                digit = l2_stack.pop()
            elif not l2_stack:
                digit = l1_stack.pop()
            else:
                digit = (l1_stack.pop() + l2_stack.pop())

            head_new = ListNode(val = (digit + carry) % 10)
            carry = (digit + carry) // 10
            head_new.next = head
            head = head_new

        return head

            
# @lc code=end

