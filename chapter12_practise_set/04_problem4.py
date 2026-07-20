try:
    a = int(input("Enter a number "))
    b = int(input("Enter b number "))

    print(f"The result of a/b is: {a/b}")

except ZeroDivisionError as e:
    print("Infinite")