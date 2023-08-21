class Solution:

    def __init__(self, nums) -> None:
        self.nums = nums
        pass
    def removeDuplicates(nums):

        nl = len(nums)
        nl = nl -1
        list = nums
        
        for x in range(nl):
            #print(nums[nl])
            #print("this is x: ", nums[x])
            for y in range(x + 1, nl+1):
                #print("this is y: ", nums[y])
                if nums[x] == nums[y]:
                    print("dup at: ", nums[y])
                    
                else:
                    print("good")
            

            

    
                
        return list
            
            
        

print(Solution.removeDuplicates([0,0,1,1,1,2,2,2,3,3,4]))

