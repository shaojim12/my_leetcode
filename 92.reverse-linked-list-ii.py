#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if  m == n:
            return head
        ohead = left = right = head

        for i in range(n-m):
            right = right.next

        for i in range(m-1):
            ohead = left
            left, right = left.next, right.next

        node = right.next

        for j in range(n-m+1):
            nxt = left.next
            left.next = node
            node = left
            left = nxt

        print(node)
        if m > 1:
            ohead.next = node
            return head
        else:
            return node
        

# @lc code=end

