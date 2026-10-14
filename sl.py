class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Sl:
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
            print("empty")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = Sl()

while True:
    print("1. Insert")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        ll.insert(data)
        print("successfully.")

    elif choice == 2:
        print("List:")
        ll.display()

    elif choice == 3:
        print("Exit")
        break

    else:
        print("Invalid")
