class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def search(self, item):
        if item in self.items:
            return f"Item {item} found at position {len(self.items) - self.items[::-1].index(item)}"
        else:
            return f"Item {item} not found"

    def is_empty(self):
        return len(self.items) == 0


def main():
    stack = Stack()

    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Search")
        print("5. Check if the stack is empty")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter item to push: ")
            stack.push(item)
            print(f"{item} pushed to stack.")
        elif choice == 2:
            popped_item = stack.pop()
            print(f"Popped item: {popped_item}")
        elif choice == 3:
            print(f"Top item of the stack: {stack.peek()}")
        elif choice == 4:
            item = input("Enter item to search: ")
            print(stack.search(item))
        elif choice == 5:
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
