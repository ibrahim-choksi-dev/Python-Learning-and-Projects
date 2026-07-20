class Employee:
    language = "Python" # Class attribute, shared by all instances of the class
    salary = 1200000


mohammad = Employee()
mohammad.name = "Mohammad" # Instance attribute, unique to the mohammad instance
print(mohammad.name)
print(mohammad.language)
print(mohammad.salary)


ibrahim = Employee() 
ibrahim.name = "Ibrahim" # Instance attribute, unique to the ibrahim instance 
print(ibrahim.name)
print(ibrahim.language)
print(ibrahim.salary)


#Here name is object attribute and language and salary are class attributes. Class attributes are shared by all instances of the class, while object attributes are unique to each instance.    