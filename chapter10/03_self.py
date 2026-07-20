class Employee:
    language = "Python" # Class attribute, shared by all instances of the class
    salary = 1200000

    def getInfo(self):
            print(f"The language is {self.language} and the salary is {self.salary}")
    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

mohammad = Employee()
mohammad.language = "Java" # This creates an instance attribute 'language' for the mohammad instance, which shadows the class attribute
print(mohammad.language) # Output: Java, because the instance attribute shadows the class attribute    


mohammad.greet() # This will call the greet method for the mohammad instance. It will print "Hello, welcome to the company!" because the greet method does not use any class or instance
mohammad.getInfo() # This will call the getInfo method for the mohammad instance. It will print the language and salary for the mohammad instance. Since we have created an instance attribute 'language' for the mohammad instance, it will print 'Java' as the language and 1200000 as the salary. If we had not created an instance attribute 'language' for the mohammad instance, it would have printed 'Python' as the language and 1200000 as the salary, because it would have used the class attribute 'language'. 
# Employee.getInfo(mohammad) # This is how we can call the method using the class name and passing the instance as an argument. It will give the same output as mohammad.getInfo()    
# Employee.greet(mohammad) # This is how we can call the method using the class name and passing the instance as an argument. It will give the same output as mohammad.greet()