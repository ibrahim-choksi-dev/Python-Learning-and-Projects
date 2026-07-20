with open("this_copy.txt") as f:
    content1 = f.read()


with open("this.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("The contents of the files are the same." )

else:
    print("The contents of the files are different." )  