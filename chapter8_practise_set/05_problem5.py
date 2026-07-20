'''
    ***
    **
    *
'''

def star(n):
    if(n==0):
        return
    print("*" * n)
    star(n-1)

star(5)