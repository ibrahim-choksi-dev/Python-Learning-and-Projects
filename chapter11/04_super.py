class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a) # Prints the a attribute of Employee class


# p = Programmer()
# print(p.a) # Prints the a attribute of Employee class since Programmer class inherits from Employee class
# print(p.b) # Prints the b attribute of Programmer class
# # print(p.c) # This will raise an AttributeError since Programmer class does not have attribute c    

m = Manager()
print(m.a) # Prints the a attribute of Employee class since Manager class inherits from Programmer class which inherits from Employee class
print(m.b) # Prints the b attribute of Programmer class since Manager class inherits from Programmer class
print(m.c) # Prints the c attribute of Manager class
