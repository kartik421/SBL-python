class Employee:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def show(self):
        print(f"{self.name} is an employee whose ID is {self.ID}")

e1 = Employee("KARTIK",14)
e1.show()
print(e1.name)
print(e1.ID)
