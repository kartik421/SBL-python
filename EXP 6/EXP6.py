class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        for _ in range(position - 1):
            if current_node.next:
                current_node = current_node.next
            else:
                raise IndexError("Index out of range")
        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def replace(self, old_data, new_data):
        current_node = self.head
        while current_node:
            if current_node.data == old_data:
                current_node.data = new_data
            current_node = current_node.next

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

if __name__ == "__main__":
    linked_list = LinkedList()

    while True:
        print("\nLinked List Operations:")
        print("1. Append")
        print("2. Insert")
        print("3. Remove")
        print("4. Replace")
        print("5. Search")
        print("6. Display")
        print("7. Size")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter data to append: ")
            linked_list.append(data)
        elif choice == 2:
            data = input("Enter data to insert: ")
            position = int(input("Enter position to insert: "))
            linked_list.insert(data, position)
        elif choice == 3:
            data = input("Enter data to remove: ")
            linked_list.remove(data)
        elif choice == 4:
            old_data = input("Enter data to replace: ")
            new_data = input("Enter new data: ")
            linked_list.replace(old_data, new_data)
        elif choice == 5:
            data = input("Enter data to search: ")
            if linked_list.search(data):
                print("Data found in the linked list.")
            else:
                print("Data not found in the linked list.")
        elif choice == 6:
            print("Linked List:")
            linked_list.display()
        elif choice == 7:
            print("Size of the linked list:", linked_list.size())
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
