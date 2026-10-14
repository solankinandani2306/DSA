class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = SinglyLinkedList()

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter data: "))
    ll.insert(data)

print("Singly Linked List:")
ll.display()
