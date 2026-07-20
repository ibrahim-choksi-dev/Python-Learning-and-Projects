
f = open("meri_baat.txt")
content = f.read()
if("ishq" in content):
    print("The word ishq is present in the content... ")

else:
    print("The word ishq is not present in the content... ")

f.close()