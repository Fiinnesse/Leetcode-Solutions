strs = ["flower","flow","flight"]

sl = sorted(strs)
nl = len(strs)

for x in range(len(sl[nl -1])):
    print('x is: ',sl[nl-1])
    for y in range(x + 1, nl):
        print('y is: ',sl[y])
        


#print(pre)
#print(sorted(strs))