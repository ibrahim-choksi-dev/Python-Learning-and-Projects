n = int(input("Enter a n: "))

#5! = 1*2*3*4*5

product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")
