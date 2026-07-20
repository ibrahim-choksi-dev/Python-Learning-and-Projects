class Deno:
    a = 4


o = Deno()
print(o.a) #Prints the class attribute because instance attribute is not defined yet    
o.a = 0 #Instance attribute is defined here
print(o.a) #Prints the instance attribute because instance attribute is defined and it has higher priority than class attribute 
print(Deno.a) #Prints the class attribute