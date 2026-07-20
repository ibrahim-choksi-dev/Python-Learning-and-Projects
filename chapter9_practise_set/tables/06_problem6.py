with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("Found")

else:
    print("Not found")