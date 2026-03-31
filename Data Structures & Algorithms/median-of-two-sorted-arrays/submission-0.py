class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        mergerd = nums1 +nums2
        mergerd.sort()

        totalLen = len(mergerd)

        if totalLen % 2 == 0:
            output = (mergerd[totalLen // 2-1] + mergerd[totalLen // 2])/2
            return output
        else:
            return mergerd[totalLen // 2]