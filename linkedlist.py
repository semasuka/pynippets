class Node:
    #initialize the head node to none if not provided and set the next node to none
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None


    def append(self,data):
        #if the linkedlist is empty
        if self.head is None:
            self.head = Node(data)
        else:
            #creating the node with the data passed in
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            #when we have reached the end of list
            current_node.next = Node(data)


    def display(self):
        #container for the nodes
        node_elements = []
        current_node = self.head

        while current_node.next is not None:
            node_elements.append(current_node.data)
            current_node = current_node.next
        print(node_elements)

    def length(self):
        current_node = self.head
        index_count = 0
        while current_node.next is not None:
            current_node = current_node.next
            index_count +=1
        return index_count

    def get(self,index):
        if index >= self.length():
            print("Index out of range")
            return
        current_node = self.head
        index_count = 0
        while current_node.next is not None:
            current_node = current_node.next
            if index == index_count:
                return current_node.data
            else:
                index_count+=1

    def remove(self,index):
        if index >= self.length():
            print("Index out of range")
            return
        current_node = self.head
        index_count = 0
        while current_node.next is not None:
            last_node = current_node
            current_node = current_node.next

            if index == index_count:
                #set the last node to the node after the next node
                last_node.next = current_node.next
                return
            else:
                index_count+=1

    def insert_first(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_first(self):
        if self.head is not None:
            delete_node = self.head
            the_new_head = delete_node.next
            self.head = the_new_head
            return delete_node.next.data
        else:
            return None



my_linkedlist = Linkedlist()
my_linkedlist.append(5)
my_linkedlist.append(0)
my_linkedlist.append(19)
my_linkedlist.append(88)
my_linkedlist.display()
print(my_linkedlist.length())
print(my_linkedlist.get(2))
my_linkedlist.remove(2)
my_linkedlist.display()
