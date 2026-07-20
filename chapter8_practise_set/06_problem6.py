def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter the value of inches: "))

print(f"The corresponding value in cms is {inch_to_cms(n)}")