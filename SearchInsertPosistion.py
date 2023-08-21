class Solution:
    def searchInsert(nums, target) -> int:
        print(nums)

        for x, y in enumerate(nums):
            if target == y:
                return(x)
            
            if target < y:
                return(x)
            
            if target > y:
                i = x +1
                
            else:
                return(len(nums))
        return i
                





t1 = 2
t2 = 5
t3 = 7

print(Solution.searchInsert([1,3,5,6], 7))