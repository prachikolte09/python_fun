# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.



# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5



# a=[2,6,8,9]
# b=[3,7,,10,11]
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge = nums1 + nums2
        merge.sort()
        d = int(((len(merge)) / 2))
        if len(merge) % 2 == 0:

            m = float(merge[d - 1] + merge[d]) / 2
        else:
            m = (merge[d])
            
        return(m)		