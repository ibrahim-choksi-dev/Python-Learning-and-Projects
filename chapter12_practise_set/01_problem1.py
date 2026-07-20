try:

    with open("1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Zazakallah")

with open("2.txt","r") as f:
    print(f.read())

with open("3.txt","r") as f:
    print(f.read())