class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    def __init__(self, name, age, salary, address):
        super().__init__(name, age, salary, address)
managers = []

for i in range(10):
    print(f"\nEnter details for Manager {i+1}")
    name = input("Name: ")
    age = int(input("Age: "))
    salary = float(input("Salary: "))
    address = input("Address: ")

    m = Manager(name, age, salary, address)
    managers.append(m)

print("\n--- Manager Details ---")
for m in managers:
    m.display()
    print("---------------------")