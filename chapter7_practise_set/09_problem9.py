'''
    ***
    * *
    ***
'''

n = int(input("Enter n: "))

for i in range(1, n+1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        # middle rows: star, spaces, star
        print("*" + " " * (n - 2) + "*")