class Solution:
    def removeElement(nums,val) -> int:
        k = 0
        nums.sort()
        for x in nums:
            if val == x:
                k += 1
        
        while k >= 1:
            nums.remove(val)
            k -= 1
        print(nums)


        return k
    
print(Solution.removeElement([0,1,2,2,3,0,4,2],2))