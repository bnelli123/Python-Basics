import sys

#sys.argv → list

# for arg in sys.argv[1:]



# print(sys.argv)


# print("Start")
# sys.exit()
# print("This will not run")


# data = sys.stdin.read()
# print(data)

# print("First argument:", sys.argv[1])
# print("Second argument:", sys.argv[2])
# print("Third argument:", sys.argv[3])


for i, arg in enumerate(sys.argv[1:], start=1):
    print(f"Argument {i}: {arg}")