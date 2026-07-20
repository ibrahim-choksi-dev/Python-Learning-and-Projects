class Employee:
    language = "Python" # Class attribute, shared by all instances of the class
    salary = 1200000

    def __init__(self, name, language, salary): # dundder method, which is automatically called 
         print("I am creating an employee object")
         self.name = name
         self.language = language
         self.salary = salary

    def getInfo(self):
            print(f"The language is {self.language} and the salary is {self.salary}")
    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

mohammad = Employee("Mohammad", "Python", 1200000)
print(mohammad.name,mohammad.language,mohammad.salary)