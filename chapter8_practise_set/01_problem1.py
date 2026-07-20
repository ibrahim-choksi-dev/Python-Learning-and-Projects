

def greatestNumber():
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    c = int(input("Enter number c: "))

    if(a>b and a>c):
        print(f"A is greater {a}")

    elif(b>a and b>c):
        print(f"B is greater {b}")

    elif(c>a and c>b):
        print(f"C is greater {c}")

    else:
        print("Something wrong you did....")


greatestNumber()
