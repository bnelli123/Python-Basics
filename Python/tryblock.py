try:
    x = int("abc")
except:
    print("Type error")


try:
    y = 10/0
except ZeroDivisionError:
    print("Can't divide by zero")


try:
    x = int("abc")
    y = 10/0
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Can't divide by 0")
finally:
    print("This should run")