import os
print(os.getcwd())
try:
    f = open("abc2.txt", "x")
    print("File created successfully")
    print(f.name, f.mode, f.buffer, f.fileno)
    f.close()
except FileExistsError:
    print("File already exists")


# f1 = open("abc2.txt", "r+")
# f1.write("Hello\n")
# f1.write("Bala")
# print(f1.read())
# f1.close()

