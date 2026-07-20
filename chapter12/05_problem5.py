with(
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    content1 = f1.read()
    content2 = f2.read()

    print("Content of file1.txt:")
    print(content1)

    print("Content of file2.txt:")
    print(content2)
