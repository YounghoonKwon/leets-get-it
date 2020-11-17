class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
 
        newArr = nums1 + nums2
        newArr.sort() 
 
        x = len(newArr) // 2
        y = len(newArr) % 2
        ans = 0
 
        if(y == 0) :
            ans = (newArr[x]+newArr[x-1])/2
        else :
            ans = newArr[x]
 
        return ans
        
