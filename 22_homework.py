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


# Tests

lst = linkedList()       #create list
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.printList()

print("\n\n\n Prepend 0")

lst.prepend(0)
lst.printList()

lst.insertAfterNode(lst.head.next,999)
print('\n\n\n Insert 999 after 1 ')
lst.printList()

lst.deleteNode(999)
print("\n\n\n Delete 999")
lst.printList()



