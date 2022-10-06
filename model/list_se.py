from model.kid import Kid
from model.node import Node


class ListSE:
    def __init__(self):
        self.head = None
        self.size =0

    def add(self, kid:Kid):
        if self.head == None:
            self.head = Node(kid)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            # Estoy parado en el último
            temp.next = Node(kid)
        self.size+=1

    def add_to_start(self, kid:Kid):
        if self.head == None:
            self.head = Node(kid)
        else:
            newNode = Node(kid)
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def invert(self):
        if self.head != None:
            temp = self.head
            listCp = ListSE()
            while temp != None:
                listCp.add(temp.data)
                temp = temp.next
            self.head = listCp.head


