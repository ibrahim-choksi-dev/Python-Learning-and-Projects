words = {"donkey","work","too many"}
with open("donkey.txt","r") as f:
    content = f.read()

    for word in words:
        content = content.replace(word, "#" * len(word) )

with open("donkey.txt","w") as f:
    f.write(content)
