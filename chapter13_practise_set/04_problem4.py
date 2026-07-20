#Filter Example
def divisible5(n):
    if(n%5==0):
        return True
    return False

a = [1,2,5,66,55,98,985,758,9986]
f = list(filter(divisible5, a))
print(f)
