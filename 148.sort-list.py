#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        start = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(start)
        return self.merge(l, r)

    
    def merge(self, l, r):
        if not l or not r:
            return l or r
            
        if l.val > r.val:
            l, r = r, l

        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                pre.next = l
                l = l.next
            else:
                pre.next = r
                r = r.next

            pre = pre.next

        pre.next = l or r
        return head
        
# @lc code=end

