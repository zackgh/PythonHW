"""
homeowork 22
singly linked list 
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
class linkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return 
        else:
            lastNode = self.head #make a duplicate of the head pointer
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = newNode

    def prepend(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return 
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAfterNode(self,prevNode,data):
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
    
    def printList(self):
        curNode = self.head
        while curNode != None:
            print(curNode.data)
            curNode = curNode.next

    def deleteNode(self,key):
        curNode = self.head
        if curNode != None and curNode.data == key:
            self.head=  curNode.next
            curNode = None
            return 
        else:
            prev = None
            while curNode != None and curNode.data != key:
                prev = curNode
                curNode = curNode.next
            if curNode == None:
                print("The data is not found in the list")
                return 
            else:
                prev.next = curNode.next
                curNode = None

    def deleteAtPos(self,pos):
        curNode = self.head
        if pos == 0:
            self.head = curNode.next
            curNode = None
            return 
        else:
            cnt = 0
            prev = None
            while curNode != None and cnt != pos:
                prev = curNode
                curNode = curNode.next
                cnt+=1
            if curNode == None:
                print("The node doesn't exist")
                return 
            else:
                prev.next = curNode.next
                curNode=None


    def len_iterative(self):
        cnt = 0
        curNode = self.head
        while curNode != None:
            curNode = curNode.next
            cnt+=1
        return cnt

    def swapNode(self,key1,key2):
        if key1 == key2:
            print("Thetwo nodes are the same nodes, cannot be swapped")
            return

        prev1 = None
        curNode1 = self.head
        while curNode1 != None and curNode1.data != key1:
            prev1 = curNode1
            curNode1 = curNode1.next

        prev2=None
        curNode2=self.head
        while curNode2 != None and curNode2.data != key2:
            prev2 = curNode2
            curNode2 = curNode2.next

        if curNode1==None or curNode2 == None:
            print("THe nodes dont exist in the list")
            return 
        else:
            if prev1 == None:
                self.head=curNode2
                prev2.next = curNode1
            elif prev2 == None:
                self.head = curNode1
                prev2.next = curNode1

            temp1 = curNode1.next
            temp2 = curNode2.next
            curNode1.next = temp2
            curNode2.next = temp1

    def reserve_iterative(self):
        prev = None
        curNode = self.head
        while curNode != None:
            nxt_temp = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = nxt_temp
        self.head = prev


# Tests

lst = linkedList()
lst.append('A')
lst.append('B')
lst.append('C')

lst.prepend('D')
lst.deleteNode('A')
lst.deleteAtPos(0)
print(lst.len_iterative())
lst.swapNode('A','C')
lst.swapNode('A','A')
lst.swapNode('E','F')
lst.swapNode('B','C')
lst.swapNode('A','B')

lst.reserve_iterative()
