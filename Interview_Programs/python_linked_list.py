class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        """
        appending a node at the end
        :param data: node to be appended at the end
        :return:
        """
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def insert(self, data, index):
        """
        adding node to a particular index
        :param data: node to be appended
        :param index: index where node is to be appended.
        :return:
        """
        new_node = Node(data)
        if index > self.length():
            print('Error: index greater than linkedList size')
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = new_node
                new_node.next = cur_node
                return
            cur_idx+=1


    def length(self):
        """
        find the size of the linked list
        :return:
        """
        cur_node = self.head
        total = 0
        while cur_node.next is not None:
            cur_node = cur_node.next
            total+=1
        return total

    def display(self):
        """
        print data inside the linked list.
        :return: list of items in the linked list
        """
        elem = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elem.append(cur_node.data)
        print(elem)

    def get(self, index):
        """
        Get an element based on the index
        :param index:
        :return:
        """
        if index > self.length():
            print('Error: index is greater the length of linkedList')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx+=1

    def erase(self, index):
        """
        removing an element based on the index provided by the user.
        :param index:
        :return:
        """
        if index > self.length():
            print('Error: index is greater than length of linkedList')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx+=1

    def delete_node(self, data):
        """
        Delete a node based on value provided by the user
        :param data: the node to be deleted
        :return:
        """
        cur_node = self.head
        while cur_node.next is not None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_node.data == data:
                last_node.next = cur_node.next
                return
        print(str(data) + ' not found in the linked List')



my_list = LinkedList()
print(my_list.length())
my_list.append(1)
my_list.append(3)
my_list.display()
print(my_list.length())
my_list.insert(2,1)
my_list.display()
print(my_list.length())
my_list.erase(1)
my_list.display()
print(my_list.length())
my_list.delete_node(3)
my_list.delete_node(4)
