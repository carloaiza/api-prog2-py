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

    def add_by_position(self,position:int,kid:Kid):
        if position == 1:
            self.add_to_start(kid)
        else:
            postemp =1
            temp = self.head;
            while postemp < (position-1):
                temp = temp.next
                postemp = postemp +1

            newNode = Node(kid)
            newNode.next = temp.next
            temp.next = newNode
            self.size += 1

    def mix_by_gender(self):
        if self.size > 1:
            contM =1
            contF = 2
            temp = self.head
            listCp = ListSE()
            while temp != None:
                if temp.data.gender =='M':
                    if contM > listCp.size:
                        listCp.add(temp.data)
                    else:
                        listCp.add_by_position(contM, temp.data)
                    contM += 2
                else:
                    if contF > listCp.size:
                        listCp.add(temp.data)
                    else:
                        listCp.add_by_position(contF, temp.data)
                    contF += 2
                temp = temp.next
            self.head = listCp.head


