from functools import reduce


l = [1,2,5,66,55,98,985,758,86]

def greater(a,b):
    if (a>b):
        return a
    return b

print(reduce(greater, l))

