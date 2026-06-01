class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #bs = mid = x + y - x/2
        
        numx = nums1 + nums2
        numx.sort()
        
        n = len(numx)
        if n % 2 == 0:
            return ((numx[(n - 1)//2] + numx[((n - 1)//2) + 1])/2)
        else:
            return (numx[(n-1)//2])

        