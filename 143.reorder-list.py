#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        bottom_list = None
        after = curr.next
        while after:
            curr.next = bottom_list
            bottom_list = curr
            curr = after
            after = after.next
        curr.next = bottom_list

        new_head = temp_head = ListNode()
        while curr:
            temp_head.next = head
            head = head.next
            temp_head.next.next = curr
            curr = curr.next
            temp_head = temp_head.next.next

        if head:
            temp_head.next = head
        
        return new_head.next


# @lc code=end

