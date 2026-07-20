import os

# Specify the directory path
path = r"D:\python_cwh_17_5_26\chapter1_practise_set"

# Get the list of files and folders
contents = os.listdir(path)

# Print each item
print("Contents of the directory:")
for item in contents:
    print(item)