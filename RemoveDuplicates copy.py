class Solution:

    def __init__(self, nums) -> None:
        self.nums = nums
        pass
    def removeDuplicates(nums):

        k = 0
        v = -(len(nums))
        newList = []

        if len(nums) == 1:
            return 1
        elif len(nums) == 2 and nums[0] == nums[1]:
            return 1    
        else:
            for x, y in enumerate(nums):
                #print("this is x: ", k, "this is val: ",nums[v] , 'This is y: ', y)
                k+=1
                v+=1
                #print(nums[x-1])
                if y == nums[v]:

                    #print(y)
                    i = y
                    newList.append(i)

            if len(newList) == len(nums):
                newList.pop()
            
            for j in newList:
                nums.remove(j)
               
        return len(nums)
    

print(Solution.removeDuplicates([1,1,1,1]))

class Solution2:
    def removeDuplicates(nums) -> int:
        j = 1
        for i in range(1, len(nums)):
            print("This is I: ", i)
            if nums[i] != nums[i - 1]:
                print("if ", nums[i],"does not = ", nums[i -1])
                nums[j] = nums[i]
                print(nums[j], " equals ", nums[i])
                j += 1
        return j
    
print(Solution2.removeDuplicates([1,1,2,3]))
    





