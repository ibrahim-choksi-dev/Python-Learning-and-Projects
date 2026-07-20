'''
factorial(0) = 1
factorial(5) = 5*4*3*2*1 = 120
factorial(n) = n*n-1*....3*2*1

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")