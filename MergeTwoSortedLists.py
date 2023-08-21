# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = ListNode(data)
        if self.head:
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        list = []
        current = self.head
        while(current):
            if current.val != None:
                list.append(current.val)
                #print(current.val)
                current = current.next
            else:
                pass
        return list

class Solution(ListNode, LinkedList):
    def mergeTwoLists(self, list1, list2):
        
        LL = LinkedList()
        fl = list1 + list2
        fl.sort()

        if fl != []:
            LL.head = ListNode(fl[0])
            for x in fl[1::]:
                LL.insert(x)
        else:
            return fl
        
        return LL.printLL()
    
        


list1 = [1,2,4]
list2 = [1,2,3]

print(Solution().mergeTwoLists(list1, list2))