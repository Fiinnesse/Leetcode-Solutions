class ListNode:
     def __init__(self, val, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2 ):

        
        def getList(llist):
            start = llist.val
            node = llist.next
            fl = []

            if start == None:
                return ("list is empyt")
            elif start != None:
                #print("The first node is: ", start)
                fl.append(start)
                while (node != None):
                    #print("the next node is: ", node.val)
                    fl.append(node.val)
                    node = node.next
                #print()
                return fl
        
        def getTot(list1, list2):
            l1str = ""
            l2str = ""
            totstr = ""
            
            for x in list1:
                l1str += str(x)

            for x in list2:
                l2str += str(x)
            
            total = int(l1str) + int(l2str)

            for x in str(total)[::1]:
                totstr += x

            return totstr
        
        def newList(total):
            listlen = len(total)
            start = ListNode(int(total[listlen-1]))

            for x,y in enumerate(total[1::]):
                new_node = ListNode(int(total[x]))
                new_node.next = start.next
                start.next = new_node

            return start
        
        list1 = getList(l1)
        list2 = getList(l2)
        list1.reverse()
        list2.reverse()
        total = getTot(list1,list2)
        endlist = newList(total)

        return getList(endlist)
    
#l1 = [2,4,3]; l2 = [5,6,4]
s = Solution()
#add = s.addTwoNumbers(l1, l2)

ll = ListNode(2)
ll.next = ListNode(4)
ll.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

#print(l2.next.next.val)
add = s.addTwoNumbers(ll, l2)
print(add)
