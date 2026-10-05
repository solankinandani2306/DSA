class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Sll:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def insert_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

s = Sll()

while True:
    print("1. Insert at Beginning")
    print("2. Insert at Last")
    print("3. Insert at Specific Position")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        data = int(input("Enter Data: "))
        s.insert_begin(data)

    elif ch == 2:
        data = int(input("Enter Data: "))
        s.insert_last(data)

    elif ch == 3:
        data = int(input("Enter Data: "))
        pos = int(input("Enter Position: "))
        s.insert_position(data, pos)

    elif ch == 4:
        s.display()

    elif ch == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
