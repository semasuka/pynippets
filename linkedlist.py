class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def append(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(data)

    def display(self):
        if self.head is None:
            print("empty linked list")
            return
        else:
            elements = []
            cur = self.head
            while cur is not None:
                elements.append(cur.data)
                cur = cur.next
            print(elements)

    def length(self):
        index_count = 0
        cur = self.head
        while cur is not None:
            index_count+=1
            cur = cur.next
        return index_count

    def get(self,index):
        if self.head is None:
            print("empty linked list")
            return
        else:
            if index >= self.length():
                raise IndexError("Index out of bound")
            cur = self.head
            index_count = 0
            while cur is not None:
                if index_count == index:
                    return cur.data
                else:
                    index_count += 1
                    cur = cur.next

    def remove(self,index):
        if self.head is None:
            print("empty linked list")
            return
        else:
            if index >= self.length():
                raise IndexError("Index out of bound")
            elif index == 0:
                self.remove_first()
            else:
                cur = self.head
                index_count = 1
                while cur is not None:

                    last = cur
                    cur = cur.next

                    if index == index_count:
                        last.next = cur.next
                        return
                    else:
                        index_count+=1


    def remove_first(self):
        if self.head is None:
            print("empty linked list")
            return
        else:
            cur = self.head
            self.head = cur.next

    def insert_first(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            new_node.next = cur
            self.head = new_node







my_linkedlist = Linkedlist()
my_linkedlist.append(5)
my_linkedlist.append(0)
my_linkedlist.append(19)
my_linkedlist.append(88)
my_linkedlist.display()
# print(my_linkedlist.length())
# print(my_linkedlist.get(2))
# my_linkedlist.remove(2)
# my_linkedlist.display()
