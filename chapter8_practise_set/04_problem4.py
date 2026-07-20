'''
    sum(1)=1
    sum(2)= 1+2
    sum(3)= 1+2+3
    sum(4)= 1+2+3+4
    sum(n) = 1+2+3+4+5+6+7+8+9+10.....n-1+n
    sum(n) = sum(n-1) + n
'''


def recFun(n):
    if(n==1):
        return 1
    
    return recFun(n-1) + n

print(recFun(4))