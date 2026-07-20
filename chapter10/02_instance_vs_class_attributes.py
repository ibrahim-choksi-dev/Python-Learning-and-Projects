class Employee:
    language = "Python" # Class attribute, shared by all instances of the class
    salary = 1200000

mohammad = Employee()
mohammad.language = "Java" # This creates an instance attribute 'language' for the mohammad instance, which shadows the class attribute
print(mohammad.language) # Output: Java, because the instance attribute shadows the class attribute     