class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            pass
        elif n >= 1:
            i = n
            for x in range(n):
                print("x is: ",nums2[x],"i is:",nums1[m])
                nums1[m] = nums2[x]
                m += 1


        nums1.sort()
        print(nums1)


nums1 = [-1,0,0,3,3,3,0,0,0]
nums3 = [0,0,0,0,0]
nums4 = [1,2,3,4,5]


nums2 = [1,2,2]

m = 6
n = 3

s = Solution()
t = s.merge(nums3, 5, nums4, 0)