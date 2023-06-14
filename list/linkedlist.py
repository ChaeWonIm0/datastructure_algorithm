class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        # 맨뒤의 node가 new_node를 가리켜야 함
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll)

class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            front = self.head
            while(front.next):
                front = front.next
            front.next = new_node

linkedlist = LinkedList()
linkedlist.append(1)