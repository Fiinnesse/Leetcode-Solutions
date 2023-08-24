class Solution:
    def majorityElement(nums) -> int:
        
        count = 0
        cur_max = 0
        cur_max_value = 0
        nd = set(nums)
        for x in nd:
            for y in nums:
                if y == x:
                    count += 1
            if count >= cur_max:
                print(x, "new max is: ", count)
                cur_max = count
                count = 0
                cur_max_value = x
            elif count < cur_max:
                print("this is count on: ",x,"count is: ", count,"current max: ", cur_max)
                count = 0
        print("your max is: ", cur_max_value)
        

        
                



nums = [2,2,1,1,1,2,2]

s = Solution.majorityElement(nums)
