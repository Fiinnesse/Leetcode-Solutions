nums = [2,7,11,15]
nums2 = [3,2,4]
nums3 = [3,3]

target = 9
list2 = []

def twosum(list, target, list2):
    nl = len(list)
    print(list)

    for x in range(nl -1):
        for y in range(x + 1, nl):
            j = list[x] + list[y]
            if j == target:
                return [x, y]
            
    
      
print('test 1')
print(twosum(nums,target,list2))
print('test 2')
print(twosum(nums3,6,list2))
print('test 3')
print(twosum(nums2, 6, list2))      