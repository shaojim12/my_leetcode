#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_than_x = []
        greater_than_x = []
        while head:
            if head.val < x:
                less_than_x.append(head.val)
            else:
                greater_than_x.append(head.val)

            head = head.next

        head = None

        while (less_than_x or greater_than_x):
            if greater_than_x:
                new_head = ListNode(greater_than_x.pop())
            else:
                new_head = ListNode(less_than_x.pop())

            new_head.next = head
            head = new_head

        return head
# @lc code=end

