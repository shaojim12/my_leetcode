#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.findKth(nums1, nums2, l//2)
        else:
            return (self.findKth(nums1, nums2, l//2 -1 ) + self.findKth(nums1, nums2, l//2)) / 2



    def findKth(self, A, B, k):
        if not A:
            return B[k]

        i = len(A) // 2
        j = k - i

        if A[i] > B[j]:
            return self.findKth(A[:i],B[j:],i)
        else:
            return self.findKth(A[i:],B[:j],j)




# @lc code=end

