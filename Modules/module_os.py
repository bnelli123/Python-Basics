import os
print(os.getcwd())
print(os.listdir())
try: 
    os.mkdir("/tmp/dir1")
except FileExistsError:
    print("Dir exists")
print(os.listdir("/tmp"))

if not os.path.exists("/tmp/dir1"):
    os.mkdir("/tmp/dir1")


print(os.environ['HOME'])
print(os.environ['PATH'])